async def create_order_item(order_item_collection, order_item):
    try:
        order_item = await order_item_collection.insert_one(order_item)

        if order_item.inserted_id:
            order_item = await get_order(order_item_collection, order_item.inserted_id)
            return order_item

    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order(order_item_collection, order_item_id):
    try:
        data = await order_item_collection.find_one({'_id': order_item_id})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')