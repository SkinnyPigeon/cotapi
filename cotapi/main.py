from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from login import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, \
                  create_access_token, get_current_active_user
from user import RegisterUser, UserPersistance, User
from transactions import Transactions
from transaction_persistance import TransactionPersistance
from transaction_functions import TransactionFunctions

from request_fields import SavedTransactionRequestBody, \
                           XNumberOfTransactionsRequest, \
                           TransactionByHashRequest, \
                           IncomeRequest, \
                           OutgoingsRequest, \
                           BalanceRequest, \
                           IncomeResponse, \
                           OutgoingsResponse, \
                           BalanceResponse, \
                           UpdatedTransactionResponse, \
                           IndividualTransaction, \
                           SavedTransactionsResponse, \
                           TokenResponse, \
                           SignupResponse, \
                           ProfileResponse

app = FastAPI()


@app.post("/token", response_model=TokenResponse, tags=['TOKEN'])
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


@app.post("/users/signup", tags=['USERS'], response_model=SignupResponse)
def register_user(user: RegisterUser):
    up = UserPersistance(user.username, user.password, user.address)
    registered = up.create_user()
    if registered:
        return {"message": f"{user.username} successfully registered"}
    else:
        return {"message": f"{user.username} already exists in database"}


@app.get("/users/profile", response_model=ProfileResponse, tags=['USERS'])
async def read_my_details(current_user:
                          User = Depends(get_current_active_user)):
    return current_user


@app.get("/transactions/update",
         tags=['TRANSACTIONS'],
         response_model=UpdatedTransactionResponse)
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


@app.post("/transactions/saved",
          tags=['TRANSACTIONS'],
          response_model=SavedTransactionsResponse)
def view_saved_transaction_data(body: SavedTransactionRequestBody,
                                current_user:
                                User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    return tf.retrieve_transactions(body.start, body.end, body.direction)


@app.post("/transactions/recent",
          tags=['TRANSACTIONS'],
          response_model=SavedTransactionsResponse)
def view_x_number_of_transactions(body: XNumberOfTransactionsRequest,
                                  current_user:
                                  User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    transactions = tf.retrieve_last_x_transactions(body.direction, body.limit)
    return transactions


@app.post("/transactions/hash",
          tags=['TRANSACTIONS'],
          response_model=IndividualTransaction)
def search_by_transaction_hash(body: TransactionByHashRequest,
                               current_user:
                               User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    transaction = tf.transaction_by_id(body.tx_hash)
    if transaction:
        return transaction
    else:
        return {"error": "unable to find transaction with hash. \
                          please check it is correct", "tx_hash": body.tx_hash}


@app.post("/balance/outgoings",
          tags=['BALANCE'],
          response_model=OutgoingsResponse)
def view_outgoings(body: OutgoingsRequest,
                   current_user: User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    return {"outgoings": tf.calculate_outgoings(body.start, body.end)}


@app.post("/balance/income", tags=['BALANCE'], response_model=IncomeResponse)
def view_income(body: IncomeRequest,
                current_user: User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    return {"income": tf.calculate_income(body.start, body.end)}


@app.post("/balance/", tags=['BALANCE'], response_model=BalanceResponse)
def view_balance(body: BalanceRequest,
                 current_user: User = Depends(get_current_active_user)):
    tf = TransactionFunctions(current_user.address, current_user.username)
    return {"balance": tf.calculate_balance(body.start, body.end),
            "outgoings": tf.outgoings, "income": tf.income}
