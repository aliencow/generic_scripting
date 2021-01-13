Para instalar Mongo db en ubuntu 18.04:
======================================

https://websiteforstudents.com/install-mongodb-on-ubuntu-18-04-lts-beta-server/



Para desinstalar mongo db de ubuntu totalmente:
===============================================

https://www.anintegratedworld.com/uninstall-mongodb-in-ubuntu-via-command-line-in-3-easy-steps/


Step 1: Stop the service

sudo service mongod stop

Step 2: Remove packages

sudo apt-get purge mongodb-org*

Step 3: Remove data directories

sudo rm -r /var/log/mongodb

sudo rm -r /var/lib/mongodb

-r means recursive

Reference: https://docs.mongodb.org/v3.0/tutorial/install-mongodb-on-ubuntu/


Installing MongoDB on Windows Subsystem for Linux (WSL) 2 :
===========================================================
https://dev.to/seanwelshbrown/installing-mongodb-on-windows-subsystem-for-linux-wsl-2-19m9


INSERT -- Inertar registros en mongodb
======================================

mydict = { "name": "John", "address": "Highway 37" }
db.COLLECTION_NAME.insertOne(mydict)  inserta un registro
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
db.COLLECTION_NAME.insert(mydict)  inserta varios registros (documents)


FIND -- Buscar registros en mongodb
===================================

db.COLLECTION_NAME.find(FIND_CRITERIA, PROJECTION)

CRITERIA:
db.collection_name.find()  find All
db.collection_name.find({}).pretty()  find all pretty

db.collection_name.findOne("key":"value") busca uno con el valor value en key
db.collection_name.find("key":"value") busca todos con el valor value en key
<  : db.collection_name.find("key":{$lt:"value"}) busca los menores que uno con el valor value en key ($lt less than)
<= : db.collection_name.find("key":{$lte:"value"}) busca los menores o iguales al valor value en key ($lte less than or equals)
>  : db.collection_name.find("key":{$gt:"value"}) busca los mayores que uno con el valor value en key ($gt greater than)
>= : db.collection_name.find("key":{$gte:"value"}) busca los mayores o iguales que el valor value en key ($gte greater than or equals)
!= : db.collection_name.find("key":{$ne:"value"}) busca los distintos del valor value en key ($ne not equals)

and db.collection_name.find({$and: [{"key": "value" or {contidion}},{"key": "value" or {contidion}}]})
or  db.collection_name.find({$or : [{"key": "value" or {contidion}},{"key": "value" or {contidion}}]})

PROJECTION
indica cuales de los campos queremos que devuelva (en lugar de devolverlos todos como por defecte)
db.mycollection.find({}, { "name": 1, "address": 1}) En este ejemplo busca todos
                                                     los registros y devuelve unicamente el
                                                     contenido de los campos nombre y domicilio
LIMIT limitar los regsitros a encontrar
db.COLLECTION_NAME.find().limit(NUMBER) - devuelve como máximo NUMBER de registros
db.mycollection.find({}).pretty().limit(8) devuelve 8 registros en pretty
db.mycollection.find({}).limit(8) devuelve 8 registros


SORT ordenar los registros a encontrar
db.COLLECTION_NAME.find().sort({Key1: 1, key2: 1})
db.mycollection.find({}).pretty().sort({"address":1,"name":1}) en este ejemplo nos devuelve la
                                                               busqueda ordenada por address y luego
                                                               por nombre

UPDATE -- Actualicacion en mongodb (update and save):
====================================================

db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATA, MULTI)
db.mycollection.update({"_id":"5fef5b8c5b597f1a457a9e0e"},{$set:{"name": "Winston"}}) un ejemplo..
para updates multiples hay que añadir multi:true (por defecto solo actualiza uno).
db.mycollection.update({"_id":"5fef5b8c5b597f1a457a9e0e"},{$set:{"name": "Winston"}}, {multi:true})


DELETE -- Eliminar registros con mongodb
========================================

db.COLLECTION_NAME.remove(DELETING_CRITERIA, JUSTONE)

db.mycollection.remove({"name":"William"})
para borrar un solo registro hay que especificar justOne:true (por defecto borra todos los que encuentre)
db.mycollection.remove({"name":"William"}, {justOne:true})
