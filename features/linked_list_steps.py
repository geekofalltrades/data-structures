from lettuce import step
from lettuce import world

from linked_list import LinkedList


#Checking an empty LinkedList:
@step('a LinkedList X that is empty')
def empty_list(step):
    world.linkedlist = LinkedList()


@step('And value (\w+) to be added')
def empty_list_value(step, value):
    world.value = value


@step("X's head node's value is (\w+) and next is None")
def empty_list_result(step, expected):
    assert world.linkedlist.head.value == expected, \
        "Got %s" % world.linkedlist.head.value
    assert world.linkedlist.head.next is None, \
        "Got %s" % world.linkedlist.head.next


#Checking a populated LinkedList:
@step('a LinkedList X with a head node with value (\w+)')
def populated_list(step, value):
    world.linkedlist = LinkedList()
    world.linkedlist.insert(value)


@step('And value (\w+) to be added')
def populated_list_value(step, value):
    world.value = value


@step("X's head node's value is (\w+) and next is a node with value (\w+)")
def populated_list_result(step, headval, nextval):
    assert world.linkedlist.head.value == headval, \
        "Got %s" % world.linkedlist.head.value
    assert world.linkedlist.head.next.value == nextval, \
        "Got %s" % world.linkedlist.head.next.value


@step('And value (\w+) to be added')
def generic_value(step, value):
    world.value = value


@step('I call X\.insert')
def call_add(step):
    world.linkedlist.insert(world.value)
