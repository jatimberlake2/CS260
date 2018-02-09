class Node(object):
	"""Represents a singly linked node."""
	def __init__(self, data, next = None):
		"""Instantiates a Node with a default next of None."""
		self.data = data
		self.next = next
	def __str__(self):
		"""-> The string representation of the array."""
		return str(self.data)

