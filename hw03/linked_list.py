class Node(object):
	"""Stores a single database entry.

	Represents a database entry within a linked list. Specified to 
	store a name and abbreviation of a USA Territory as cargo.

	Attributes:
       name = the name of the state
       abbreviation = the postal abbreviation
       next = the next node object in the linked list
	"""	

	def __init__(self, name, abb, next=None):
		"""Initializes Node class with territory name and postal abbreviation."""

		self.name = name
		self.abbreviation = abb
		self.next = next

	def print_node(self):
		"""Displays cargo of a Node object.

		Args:
			None

		Returns:
			None
		"""

		print "--------------------------"
		print "State/Territory: " + self.name
		print "Abbreviation: " + self.abbreviation.rstrip()
		print "--------------------------"

class LinkedList(object):
	"""Stores an entire flat file database in the form of Node objects.

	Uses Node objects to store a flat file database. Specified to store
	the flat file database containing USA Territory names and abbreviations.

	Attributes:
		size = the number of entries within the Linked List
		head = the first entry (Node object) in the Linked List
	"""

	def __init__(self):
		"""Initializes LinkedList class by setting the size as 0 and the head Node to None."""

		self.size = 0
		self.head = None

	def append(self, territory_name, territory_abb):
		"""Appends a new Node object to the end of the Linked List instance.

		Creates a new instance of the Node class and inserts it at the very end
		of the Linked List instance.

		Args:
			territory_name = the name of the territory/state
			territory_abb = the postal abbreviation of the territory/state

		Returns:
			None
		"""

		new_node = Node(territory_name, territory_abb)

		if(self.head == None):
			self.head = new_node
		else:
			temp_node = self.head

			while(temp_node.next != None):
				temp_node = temp_node.next

			temp_node.next = new_node

	def search(self, query):
		"""Searches for a specific query in the linked list

		Iterates through the entries in the linked list for a specific query.
		Prints out the entry if it is found.

		Args:
			query = the name of the state/territory that is being searched for

		Returns:
			A Boolean, True  - the search item was found
					   False - the search item was not found
		"""

		temp_node = self.head
		while(temp_node != None):
			if(temp_node.name == query):
				print query + " found!"
				temp_node.print_node()
				return True
			temp_node = temp_node.next

		print query + " NOT found!"
		return False


	def populate(self, file_name):
		"""Populates an empty linked list with a flat file database

		Only populates an empty linked list.

		Args:
			file_name = the name of the file that is to be read into the linked list

		Returns:
			A Boolean, True  - the search item was found
					   False - the search item was not found
		"""

		if(self.head != None):
			print "This Linked List is already populated. Please try again with an empty list."
		else:
			fin = open(file_name, "r")
			for entry in fin:
				temp_data = entry.split(",")
				self.append(temp_data[0], temp_data[1])

			fin.close()

	def display(self):
		"""Displays each entry within the linked list 

		Args:
			None

		Returns:
			None
		"""

		if(self.head == None):
			print "\n\n--------------------------"
			print "This Linked List is empty."
			print "--------------------------\n\n"
		else:
			temp_node = self.head
			while(temp_node != None):
				temp_node.print_node();
				temp_node = temp_node.next

