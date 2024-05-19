
class LinkedListNode(object):
  def __init__(self,value,next_node=None,prev_node=None):
    self.value = value
    self.next = next_node
    self.prev = prev_node

class LinkedList(object):
    def __init__(self,values=None):
       self.head = None
       self.tail = None
       if values is not None:
          self.multiple_add(values)
    
    def add(self,value):
      if self.head is None:
        self.tail = self.head =  LinkedListNode(value)
      else:  
        self.tail.next = LinkedListNode(value)
        self.tail = self.tail.next
      return self.tail

    def multiple_add(self,values):
       for value in values:
          self.add(value)



def loop_detection(ll):
   fast =slow = ll.head

   while (fast and fast.next):
      slow = slow.next
      fast = fast.next.next
      if fast is slow:
         break
    
   if ((fast is None) or (fast.next is None)):
      return None
   
   slow == ll.head

   while(fast is not slow):
      fast = fast.next
      slow = slow.next
   
   return fast

def is_palindrome(ll):
   fast = slow = None
   stack = []

   while (fast and fast.next):
      stack.append(slow.value)
      fast = fast.next.next
      slow = slow.next

   if fast:
      top = stack.pop()

      if (top != slow.value):
         return False
      
      slow = slow.next

   return True
      



def test():
    
    is_palindrome_test_cases = [
      ([1, 2], False),
      ([1, 2, 3, 4, 5], False),
      ([], True),
      ([1], True),
      (["a", "a"], True),
      ([1, 2, 3, 4, 3, 2, 1], True),
      ("aba", True)
      ]
    

    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    
    loop_detection_tests = [
        (looped_list, loop_start_node),
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
    ]

    '''
    for ll, expected in is_palindrome_test_cases:
        print(is_palindrome(ll) == expected)
    '''
    
    for ll, expected in loop_detection_tests:
        print(loop_detection(ll) == expected)
    

test()


       