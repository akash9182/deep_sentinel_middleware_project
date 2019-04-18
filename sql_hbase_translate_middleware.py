from sql_query_middleware import SqlQueryMiddleware

class SqlHbaseTranslateMiddleware(SqlQueryMiddleware):
	def translate_sql_query(self, query):
		pass
