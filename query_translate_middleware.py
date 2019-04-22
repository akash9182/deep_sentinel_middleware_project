'''
This class represents a Middleware component that
takes in a query for some query language and outputs 
a query in some different query langauge
'''
class QueryTranslateMiddleware:
	def translate(self, input_query):
		raise NotImplementedError('method translate for class QueryTranslateMiddleware not implemented')