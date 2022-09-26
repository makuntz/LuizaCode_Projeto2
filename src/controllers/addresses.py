from pymongo import MongoClient
from bson.objectid import ObjectId

from src.models.address import (
    create_address,
    get_address,
    delete_address
    
)

from src.models.user import (
    get_user_by_email
)

from src.server.database import connect_db, db, disconnect_db

async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection = db.address_collection
    users_collection = db.users_collection
    
    
    address =   {

                "street": "Rua Abraao Caixe, 719",
                "cep": "14020630",
                "district": "Jd Irajá",
                "city": "Ribeirao Preto",
                "state": "São Paulo",
                "is_delivery": True
    }
    
    test_new_address = {
        
                "street": "Rua Joaquim Marques Castelhano, 290",
                "cep": "13660000",
                "district": "Jd Independencia",
                "city": "Sao carlos",
                "state": "São Paulo",
                "is_delivery": True
    }
    
    email = "lu_domagalu@gmail.com"
    user = await get_user_by_email(
        users_collection,
        email
    )
    
    search_address_user = await address_collection.find_one({"user._id": user["_id"]})
    
    if option == '1':
        # create address
            if search_address_user == None:
            
                address = await create_address(
                    address_collection,
                    address,
                    user['_id']
                    
                )
                print(address)
            else: 
                            
                await address_collection.update_one(
                    {"_id": search_address_user["_id"]},
                    {
                        "$set": {
                            "address": test_new_address
                        }
                    }
                )
    
    address_id = ObjectId("632ba64cf1d22c9a545da707")
    
    if option == '2':
        
        pick_address = await get_address(
            address_collection,
            address_id
        )
        
        print(pick_address)
        
    
    if option == '3':
        
        deleting = await delete_address(
            address_collection,
            address_id
        )
        print('Deletou')

    await disconnect_db()
