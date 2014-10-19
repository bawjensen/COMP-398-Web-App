import linkedlist

def main():
	# Create the linked list
	ll = linkedlist.LinkedList()

	# Populate from the file
	ll.populate_v2("states.csv", "\r", ",")

	# Test printing
	print ll.find(('ALABAMA', 'AL'))

	# Test printing
	print ll


if __name__ == "__main__":
	main()