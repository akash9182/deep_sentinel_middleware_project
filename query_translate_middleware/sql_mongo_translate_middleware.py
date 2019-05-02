from .sql_query_translate_middleware import SqlQueryTranslateMiddleware

class SqlMongoTranslateMiddleware(SqlQueryTranslateMiddleware):
	def translate_sql_query(self, query):
		table, column, value = self.decode_sql_query(query)
		output_string = "db." + table + ".find({" + column + " = \"" + value + "\"})"
		return output_string