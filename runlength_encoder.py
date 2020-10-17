class Rle:
	"""
	Calls a callback with (num items, value) for each runlength encoded chunk.
	The handle function returns the amount of items that have been processed.
	If the end of the sequence is reached, it will return 0.
	"""
	def __init__(self, callback, initial_value=0):
		self.callback = callback
		self.current_value = initial_value

	def handle(self, values):
		pos = 0
		while True:
			try:
				new_pos, value = next(
					(i, v) for i,v in enumerate(values[pos:], pos)
					if v != self.current_value)
				self.callback(new_pos - pos, self.current_value)
				self.current_value = value
				pos = new_pos
			except StopIteration:
				return pos
