module.exports = {
  LinkedList: LinkedList
}

var fs = require('fs');


/**
 * read takes in a file name (or path), and returns a Promise that will resolve with
 * the utf-8 encoded contents of the file
 * 
 * @param: fileName: The path to the file to be read in
*/
function read(fileName) {
  return new Promise(function promiseRead(resolve, reject) {
    fs.readFile(fileName, { encoding: 'utf8' }, function handleResponse(err, data) {
      if (err) { reject(Error(err)); }
      else { resolve(data); }
    });
  });
}

/**
 * Default constructor for the Node class
*/
function Node() {
  this.value = null;
  this.next = null;
}

/**
 * Parameterized constructor for the Node class
 * Takes in a value to store in this node
 * 
 * @param: newValue: The value to store
*/
function Node(newValue) {
  this.value = newValue;
  this.next = null;
}

/**
 * Default constructor for the LinkedList class
*/
function LinkedList() {
  this.head = null;
  this.tail = null;
}

/**
 * Append (or push) method for the LinkedList class
 * Takes one value to store in a new node, appended as the last element of the list
 * 
 * @param: newValue: The new value to append to the list
*/
LinkedList.prototype.append = function append(newValue) {
  if (this.head == null) {
    this.head = new Node(newValue);
    this.tail = this.head;
  }

  else {
    this.tail.next = new Node(newValue);
    this.tail = this.tail.next;
  }
}

/**
 * Copies the contents of an array into the LinkedList object
 * 
 * @param: arrayData: The array of data to copy over
*/
LinkedList.prototype.insertIntoList = function insertIntoList(arrayData) {
  for (var i in arrayData) {
    this.append(arrayData[i]);
  }
}

/**
 * Populates the LinkedList from the file provided by the fileName parameter.
 * The format of the given file is assumed to be a delimiter-separated list of strings.
 * 
 * @param: fileName: The name of the file to load in
 * @param: delimiter: The string that separates the values of the list, stored in the file
*/
LinkedList.prototype.populate = function populate(fileName, delimiter) {
  return read(fileName).then(function splitOnDelimiter(fileData) {
    return fileData.split(delimiter);
  }).then(this.insertIntoList.bind(this))
  .catch(function handleError(err) {
    console.error(err.stack);
    throw err;
  });
}

/**
 * Searches the LinkedList for a stored value, returning the index at which the value
 * was found. Returns -1 if not found.
 * 
 * @param: value: The value to find in the LinkedList
 * 
 * @return: The index at which the value was found. -1 if not.
*/
LinkedList.prototype.find = function find(value) {
  var index = 0;
  itNode = this.head;

  while (itNode != null) {
    if (itNode.value == value) {
      break;
    }

    ++index;
    itNode = itNode.next;
  }

  if (itNode == null) {
    index = -1;
  }

  return index;
}
LinkedList.prototype.search = LinkedList.prototype.find;

/**
 * Converts the LinkedList to a string format, similar to JSON. Useful for debugging output
 * when used with console.log().
 * 
 * @return: The string representation of the string.
*/
LinkedList.prototype.toString = function toString() {
  var itNode = this.head;

  var strBuffer = '';

  while (itNode != null) {
    if (typeof itNode.value == "string") {
      strBuffer += '"' + itNode.value + '"' + ', ';
    }
    else {
      strBuffer += itNode.value + ', ';
    }

    itNode = itNode.next;
  }

  return '[' + strBuffer.slice(0, -2) + ']';
}