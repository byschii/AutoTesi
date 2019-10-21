class Tesi(object):
	"""un piccolo appoggio per la gestione"""
	def __init__(self, laurea, titolo, pageLink, pdfLink):
		super(Tesi, self).__init__()
		self.laurea = laurea
		self.titolo = titolo
		self.pageLink = pageLink
		self.pdfLink = pdfLink
		