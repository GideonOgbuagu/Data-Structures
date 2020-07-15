"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node

        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # pass
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # store the value of the head
        old_head = self.head
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        self.head = None
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to None
            self.head.prev = None
            # set head to head.next
            self.head = old_head.next
            old_head.next = None

        elif self.head.next is None:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        return old_head
        # if self.length == 0:
        #     return None
        # old_head = self.head
        # if self.head.next is None:
        #     self.head = None
        #     self.tail = None
        # else:
        #     self.head = old_head.next
        #     self.head.prev = None
        #     old_head.next = None

        # self.length -= 1
        # return old_head

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if not self.head:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node

        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        #     pass
        # store the value of the tail
        removed = self.tail
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        self.tail = None
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = removed.prev
        # else (if tail.prev is None)
        elif self.tail.prev is None:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
    # return the value
        return removed

        # if self.head == None:
        #     return None
        # removed = self.tail
        # if self.tail.prev is None:
        #     self.tail = removed.prev
        #     self.tail.next = None
        #     removed.prev = None
        # self.length -= 1
        # return removed

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # pass
        current = self.head
        while current.next:
            if current == node:
                node = self.head
                
            return current
        self.head.prev = current
        self.head = current
        current.prev = None
        current.next = self.head
        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if the current value is greater than the max_value
        if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.val
            # update thk to see if we're still at a valid list node
        while current:
            # chece current node to the next node in the list
            current = current.next
        return max_value
