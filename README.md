[![Build Status](https://travis-ci.org/geekofalltrades/data-structures.png?branch=master)](https://travis-ci.org/geekofalltrades/data-structures)

Data Structures
------

#### These are various implementations of classic data structures in Python.

#####linked_list.py
A singly-linked list. Implements the LinkedList class for import.

#####stack.py
A stack. Implements the Stack class for import.

#####queue.py
A queue. Implements the Queue class for import.

#####hash_table.py
A hash table (something like Python's native dictionary). It uses a very naive
hashing algorithm which hashes based on the summed ordinal values of the characters
in the key. It handles collisions by binning key-value pairs that collide.
Its internal storage - and the storage of each bin - are implemented as
LinkedLists, using the LinkedList implemented in this repository. This largely
defeats the purpose of using a hashtable by removing constant-time lookup, but
it allows me to build on my previous work.

#####make_month.py
Implemented are make_month and DayLookup.
make_month is a factory function; it takes as arguments a month and a year.
It returns a DayLookup object which can be queried with a day of the given
month and reply with what day of the week that day is.

Hashing all the way, baby: given an integer day, the hashing algorithm
first determines a representation of that day as an integer between 0 and 6,
where 0-6 correspond to Mo-Su. It then plugs that integer into two separate
sixth-degree polynomials, which calculate the ordinal values for the two
characters representing the appropriate day code.

#####bst.py
A binary search tree. Implements the BST class for import. The tree does
not balance itself; the first value inserted will always remain the root.
Inserting sequentially increasing values can therefore cause the tree to
become quite unabalanced.

The tree now has four methods of traversal: in\_order, pre\_order, post\_order,
and breadth\_first. Each of these traversal methods returns a generator
that iterates over the values in the tree in the specified order.