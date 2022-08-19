class ArgNumError(Exception):
	"""Klasa reprezentjaca wyjatek niewlasciwej liczby argumentow."""

	def __init__(self, msg=None):
		self.msg = msg

	def __str__(self):
		if self.msg:
			return f'ArgNumError, {self.msg}'
		else:
			return 'ArgNumError, nieprawidlowa liczba argumentow'
