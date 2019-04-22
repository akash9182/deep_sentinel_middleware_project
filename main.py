from pymongo import MongoClient
from constants import NAMES, COUNTRIES
import random
from sql_mongo_translate_middleware import SqlMongoTranslateMiddleware

def get_random_element_from_list(l):
    return l[random.randint(0,len(l)-1)]

def populate_database_with_random_values(db):
    # add random entries to the "customer" collection
    for i in range(10000):       
        name = get_random_element_from_list(NAMES)
        country = get_random_element_from_list(COUNTRIES) 
        db.customer.insert_one({
            'name': name,
            'country': country
        })

if __name__ == '__main__':
    # # instantiate a mongo-db client
    # client = MongoClient('localhost:27017')

    # # connect to the databse "test"
    # db = client.test
    middlerware = SqlMongoTranslateMiddleware()
    print(middlerware.transate('Select * from Customer where Country = ‘Germany’'))