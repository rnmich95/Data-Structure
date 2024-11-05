class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data, index=0):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        if index == 0:
            new_node.next  = self.head
            # the newly created node is made the head of the list
            self.head = new_node
            return
        
        current = self.head
        target_index = 0
        while target_index < index:

            previous  = current
            following = current.next

            target_index += 1
            current = following
        
        previous.next = new_node
        new_node.next = following

    def replace(self, data, index):
        new_node = Node(data)

        if index == 0:
            following = self.head.next

            self.head.next = new_node
            new_node.next  = following 

            self.head = new_node
            return

        current = self.head
        target_index = 0
        while target_index < index:

            previous   = current
            to_replace = current.next
            target_index += 1

            current = current.next
        
        previous.next = new_node
        new_node.next = to_replace.next

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        target_index = 0
        while target_index < index:
            previous = current
            to_exclude = current.next

            target_index += 1
            current = current.next

        previous.next = to_exclude.next 

    def find(self, data):
        current = self.head
        i = 0
        while current:
            if current.data == data:
                return i

            current = current.next
            i +=1
        
        return -1

    def value(self, index):
        current = self.head
        target_index = 0

        while target_index < index:
            target_index += 1
            current = current.next
        
        return current.data 
    
    def length(self):
        current = self.head
        length  = 0

        while current:
            length += 1
            current = current.next

        return length

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


import unittest
class LinkedListTestCase(unittest.TestCase):
    def test_insert(self):
        case = LinkedList()

        case.insert('A')
        self.assertEqual(case.value(0), 'A')

        case.insert('B', 1)
        case.insert('C', 2)
        
        self.assertEqual(case.value(2), 'C')

    def test_replace(self):
        case = LinkedList()

        case.insert('A')
        case.insert('B', 1)
        case.insert('C', 2)

        case.replace('D', 0)
        self.assertEqual(case.value(0), 'D')

        case.replace('E', 2)
        self.assertEqual(case.value(2), 'E')

    def test_delete(self):
        case = LinkedList()

        case.insert('A')
        case.insert('B', 1)
        case.insert('C', 2)

        case.delete(2)

        with self.assertRaises(AttributeError):
            case.value(2)

        l = case.length()

        self.assertEqual(l, 2)

    def test_find(self):
        case = LinkedList()

        case.insert('A')
        case.insert('B', 1)
        case.insert('C', 2)

        self.assertEqual(case.find('H'), -1)
        self.assertEqual(case.find('A'), 0)        


if __name__ == '__main__':
    unittest.main()
