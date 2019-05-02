from pymongo import MongoClient
from constants import NAMES, COUNTRIES
import random
from sql_mongo_translate_middleware import SqlMongoTranslateMiddleware
from sql_hbase_translate_middleware import SqlHbaseTranslateMiddleware
from sql_cassandra_translate_middleware import SqlCassandraTranslateMiddleware

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

def translate_query(input_language, output_language, input_query):
    middleware = input_output_query_middlware_map[(input_language, output_language)]()
    return middleware.transate(input_query)

input_output_query_middlware_map = {
    ('sql', 'mongo'): SqlMongoTranslateMiddleware,
    ('sql', 'hbase'): SqlHbaseTranslateMiddleware,
    ('sql', 'cassandra'): SqlCassandraTranslateMiddleware
}

if __name__ == '__main__':
    # # instantiate a mongo-db client
    # client = MongoClient('localhost:27017')

    # # connect to the databse "test"
    # db = client.test
    translated_query = translate_query('sql', 'mongo', 'Select * from Customer where Country = "Germany"')
    print(translated_query)