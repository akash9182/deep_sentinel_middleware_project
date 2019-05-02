from .sql_mongo_translate_middleware import SqlMongoTranslateMiddleware
from .sql_hbase_translate_middleware import SqlHbaseTranslateMiddleware
from .sql_cassandra_translate_middleware import SqlCassandraTranslateMiddleware

def translate_query(input_language, output_language, input_query):
    middleware = input_output_query_middlware_map[(input_language, output_language)]()
    return middleware.transate(input_query)

input_output_query_middlware_map = {
    ('sql', 'mongo'): SqlMongoTranslateMiddleware,
    ('sql', 'hbase'): SqlHbaseTranslateMiddleware,
    ('sql', 'cassandra'): SqlCassandraTranslateMiddleware
}