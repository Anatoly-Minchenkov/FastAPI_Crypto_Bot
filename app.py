import copy

import uvicorn

from database import crud
import pydantic_models
import fastapi
from fastapi import FastAPI, Query, Body


api = FastAPI()

@api.post('/user/create')
def create_user(user: pydantic_models.User_to_create):
    return crud.create_user(tg_id=user.tg_ID,
                            nick=user.nick if user.nick else None).to_dict()

@api.put('/user/{user_id}')
def update_user(user_id: int, user: pydantic_models.User_to_update = fastapi.Body()):
    return crud.update_user(user).to_dict()

@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = fastapi.Path()): # используя fastapi.Path() мы явно указываем, что переменную нужно брать из пути
    crud.get_user_by_id(user_id).delete()
    return True



@api.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_about_user(user_id):
    return crud.get_user_info(crud.User[user_id])

@api.get('/get_user_balance_by_id/{user_id:int}')
@crud.db_session
def get_user_balance_by_id(user_id):
    crud.update_wallet_balance(crud.User[user_id].wallet)
    return crud.User[user_id].wallet.balance

@api.get('/get_total_balance')
@crud.db_session
def get_total_balance():
    balance = 0.0
    crud.update_all_wallets()
    for user in crud.User.select()[:]:
        balance += user.wallet.balance
    return balance

@api.get("/users")
@crud.db_session
def get_users():
    users = []
    for user in crud.User.select()[:]:
        users.append(user.to_dict())
    return users

@api.get('/user_by_tg_id/{tg_id:int}')
@crud.db_session
def get_user_by_tg_id(tg_id):
    return crud.get_user_info(crud.get_user_by_tg_id(tg_id))

@api.post('/create_transaction')
@crud.db_session
def create_transaction(user_id, transaction):
    return crud.create_transaction(crud.get_user_by_id(user_id), transaction.amount_btc_without_fee,
                                   transaction.receiver_address)

@api.get("/get_user_wallet/{user_id:int}")
@crud.db_session
def get_user_wallet(user_id):
    return crud.get_wallet_info(crud.User[user_id].wallet)

if __name__ == "__main__":
    uvicorn.run("app:api", host="127.0.0.1", port=8000, reload=True)
