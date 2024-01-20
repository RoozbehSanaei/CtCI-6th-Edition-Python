from chapter_02.linked_list import LinkedList


'''
The delete_middle_node function deletes a node from a singly linked list assuming the node to be deleted is not the last one in the list.
The process involves two steps: 
    replacing the current node's value with the next node's value, 
    and then setting the current node's next pointer to skip the next node, 
    effectively removing it from the list.
'''

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)
