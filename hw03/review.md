# Bryan Jensen Reviewing Devin Delfino's Code

## Style Guide Evaluation

(Note: Only listing places where the style guide was NOT followed)
+ Goes slightly over maximum line length, but not often and not severely.
+ Style guide suggests minimal usage of parentheses, but there are instances of unnecessary parentheses around the boolean clause of if and while statements. This, however, does *not* harm the readability of the code.
+ No in-line comments. For the most part, the code is self-explanatory, but there are occurrences of non-obvious choices, such as choosing to do an '.rstrip()' method call before outputting the contents of a Node object. (Very minor improvement)

## Code Evaluation

(I was about as harsh as I could be in this section. Overall, the code is great, and well written for such a tiny, one-off project.)
+ Node class, print_node method: Doesn't do error checking before calling rstrip() on a potentially NoneType object. 
+ Even though the assignment consisted of specializing our LinkedList class for the given data set, there are ''better'' ways of doing so than heavily adapting the code to handle this specific circumstance. One such way could be to keep the highly generalized methods of a generic LinkedList class, and simply utilize them in specialized methods, which would actually be used in the main function.
+ Instantiates self.size of the LinkedList, but never makes use of it.
+ Assumes (not unreasonably) proper use of methods, such as never being called with a NoneType object.
+ Has print statements in code, where they may not be necessary or expected (such as LinkedList's search method).
+ LinkedList uses open() and close() on a file, instead of using the with `open(x, 'r') as fin:` syntax. Only bad because it relies on the programmer to remember and keep the close() method call.
+ I would provide a default constructor for the Node class. However, may be unnecessary as it is implicitly not publicly accessible.
+ Personal preference: I would overload the __str__ operator method, and not create a new method called 'display' or 'print_node', for simple text output of an object.