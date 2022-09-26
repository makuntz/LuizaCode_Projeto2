
async def create_order_item(order_item_collection, order_item):
    try:
        order_item = await order_item_collection.insert_one(order_item)

        if order_item.inserted_id:
            order_item = await get_order_item(order_item_collection, order_item.inserted_id)
            return order_item

    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order_item(order_item_collection, order_item_id):
    try:
        data = await order_item_collection.find_one({'_id': order_item_id})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')
        
async def delete_order_item(order_item_collection, name):
    try:
        order_item = await order_item_collection.delete_one(
            {'order_item.name': name}
        )
        if order_item.deleted_count:
            return {'status': 'order_item deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')
        

async def delete_product(order_item_collection, product_id):
    
    try:
        product = await order_item_collection.update_one(
            {'product._id': product_id},
            {'$set': {'product': {}} }
            
        )
        print(product)
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')
        

async def insert_product(order_item_collection, product):
    try:
        product = await order_item_collection.update_one(
            {'product': {}},
            {'$set': product }
            
        )
        print(product)
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')
        
        
##funcao reclamando do uso do await => procurar sobre o erro        
async def total_sum(order_item_collection):
    try:
        total_sum = await order_item_collection.aggregate([
            {
                "$group": {"_id": "$price", "count": {"$sum": "$price"}}            
            }
        ])
        
        print(total_sum)
        # if total_sum.deleted_count:
        #     return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')