class ArrayStack: 
	"""LIFO Stack Implementation using a Python list as underlying storage."""

	def __init__(self):
		"""Create an empty stack."""
		self._data = []

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if stack is empty."""
		return len(self._data) == 0

	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)

	def top(self):
		"""Return (but do not remove) the element at the top of the stack."""

		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]
