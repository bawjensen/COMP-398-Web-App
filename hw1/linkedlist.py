class Node():
	def __init__(self):
		self.cargo = None
		self.next = None

	def __init__(self, newCargo):
		self.cargo = newCargo
		self.next = None

	def getNext(self):
		return self.next

	def getCargo(self):
		return self.cargo

	def insertAfter(self, newItem):
		if type(newItem) == str:
			self.next = Node(newItem)
		elif type(newItem) == Node:
			self.next = newItem

	def __eq__(self, other):
		if other == None:
			return False
		return self.cargo == other.cargo

	def __str__(self):
		strBuffer = ""

		if type(self.cargo) == str:
			strBuffer += "\'"

		strBuffer += self.cargo

		if type(self.cargo) == str:
			strBuffer += "\'"

		return strBuffer

class LinkedList():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def append(self, newCargo):
		if self.isEmpty():
			self.head = Node(newCargo)
		else:
			iterNode = self.head

			while iterNode.getNext() != None:
				iterNode = iterNode.getNext()

			iterNode.insertAfter(newCargo)

	def find(self, item):
		iterNode = self.head
		depth = 0

		while iterNode != None:
			if (type(item) == str and iterNode.getCargo() == item) or (type(item) == Node and iterNode == item):
				return depth

			iterNode = iterNode.getNext()
			depth += 1

		return -1

	def populate(self, fileName, delimiter):
		self.head = None

		fileString = open(fileName, "r").read()

		items = fileString.split(delimiter)

		for item in items:
			self.append(item)

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