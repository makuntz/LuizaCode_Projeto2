from pymongo import MongoClient
from bson.objectid import ObjectId
from decimal import Decimal
import datetime
from src.models.order_item import create_order_item, delete_order_item, delete_product, insert_product, total_sum



from src.server.database import connect_db, db, disconnect_db

async def order_item_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_collection = db.order_collection
    product_collection = db.product_collection
    order_item_collection = db.order_items_collection
     
    
    order_id = ObjectId('632e32d45e9b24cb8ee9e7a8')
    product_id = ObjectId('632cba269beac095430b1c5d')
    order_item_id = ObjectId('6330bed87efea6e56a9608a6')
    
    
    order_found = await order_collection.find_one({'_id': order_id})
    product_found = await product_collection.find_one({'_id': product_id })
    item_found =  'Fritadeira Elétrica sem Óleo/Air Fryer Nell Fit - Preto 3,2L com Timer' 
    
       
    order_items = {
        "order": order_found['_id'],
        "product": product_found
    }
    
        
    if option == '1':
        order_items_insert = await create_order_item(
            order_item_collection,
            order_items
        )
        
        # print(order_items_insert) 
        
    
    ##funcao reclamando do uso do await => procurar sobre o erro 
    if option == '2':
        sum = await total_sum(
            
            order_item_collection
        )
        
        print(sum)
    
    if option == '3':
        deleted_item = await delete_order_item(
            order_item_collection,
            item_found
        )
        print('Produto excluido com sucesso!')
        
    
    if option == '4':
        await delete_product(
            order_item_collection,
            product_id
        
        )
        
    if option == '4':
        await insert_product(
            order_item_collection,
            product_found
        )
       
        
    await disconnect_db()
