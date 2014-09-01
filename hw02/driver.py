import linkedlist

def main():
	ll = linkedlist.LinkedList() # Create the linked list

	ll.populate_v2("states.csv", "\r", ",") # Populate from the file

	print ll


if __name__ == "__main__":
	main()