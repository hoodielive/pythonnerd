# create class for Node
class Node(object):
    def __init__(self, data):
        self.data = data
        # make reference to next node (pointer)
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        # first node in linked list - root node of the tree (head)
        self.head = None
        self.size = 0

    # O(1) - insert data at the beginning of list  
    def insertStart(self, data):
        self.size = self.size + 1 # increment the size
        newNode = Node(data) # instantiate a new node object

        # if the head is Null, then it becomes the new node, root or head
        if not self.head:
            self.head = newNode
        else:
            # or if the head is there, then newNode is the head of the linked list
            newNode.nextNode = self.head
            # pointer - reference - head
            self.head = newNode

    # Remove - remove the specified instance and change the pointer/reference
    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    # O(1)
    def size(self):
        return self.size

    # O(n) - calculate how many items are stored in the linked list
    def size2(self):
        actualNode = self.head
        size = 0

        # if the size is Null then increment by 1 
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    # O(n) 
    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode
