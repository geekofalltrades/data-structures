Feature: LinkedList.insert()
    Add items to a LinkedList.

    Scenario: Add items to an empty LinkedList.
        Given a LinkedList X that is empty
        And value <to_add> to be added
        When I call X.insert(<to_add>)
        Then X's head node's value is <to_add> and next is None

    Examples:
        | to_add |
        | 3 |
        | '3' |
        | 3.3 |

    Scenario: Add items to a populated LinkedList.
        Given a LinkedList X with a head node with value <head_val>
        And value <to_add> to be added
        When I call X.insert(<to_add>)
        Then X's head node's value is <to_add> and next is a node with value <head_val>

    Examples:
        | head_val | to_add |
        | 3 | 4 |
        | '3' | '4' |
        | 3.3 | 4.4 |


Feature: LinkedList.pop()
    Pop items from the head of a LinkedList.

    Scenario: Pop from an empty LinkedList.

    Scenario: Pop from a LinkedList with one item.

    Scenario: Pop from a LinkedLIst with multiple items.


Feature: LinkedList.size()
    Return the number of items in a LinkedList.

    Scenario: Get the size of an empty LinkedList.

    Scenario: Get the size of a populated LinkedList.


Feature: LinkedList.search()
    Search a LinkedList for a node with a certain value.

    Scenario: Search a LinkedList for a value it contains.

    Scenario: Search a LinkedList for a value it does not contain.

Scenario: Search the list.
        Given a list X populated with <list_stuff>
        And a value <to_search>
        When I call X.search(<to_search>)
        Then I receive <returned_node>
        With value <node_value>

    Examples:
        | list_stuff | to_search  | returned_node | node_value |
        | 0     | 0       |
        | 1     | 1       |
        | 3     | Fizz    |
        | 5     | Buzz    |
        | 15    | FizzBuzz|


Feature: LinkedList.remove()
    Remove the first instance of an item from the LinkedList.

    Scenario: Remove an item from the LinkedList that is in the LinkedList.

    Scenario: Remove an item from the LinkedList that is not in the LinkedList.


Feature: LinkedList.__str__()
    Return a string representation of a LinkedList that looks like a
    Python tuple.

    Scenario: Print an empty LinkedList.

    Scenario: Print a LinkedList containing multiple values of different types.
