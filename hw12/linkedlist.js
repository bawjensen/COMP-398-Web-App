var fs = require('fs');

function read(fileName) {
    return new Promise(function promiseRead(resolve, reject) {
        fs.readFile(fileName, { encoding: 'utf8' }, function handleResponse(err, data) {
            if (err) { reject(Error(err)); }
            else { resolve(data); }
        });
    });
}

function Node() {
    this.value = null;
    this.next = null;
}

function Node(newValue) {
    this.value = newValue;
    this.next = null;
}

function LinkedList() {
    this.head = null;
    this.tail = null;
}

LinkedList.prototype.append = function append(newNode) {
    if (this.head == null) {
        this.head = new Node(newNode);
        this.tail = this.head;
    }

    else {
        this.tail.next = new Node(newNode);
        this.tail = this.tail.next;
    }
}

LinkedList.prototype.insertIntoList = function insertIntoList(arrayData) {
    // console.log(this);
    for (var i in arrayData) {
        // console.log(this);
        this.append(arrayData[i]);
    }
}

LinkedList.prototype.populate = function populate(fileName, delimiter) {
    return read(fileName).then(function splitOnDelimiter(fileData) {
        return fileData.split(delimiter);
    }).then(this.insertIntoList.bind(this))
    .catch(function handleError(err) {
        console.error(err.stack);
        throw err;
    });
}

LinkedList.prototype.toString = function toString() {
    var itNode = this.head;

    while (itNode != null) {
        process.stdout.write(itNode.value + ', ');
        itNode = itNode.next;
    }
}

function main() {
    var list = new LinkedList();

    list.populate('db.txt', '\n').then(function printIt() {
        console.log(list.toString());
    });
}

main();