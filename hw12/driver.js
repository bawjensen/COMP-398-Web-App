var LinkedList = require('./linkedlist').LinkedList;

function main() {
    var list = new LinkedList();

    list.populate('db.txt', '\n').then(function printIt() {
        console.log(list.toString());
    }).then(function findSomething() {
        console.log(list.find('Weaver of Lies'));
        console.log(list.search('Anowon, the Ruin Sage'));
    });
}

main();