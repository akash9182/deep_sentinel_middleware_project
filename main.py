from pymongo import MongoClient
from constants import NAMES, COUNTRIES
import random
from query_translate_middleware.translate import translate_query, get_middlware_instance


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
    middleware = get_middlware_instance('sql', 'mongo')
    translated_query = middleware.transate('Select * from Customer where Country = "Germany"')
    print(translated_query)