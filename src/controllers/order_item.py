from pymongo import MongoClient
from bson.objectid import ObjectId
from decimal import Decimal
import datetime



from src.server.database import connect_db, db, disconnect_db

async def order_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    users_collection = db.users_collection
    address_collection = db.address_collection   
    

    
  
   
    
   

    await disconnect_db()
