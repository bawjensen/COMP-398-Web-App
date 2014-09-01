"""
Typical LinkedList class. Includes functionality for appending items, and populating
from a delimiter-separated list of strings. It also allows for a list of tuples, where
each element is sub-delimited by a different delimiter.
"""
class LinkedList():
	"""
	Node class for the LinkedList class. Allows for basic functionality of construction,
	getters, insertion, etc.
	"""
	class Node():
		"""
		Basic default constructor. Initializes with sentinel values.
		"""
		def __init__(self):
			self.cargo = None
			self.next = None

		"""
		Basic parameterized constructor. Initializes cargo with provided data.

		Parameters:
			newCargo: The item to insert.
		"""
		def __init__(self, newCargo):
			self.cargo = newCargo
			self.next = None


		"""
		Basic getter for the pointer to the next node in the list.
		"""
		def getNext(self):
			return self.next


		"""
		Basic getter for the cargo in the node.
		"""
		def getCargo(self):
			return self.cargo


		"""
		Inserts the data (or Node) after the given node.

		Parameters:
			newItem: The item to insert.
		"""
		def insertAfter(self, newItem):
			if type(newItem) == LinkedList.Node:
				self.next = newItem
			else:
				self.next = LinkedList.Node(newItem)


		"""
		Tests equality between the two provided nodes, by comparing the cargo contents of the two.

		Parameters:
			other: The other Node against which to compare the current Node.
		"""
		def __eq__(self, other):
			if other == None:
				return False
			return self.cargo == other.cargo


		"""
		Converts the Node into a string, using the cargo.
		"""
		def __str__(self):
			strBuffer = ""

			if type(self.cargo) == str:
				strBuffer += "\'"

			strBuffer += str(self.cargo)

			if type(self.cargo) == str:
				strBuffer += "\'"

			return strBuffer


	"""
	Basic default constructor. Initializes the data members with sentinel values.
	"""
	def __init__(self):
		self.head = None
		self.tail = None

	"""
	Tests if the list is empty.
	"""
	def isEmpty(self):
		return self.head == None

	"""
	Appends the given cargo/Node to the end of the LinekdList.

	Parameters:
		newCargo: The new Node, or cargo, which to append at the end of the list.
	"""
	def append(self, newCargo):
		if self.isEmpty():
			self.head = self.Node(newCargo)
			self.tail = self.head
		else:
			iterNode = self.head

			self.tail.insertAfter(newCargo)
			self.tail = self.tail.getNext()

	"""
	Tests for the presence of the provided item, and returns the index at which the item was
	found, or -1 if it wasn't.

	Parameters:
		item: The item to find in the list.
	"""
	def find(self, item):
		iterNode = self.head
		depth = 0

		while iterNode != None:
			if (type(item) == str and iterNode.getCargo() == item) or (type(item) == self.Node and iterNode == item):
				return depth

			iterNode = iterNode.getNext()
			depth += 1

		return -1

	"""
	Populates the LinkedList from the file represented by the filename, with items delimited by the
	provided string. Wipes any existing data before doing so.

	Parameters:
		fileName: The name of the file to load in.
		delimiter: The delimiter separating the items in the database file.
	"""
	def populate(self, fileName, delimiter):
		self.head = None

		fileString = open(fileName, "r").read()

		items = fileString.split(delimiter)

		for item in items:
			self.append(item)

	"""
	Populates the LinkedList from the file represented by the filename, with tuples delimited by the
	provided string, and the tuples sub-delimited. Wipes any existing data before doing so.

	Parameters:
		fileName: The name of the file to load in.
		delimiter1: The character that separates the tuples in the database file.
		delimiter2: The character that separates the items within the tuples.
	"""
	def populate_v2(self, fileName, delimiter1, delimiter2):
		self.head = None

		fileString = open(fileName, "r").read()

		items = fileString.split(delimiter1)

		for item in items:
			self.append(tuple(item.strip().split(delimiter2)))


	"""
	Returns the string representation of the LinkedList, showing the contents of the different Nodes
	in the linked list.
	"""
	def __str__(self):
		strBuffer = ""
		strBuffer += "LinkedList: "

		if self.isEmpty():
			strBuffer += "None."

		else:
			strBuffer += "["

			iterNode = self.head
			while iterNode.getNext() != None:
				strBuffer += str(iterNode) + ", "
				iterNode = iterNode.getNext()

			strBuffer += str(iterNode) + "]"


		return strBuffer


def main():
	pass

if __name__ == "__main__":
	main()