import unittest
from sql_mongo_translate_middleware import SqlMongoTranslateMiddleware
from errors import InvalidSqlQueryError

class TestSqlMongoTranslateMiddleware(unittest.TestCase):
    def setUp(self):
        self.middleware = SqlMongoTranslateMiddleware()

    def test_wierd_sql_queries(self):
        queries = [
            # normal query
            'SELECT * FROM Customers where Country = "United States of America"',
            # queries with spaces and tabs
            'SELECT     *   FROM     Customers     where Country      =      "United States of America"  ',
            # lowercase select
            'select * FROM Customers where Country = "United States of America"',
            # lowercase from
            'SELECT * from Customers where Country = "United States of America"',
            # multicase from
            'SELECT * FroM Customers where Country = "United States of America"',
            # multicase select
            'seLECt * FROM Customers where Country = "United States of America"'
        ]
        for query in queries:
            # print(query)
            self.assertEqual(self.middleware.transate(query), 'db.Customers.find({Country = "United States of America"})')
    
    def test_with_single_quote_sql_query(self):
        query = 'SELECT * FROM Customers where Country = \'United States of America\''
        self.assertEqual(self.middleware.transate(query), 'db.Customers.find({Country = "United States of America"})')

    def test_with_semi_colon_at_the_end(self):
        query = 'SELECT * FROM Customers where Country = "United States of America";'
        self.assertEqual(self.middleware.transate(query), 'db.Customers.find({Country = "United States of America"})')

        # semi-colons with a tab
        query = 'SELECT * FROM Customers where Country = \"United States of America\"   ;  '
        self.assertEqual(self.middleware.transate(query), 'db.Customers.find({Country = "United States of America"})')

    def test_invalid_sql_query(self):
        # empty sql query
        query = ''
        self.assertRaises(InvalidSqlQueryError, self.middleware.transate, query)

        # sql query without the FROM keyword
        query = 'SELECt * Customers'
        self.assertRaises(InvalidSqlQueryError, self.middleware.transate, query)

        # sql query withought value
        query = 'select * FROM customers where ABC'
        self.assertRaises(InvalidSqlQueryError, self.middleware.transate, query)

        # sql query withought value
        query = 'select from where ='
        self.assertRaises(InvalidSqlQueryError, self.middleware.transate, query)

if __name__ == '__main__':
    unittest.main()