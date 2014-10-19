import linkedlist

def main():
	# Create empty list
	ll = linkedlist.LinkedList()

	# Test append
	ll.append("test")

	# Populate from flat-file database
	ll.populate("db.txt", "\n")

	# Test stdout output
	print ll

	# Test search functionality
	print ll.find("Zuran Enchanter")


if __name__ == "__main__":
	main()