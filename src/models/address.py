

async def create_address(address_collection, address, user):
    try:
        address = await address_collection.insert_one({"user": user, "address": address})
        

        if address.inserted_id:
            address = await get_address(address_collection, address.inserted_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')
        

async def delete_address(addresss_collection, address_id):
    try:
        address = await addresss_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')




