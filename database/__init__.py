import sys
import pymongo
import logging
from pymongo.errors import BulkWriteError
from config import DATABASE, TABLE, mongo_db


def mongoInsert(links:list, database=DATABASE, table=TABLE):
    try:
        myclient = pymongo.MongoClient(mongo_db)
        database = myclient[DATABASE]
        table = database[TABLE]

        table.insert_many(links.copy(), ordered=False)
        quantity = table.count_documents({})
        logging.debug(f"Quantity of documents: {quantity}")
            
        return True
    
    except BulkWriteError as bwe:
        logging.error("ERROR on spider insert_links_mongo:", str(bwe.details))

    except Exception as e:
        logging.error("ERROR on spider insert_links_mongo: ", str(e))


def mongodb_read(database:str=DATABASE, tablename:str=TABLE, query:dict=None, limit=0):
    """read data from mongo db
    Args:
        database (str, optional): database name. Defaults to 'linker'.
        tablename (str, optional): collection name. Defaults to ORIGIN_TABLE.
        query (dict, optional): query to search criterea. Defaults to None.
    Returns:
        (list[dict]): list of dicts with data
    """

    myclient = pymongo.MongoClient(mongo_db)
    database = myclient[database]
    table = database[tablename]

    if query :
        return [ item for item in table.find(query)]

    elif limit > 0:
        return [ item for item in table.find().limit(limit)]

    else: 
        return [ item for item in table.find()]
    