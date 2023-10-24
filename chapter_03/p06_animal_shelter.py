import time

'''
An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head


    '''
    The insert method adds a new node at the end of a singly-linked list.
    If the list is empty, the new node becomes the head; otherwise, it's added after the last node.
    '''

    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        # it goes through the list until it reaches the last node.
        while current_node.next_node is not None:
            # effectively going to the next node.
            current_node = current_node.next_node
        # attaches the new node to the end of the list.
        current_node.next_node = node

    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            self.head = self.head.next_node
            return head_to_pop

        return None

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size


# Animal Definitions


class Animal:
    def __init__(self, name):
        self.time_admitted = time.time()
        self.name = name


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter(LinkedList):
    def enqueue(self, animal):
        animal_node = Node(animal)
        self.insert(animal_node)

    def dequeue_any(self):
        return super().pop_head()

    def dequeue_cat(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Cat):
                previous_node.next_node = current_node.next_node
                return current_node.data
            previous_node = current_node
            current_node = current_node.next_node
        return None

    def dequeue_dog(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Dog):
                previous_node.next_node = current_node.next_node
                return current_node.data
            previous_node = current_node
            current_node = current_node.next_node
        return None


def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert animal_shelter.size() == 3
