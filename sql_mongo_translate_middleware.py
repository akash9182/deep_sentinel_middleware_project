from sql_query_middleware import SqlQueryMiddleware

class SqlMongoTranslateMiddleware(SqlQueryMiddleware):
	def translate_sql_query(self, query):
		pass
