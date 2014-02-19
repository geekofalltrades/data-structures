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