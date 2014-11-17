var fs          = require('fs'),
    MongoClient = require('mongodb').MongoClient;

function readFile(fileName) {
    console.log('Reading ' + fileName);
    return new Promise(function promiseRead(resolve, reject) {
        fs.readFile(fileName, function handleReadResponse(err, data) {
            if (err) { reject(Error(err)); }
            else { resolve(data); }
        });
    });
}

function resetDatabase() {
    console.log('Resetting database');
    return new Promise(function wipeDB(resolve, reject) {
        MongoClient.connect('mongodb://bawjensen:dummytest@ds049160.mongolab.com:49160/webapp', function handleResponse(err, db) {
            db.collection('hw14').remove({}, function handleWipeResponse(err) {
                if (err) { reject(); }
                else { resolve(); }
            });
        });
    });
}

function preprocessJSON(cardJsonData) {
    console.log('Preprocessing data');
    return Object.keys(cardJsonData).map(function eachCard(entry, i, array) {
        return cardJsonData[entry];
    });
}

function loadJSON() {
    return readFile('AllCards.json').then(JSON.parse).then(preprocessJSON);
}

function saveToDatabase(cardJsonData) {
    console.log('Read data, saving to database');
    return new Promise(function promiseSave(resolve, reject) {
        MongoClient.connect('mongodb://bawjensen:dummytest@ds049160.mongolab.com:49160/webapp', function handleResponse(err, db) {
            console.log('Opened connection to database, inserting');
            console.log(typeof cardJsonData[0]);
            db.collection('hw14').insert(cardJsonData, function handleWipeResponse(err) {
                if (err) { reject(Error(err)); }
                else { resolve(); }
            });
        });
    }).catch(function handlePromiseError(err) {
        console.error(err);
        throw err;
    });
}

function runEverything() {
    resetDatabase()
        .then(loadJSON)
        .then(saveToDatabase)
        .then(function manuallyExit() {
            console.log('Done');
            process.exit(0);
        })
        .catch(function handlePromiseError(err) {
            console.error(err.stack);
            throw err;
        });
}

runEverything();