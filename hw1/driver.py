import linkedlist

def main():
	ll = linkedlist.LinkedList()

	for i in xrange(50):
		ll.append("test")
	ll.append("hai")
	ll.append("test")

	ll.populate("db.txt", "\n")

	print ll


if __name__ == "__main__":
	main()