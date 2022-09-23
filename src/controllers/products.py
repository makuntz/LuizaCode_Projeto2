# from pymongo import MongoClient
# from bson.objectid import ObjectId

from src.models.product import (
    create_product,
    get_product,
    delete_product
)

product = {
    "name": "Fritadeira Elétrica sem Óleo/Air Fryer Nell Fit - Preto 3,2L com Timer",
    "description": "A fritadeira elétrica Nell Fit é um eletroportátil que não pode faltar na sua cozinha. O produto proporciona uma alimentação mais saudável, pois não utiliza óleo/Air Fryer em seu processo de cozimento.",
    "price": 369.0,
    "image": "https://a-static.mlcdn.com.br/800x560/fritadeira-eletrica-sem-oleo-air-fryer-nell-fit-preto-32l-com-timer/magazineluiza/222479100/64ef4d6200a6efc6cce6d265588910a9.jpg",
    "code": 222479100
}

product2 = {
    "name" : "Bicicleta Aro 29 Freio a Disco 21M. Velox Branca/Verde - Ello Bike",
    "description" : "Bicicleta produzida com materiais de qualidade e foi criada pensando nas pessoas que desejam praticar o ciclismo e ter uma vida saudável.",
    "price" : 898.2,
    "image" : "https://a-static.mlcdn.com.br/800x560/bicicleta-aro-29-freio-a-disco-21m-velox-branca-verde-ello-bike/ellobike/6344175219/b84d5dd41098961b4c2f397af40db4ce.jpg",
    "code" : 97880
}



from src.server.database import connect_db, db, disconnect_db

async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    products_collection = db.product_collection
    
    if option == '1':
        product_created = await create_product(
            products_collection,
            product2
        ) 
        print('Produto criado com sucesso!')
        
    product_code = 97880
    if option == '2':
        picked_product = await get_product(
            products_collection,
            product_code
        )
        print(picked_product)
        
    if option == '3':
        await delete_product(
            products_collection,
            product_code
        ) 
        print('Produto Excluído com sucesso')
        
        
    await disconnect_db()