# State Abbreviation

import linked_list

def main():
	file_name = "territories.csv"

	flat_file = linked_list.LinkedList()

	# ---------- Shows functionality for the POPULATE and DISPLAY functions -----------------------------

	print "\nTesting the Display function on the empty list..."
	flat_file.display() 

	print "\nTesting the Populate function on the empty list from the flat file database 'territories.csv'..."
	flat_file.populate(file_name)

	print "\nTesting the Display function on the populated list..."
	flat_file.display()

	# ---------------------------------------------------------------------------------------------------

	# ---------- Shows functionality for the SEARCH function -----------------------------

	print "\nTesting the Search function on 'Massachusetts'..."
	flat_file.search("Massachusetts")

	print "\nTesting the Search function on 'California'..."
	flat_file.search("California")

	print "\nTesting the Search function on 'Arizona'..."
	flat_file.search("Arizona")

	print "\nTesting the Search function on 'Guam'..."
	flat_file.search("Guam")

	print "\nTesting the Search function on 'Whale Lab'..."
	flat_file.search("Whale Lab")

	# ---------------------------------------------------------------------------------------------------

	# ---------- Shows functionality for the APPEND function -----------------------------

	print "\nTesting the Append function by adding the Whale Lab to the list"

	print "Adding 'Whale Lab' as a USA Territory..."

	# line taken from original flat file database
	flat_file.append("Whale Lab", "WHL")

	print "\nTesting the Search function on 'Whale Lab'..."
	flat_file.search("Whale Lab")

	# -------------------------------------------------
if __name__ == '__main__':
	main()