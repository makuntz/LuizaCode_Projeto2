async def create_product(products_collection, product):
    try:
        product = await products_collection.insert_one(product)

        if product.inserted_id:
            product = await get_product(products_collection, product.inserted_id)
            return product

    except Exception as e:
        print(f'create_user.error: {e}')

async def get_product(products_collection, product_code):
    try:
        data = await products_collection.find_one({'code': product_code})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')
        

async def delete_product(products_collection, product_code):
    try:
        product = await products_collection.delete_one(
            {'code': product_code}
        )
        if product.deleted_count:
            return {'status': 'product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')
