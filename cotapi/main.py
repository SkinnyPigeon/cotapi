from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from login import Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, \
                  create_access_token, get_current_active_user
from user import RegisterUser, UserPersistance, User
from transactions import Transactions
from transaction_persistance import TransactionPersistance

app = FastAPI()


@app.post("/token", response_model=Token, tags=['TOKEN'])
async def login_for_access_token(form_data:
                                 OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/signup", tags=['USERS'])
def register_user(user: RegisterUser):
    up = UserPersistance(user.username, user.password, user.address)
    registered = up.create_user()
    if registered:
        return {"message": f"{user.username} successfully registered"}
    else:
        return {"message": f"{user.username} already exists in database"}


@app.get("/users/profile", response_model=User, tags=['USERS'])
async def read_my_details(current_user:
                          User = Depends(get_current_active_user)):
    return current_user


@app.get("/transactions/update", tags=['TRANSACTIONS'])
def save_my_transactions(current_user:
                         User = Depends(get_current_active_user)):
    try:
        transactions = Transactions(current_user.address)
        transactions_to_save = transactions.return_transactions()
        tp = TransactionPersistance(current_user.username,
                                    transactions_to_save
                                    )
        tp.save_transactions()
        return {"detail":
                f"Successfully inserted {tp.get_update_count()} new records"}
    except Exception as e:
        return {"error": str(e)}
