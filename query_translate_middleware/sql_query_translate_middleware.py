from query_translate_middleware import QueryTranslateMiddleware
from errors import InvalidSqlQueryError
import re

'''
This class represents a middleware component which 
translates an sql query to a query in some other
query langauage
'''
class SqlQueryTranslateMiddleware(QueryTranslateMiddleware):
	def transate(self, input_query):
		if not self.validate_sql_query(input_query):
			raise InvalidSqlQueryError()
		return self.translate_sql_query(input_query)

	'''
	Decodes an sql query of the form 
	SELECT * FROM A WHERE B = "C"
	and returns A, B, C
	'''
	def decode_sql_query(self, query):
		query_lower = query.lower()
		words_lower = query_lower.split()
		words = query.split()

		try:
			table = words[words_lower.index("from") + 1]
		except ValueError as e:
			raise InvalidSqlQueryError
			
		column = words[words_lower.index("where") + 1]
		value = " ".join(words[words_lower.index("=") + 1:])

		# remove semi-colon if one exists
		if value.endswith(';'):
			value = value[:-1]
		value = " ".join(value.split())

		# remove single/double quotes from value,
		# if one exists
		if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
			value = value[1:-1]

		return table, column, value

	def translate_sql_query(self, query):
		raise NotImplementedError('method translate for class QueryTranslateMiddleware not implemented')

	def validate_sql_query(self, query):
		l = query.lower().split()
		try:
			return l[0] == 'select' and l[2] == 'from' and l[4] == 'where' and l[6] == '='
		except IndexError:
			return False
		