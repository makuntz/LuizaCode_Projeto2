from pymongo import MongoClient
from bson.objectid import ObjectId
from decimal import Decimal
import datetime

from src.schemas.user import UserSchema
from src.schemas.address import Address

from src.models.order import (
    create_order
)

from src.models.user import (
    get_user_by_email
)

from src.server.database import connect_db, db, disconnect_db

async def order_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    users_collection = db.users_collection
    address_collection = db.address_collection   
    
     
    email = "lu_domagalu@gmail.com"
    user = await get_user_by_email(
        users_collection,
        email
    )
    
    address_is_true = await address_collection.find_one({"address.is_delivery": True})
    
    order =   {
        "user": user['_id'],
        "price": 1796.4,
        "paid": False,
        "create": datetime.datetime.now(),
        "address": address_is_true
        # "authority": Optional[str] = Field(max_length=100)           
    } 
   
    
    
    if option == '1':
        info_orders_insert = await create_order(
            order_collection,
            order
            
        )        
        
        print(info_orders_insert)
        
    
    if option == '2':
        ...
    

    await disconnect_db()
