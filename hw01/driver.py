import linkedlist

def main():
	ll = linkedlist.LinkedList()

	for i in xrange(50):
		ll.append("test")
	ll.append("hai")
	ll.append("test")

	ll.populate("db.txt", "\n")

	print ll

	print ll.find("Zuran Enchanter")


if __name__ == "__main__":
	main()