[![Build Status](https://travis-ci.org/geekofalltrades/data-structures.png?branch=master)](https://travis-ci.org/geekofalltrades/data-structures)

Data Structures
======

###### These are various implementations of classic data structures in Python.

linked_list.py
------
A singly-linked list. Implements the LinkedList class for import.

stack.py
------
A stack. Implements the Stack class for import.

queue.py
------
A queue. Implements the Queue class for import.

hash_table.py
------
A hash table (something like Python's native dictionary). It uses a very naive
hashing algorithm which hashes based on the summed ordinal values of the characters
in the key. It handles collisions by binning key-value pairs that collide.
Its internal storage - and the storage of each bin - are implemented as
LinkedLists, using the LinkedList implemented in this repository. This largely
defeats the purpose of using a hashtable by removing constant-time lookup, but
it allows me to build on my previous work.