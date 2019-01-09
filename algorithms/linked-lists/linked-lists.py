# previous_node() | next_node() 
#  (singly linked list) [3]->[4]->[10]->[12]->[11] 
# Linked lists are composed of nodes and references / pointers pointing from one noe to the other
# The last node is pointing to NULL
# [] ->[] ->[] ->[] -> NULL (which suggests its the last node) 
# A single node contains a (reference/pointer) integer/double or custom object 
  # it contains a reference pointing to the next node in the linked list 
# Each node is composed of a data and reference link to the next node in the seq
# Can be used to implement stacks/queues 
# __getitem__ does not work in linked lists 

# Advantages
    # Linked lists are 'dynamic' data structures as opposed to fixed arrays 
    # Very efficient if we want to manipulate the first elements -< O(1) >-
    # Easy implementation
    # Can store items with different sizes: an array assumes every element to be exactly the same 
    # Its easier for a linked list to grow organically. An arrays size needs to be known ahead of time, or recreated
        # when it needs to grow

# Disadvantages
     Waste memory because of the references 
    # Nodes in a linked list must be read in order from the beginning as linked lists have sequential access
        (array items can be reached via indexes O(1) time!!)
    # Difficulties arise in linked lists when it comes to reverse traversing. 
     Singly linked lists are extremely difficult to navigate backwards. 
    # Solution: doubly linked lists -> easier to read, but memory is wasted in allocating space for a back pointer
    

# Linked List Operations 

# Insertion 
Inserting items at the beginning of the linked list: very simple, we just have to update the references -> O(1) time 
complexity. 
linkedList.insertAtStart(-5)
[4]->[10]-> NULL
[-5]->[4]->[10]-> NULL
Then set the pointer to point to the next node (-4)
-> this operation is really fast!

Fast insertion at end (Array)
Fast insertion at beginning (Linked List)

Inserting items at the end of the linked list: not that simple, you would have to traverse the whole linked list to find 
the last node (NULL)
+ You would have to update the references when you get to O(N) time complexity.

# Update 
linkedList.insertAtEnd(25) # It will search through the entire list to see where NULL is [10] -< makes it slow >- 
O(1) + O(N) = O(N)
update + search = linear search 

# No random access
# remove 
[12]->[4]->[123]->[10]->[25]->NULL
linkedList.removeStart() # O(1) 
linkedList.remove(10) # O(n), because it has to find(search) for 10 

# Problems with Linked Lists 
[12]->[4]->[123]->[10]->[25]->NULL

We can get from 4 to 25 because we have to hop to the next node But we cannot get go from 25 to 4 because
the references are in the opposite directions

Solution: 
    Doubly linked list -> Node class has two references, one pointing to the next node, one pointing to the 
    previous node.

[12]<-[4]<-[123]<-[10]<-[25]-NULL
[12]->[4]->[123]->[10]->[25]->NULL

This is memory intensive because you have to create so many references 
