from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from login import Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, \
                  create_access_token, get_current_active_user
from datetime import timedelta
from user import RegisterUser, UserPersistance, User

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