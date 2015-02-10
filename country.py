class Country:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Hello from {}.".format(self.name)


