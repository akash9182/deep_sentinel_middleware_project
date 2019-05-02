from sql_query_translate_middleware import SqlQueryTranslateMiddleware

class SqlCassandraTranslateMiddleware(SqlQueryTranslateMiddleware):
	def translate_sql_query(self, query):
		pass

