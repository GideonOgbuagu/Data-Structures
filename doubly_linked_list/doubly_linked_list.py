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
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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

    # def add_to_head(self, value):
    #     # pass
    #     # create instance of ListNode with value
    #     new_node = ListNode(value)
    #     # increment the DLL length attribute
    #     self.length += 1
    #     # if DLL is empty
    #     if self.length == 0:
    #         # set head and tail to the new node instance
    #         self.head = new_node
    #         self.tail = new_node

    #     # if DLL is not empty
    #     else:
    #         # set new node's next to current head
    #         new_node.next = self.head
    #         # set head's prev to new node
    #         self.head.prev = new_node
    #         # set head to the new node
    #         self.head = new_node
    def add_to_head(self, value):
        # $%$Start
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # $%$End

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    # def remove_from_head(self):
    #     # pass
    #     # return None if there is no head (i.e. the list is empty)
    #     if not self.head:
    #         return None
    #     # store the value of the head
    #     old_head = self.head
    #     # decrement the length of the DLL
    #     self.length -= 1
    #     # delete the head
    #     self.head = None
    #     # if head.next is not None
    #     if self.head.next == None:
    #         # set head.next's prev to None
    #         self.head.prev = None
    #         # set head to head.next
    #         self.head = old_head.next
    #         old_head.next = None

    #     elif self.head.next is None:
    #         # set head to None
    #         self.head = None
    #         # set tail to None
    #         self.tail = None

    #     return old_head

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

    def remove_from_head(self):
        # $%$Start
        value = self.head.value
        self.delete(self.head)
        return value
        # $%$End

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # pass
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

    # def remove_from_tail(self):
    #     #     pass
    #     # store the value of the tail
    #     removed = self.tail
    #     # decrement the length of the DLL
    #     self.length -= 1
    #     # delete the tail
    #     self.tail = None
    #     # if tail.prev is not None
    #     if self.tail.prev is not None:
    #         # set tail.prev's next to None
    #         self.tail.prev.next = None
    #         # set tail to tail.prev
    #         self.tail = removed.prev
    #     # else (if tail.prev is None)
    #     elif self.tail.prev is None:
    #         # set head to None
    #         self.head = None
    #         # set tail to None
    #         self.tail = None
    # # return the value
    #     return removed

        # if self.head == None:
        #     return None
        # removed = self.tail
        # if self.tail.prev is None:
        #     self.tail = removed.prev
        #     self.tail.next = None
        #     removed.prev = None
        # self.length -= 1
        # return removed

    def remove_from_tail(self):
        # $%$Start
        value = self.tail.value
        self.delete(self.tail)
        return value
        # $%$End

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # pass
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # pass
        if node is self.tail:
            return 
        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        
        if not self.head and not self.tail:
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # pass
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head
        # check to see if the current value is greater than the max_value
        while current:
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update thk to see if we're still at a valid list node
        
            # chece current node to the next node in the list
            current = current.next
        return max_value
