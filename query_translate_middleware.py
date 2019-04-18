from middleware import Middleware

class QueryTranslateMiddleware(Middleware):
	def translate(self, input_query):
		raise NotImplementedError('method translate for class QueryTranslateMiddleware not implemented')
