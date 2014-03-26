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
become quite unabalanced. Credit is due to Cris Ewing for suggesting that
the left and right nodes of any given node should be handled as properties.

The tree now has four methods of traversal: in\_order, pre\_order, post\_order,
and breadth\_first. Each of these traversal methods returns a generator
that iterates over the values in the tree in the specified order. In creating
these functions, I conferred with [Mark Charyk](https://github.com/markcharyk) about how to create a recursive
generator.

Node deletion is now supported with the delete method, which takes as its
argument the value to be deleted. It returns the node object deleted, or
None if no node was deleted.

The BST now self-balances according to the AVL specification. Whenever a
value is inserted or deleted, the balance of all subtrees containing that
value are recursively checked, terminating at the root of the tree. If the
balance at any step is found to be above 1 or below -1, appropriate rotations
are performed to bring the tree back into balance.

#####Assorted Sorts
Implementations of various sorting algorithms. These functions were designed
with Python lists in mind, and make use of indexing, pop(), insert(), and
append(). In theory, any interable which implements direct access with
square bracket syntax and insert(), pop(), and append() methods that behave
as Python's list equivalents do should be sortable with these implementations.
######insertion_sort.py
Implements the insertion sort algorithm as insertion_sort. This function
takes a list as an argument and sorts it in place, returning None.
######merge_sort.py
Implements the merge sort algorithm as merge_sort. This function does not
sort in place, instead returning a sorted copy of the list originally
passed in.
######quicksort.py
Implements the quicksort algorithm as quicksort. This function does not
sort in place.
######radix_sort.py
Implements the radix\_sort algorithm. radix\_sort\_int is used on integers,
while radix\_sort\_str is used on strings. Does not sort in place, instead
returning a new copy of the list.