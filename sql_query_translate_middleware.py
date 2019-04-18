from query_translate_middleware import QueryTranslateMiddleware

class SqlQueryTranslateMiddleware(QueryTranslateMiddleware):
	def transate(self, input_query):
		if not self.validate_sql_query(input_query):
			raise ValueError('invalid sql query ' + str(input_query))
		self.translate_sql_query(input_query)
		
	def translate_sql_query(self, query):
		raise NotImplementedError('method translate for class QueryTranslateMiddleware not implemented')

	def validate_sql_query(self, query):
		# TODO: implement validation logic
		return True
