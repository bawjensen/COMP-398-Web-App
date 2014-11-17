# URI's and corresponding verbs

/cards/&gt;id&lt;:
 + GET: Get the card object associated with the provided unique id
 + PUT: Add or update the card associated with the provided unique id
 + POST: Use the data contained in the headers to perform the given operation on the card associated with the provided unique id (more general than PUT, which just updates/creates)
 + DELETE: Deletes the card entry associated with the provided unique id
