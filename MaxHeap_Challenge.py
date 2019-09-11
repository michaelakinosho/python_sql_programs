class MaxHeap:
	def __init__(self):
		self.storage = []

	def myStr(self):
		print(self.storage)

	def insert(self, value):
		self.storage.append(value)
		self._bubble_up(len(self.storage)-1)

	def delete(self):
		if not self.storage:
			return None
		elif len(self.storage) == 1:
			return self.storage.pop()
		else:
			top = self.storage[0]
			self.storage[0] = self.storage.pop()
			self._sift_down(0)
			return top

	def _bubble_up(self, index):
		self.storage()

	def _sift_down(self, index):
		print("new testing")

myMaxHeap = MaxHeap()
myMaxHeap.insert(100)
myMaxHeap.insert(12)
myMaxHeap.myStr()
myMaxHeap.delete()
print(myMaxHeap.storage)
