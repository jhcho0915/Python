class Linked_List:

    class __Node:

        def __init__(self, val):
            # declare and initialize the private attributes
            # for objects of the Node class.
            # TODO replace pass with your implementation
            self.value = val
            self.next = None
            self.previous = None

    def __init__(self):
        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class
        # TODO replace pass with your implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.previous = self.__header
        self.__size = 0

    def __len__(self):
        # return the number of value-containing nodes in
        # this list.
        # TODO replace pass with your implementation
        return self.__size

    def append_element(self, val):
        # increase the size of the list by one, and add a
        # node containing val at the new tail position. this
        # is the only way to add items at the tail position.
        # TODO replace pass with your implementation
        new_node = Linked_List.__Node(val)
        new_node.next = self.__trailer
        new_node.previous = self.__trailer.previous
        new_node.previous.next = new_node
        self.__trailer.previous = new_node
        self.__size += 1


    def insert_element_at(self, val, index):
        # assuming the head position (not the header node)
        # is indexed 0, add a node containing val at the
        # specified index. If the index is not a valid
        # position within the list, raise an IndexError
        # exception. This method cannot be used to add an
        # item at the tail position.
        # TODO replace pass with your implementation
        if index >= (self.__size) or index < 0:
            raise IndexError
        new_node = Linked_List.__Node(val)
        if index > self.__size//2:
            current = self.__trailer
            for i in range(self.__size-1, index-1, -1):
                current = current.previous
            new_node.next = current
            new_node.previous = current.previous
            current.previous = new_node
            new_node.previous.next = new_node
            self.__size += 1
        else:
            current = self.__header
            for i in range(0, index):
                current = current.next
            new_node.next = current.next
            new_node.previous = current
            current.next = new_node
            new_node.next.previous = new_node
            self.__size += 1

    def remove_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, remove and return the value stored
        # in the node at the specified index. If the index
        # is invalid, raise an IndexError exception.
        # TODO replace pass with your implementation
        if index > (self.__size-1) or index < 0:
            raise IndexError
        if index > self.__size//2:
            current = self.__trailer
            for i in range(self.__size-1, index-1, -1):
                current = current.previous
            value = current.value
            current.previous.next = current.next
            current.next.previous = current.previous
            self.__size -= 1
        else:
            current = self.__header
            for i in range(0, index + 1):
                current = current.next
            value= current.value
            current.next.previous = current.previous
            current.previous.next = current.next
            self.__size -= 1
        return value
    def get_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, return the value stored in the node
        # at the specified index, but do not unlink it from
        # the list. If the specified index is invalid, raise
        # an IndexError exception.
        # TODO replace pass with your implementation
        if index > (self.__size-1) or index < 0:
            raise IndexError
        if index > self.__size//2:
            current = self.__trailer
            for i in range(self.__size-1, index-1, -1):
                current = current.previous
            return current.value
        else:
            current = self.__header
            for i in range(0, index + 1):
                current = current.next
            return current.value

    def rotate_left(self):
        # rotate the list left one position. Conceptual indices
        # should all decrease by one, except for the head, which
        # should become the tail. For example, if the list is
        # [ 5, 7, 9, -4 ], this method should alter it to
        # [ 7, 9, -4, 5 ]. This method should modify the list in
        # place and must not return a value.
        # TODO replace pass with your implementation.
        if self.__size == 0:
            return
        current = self.__header.next.value
        self.remove_element_at(0)
        self.append_element(current)


    def __str__(self):
        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.
        # TODO replace pass with your implementation
        if self.__size == 0:
            return '[ ]'
        final_string = '[ '
        current = self.__header.next
        while current is not self.__trailer:
            if current.next is self.__trailer:
                final_string = final_string + str(current.value) + ' ]'
            else:
                final_string = final_string + str(current.value) + ', '
            current = current.next
        return final_string

    def __iter__(self):
        # initialize a new attribute for walking through your list
        # TODO insert your initialization code before the return
        # statement. do not modify the return statement.
        self.__iter_node = self.__header.next
        return self

    def __next__(self):
        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more
        # values to fetch, raise a StopIteration exception.
        # TODO replace pass with your implementation
        if self.__iter_node == self.__trailer:
            raise StopIteration
        current = self.__iter_node
        self.__iter_node = self.__iter_node.next
        return current.value

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases
    # when the list is empty, when it has one element, and when
    # it has several elements. Do the indexed methods raise exceptions
    # when given invalid indices? Do they position items
    # correctly when given valid indices? Does the string
    # representation of your list conform to the specified format?
    # Does removing an element function correctly regardless of that
    # element's location? Does a for loop iterate through your list
    # from head to tail? Your writeup should explain why you chose the
    # test cases. Leave all test cases in your code when submitting.
    # TODO replace pass with your tests
    new1 = Linked_List()
    print(new1)
    new1.append_element(1)
    print(new1)
    new1.append_element(2)
    print(new1)
    new1.append_element(3)
    print(new1, ' has length ', len(new1))
    try:
        new1.insert_element_at(-1, 0)
        print(new1, ' has length ', len(new1))
        new1.insert_element_at(6, 4)
        print(new1, ' has length ', len(new1))
        new1.insert_element_at(8, 1)
        print(new1, ' has length ', len(new1))
        new1.insert_element_at(9, 4)
        print(new1, ' has length ', len(new1))
    except IndexError:
        print('Error: Unexpected no insert allowed')
    print(new1, ' has length ', len(new1))
    try:
        new1.insert_element_at(4, len(new1)+1)
    except IndexError:
        print('Correctly caught too large index error for insert')
    try:
        new1.insert_element_at(4, -1)
    except IndexError:
        print('Correctly caught negative index error for insert')
    print(new1, ' has length ', len(new1))

    new2 = Linked_List()
    new2.append_element(1)
    new2.append_element(2)
    new2.append_element(3)
    new2.append_element(4)
    new2.append_element(5)
    print(new2, ' has length ', len(new2))
    try:
        new2.remove_element_at(4)
        print(new2, ' has length ', len(new2))
        new2.remove_element_at(1)
        print(new2, ' has length ', len(new2))
        new2.remove_element_at(2)
        print(new2, ' has length ', len(new2))
        new2.remove_element_at(0)
        print(new2, ' has length ', len(new2))
    except IndexError:
        print('Error: Undexpected no remove allowed')
    print(new2, ' has length ', len(new2))
    try:
        new2.remove_element_at(len(new2))
    except IndexError:
        print('Correctly caught too large index error for removal')
    try:
        new2.remove_element_at(-1)
    except IndexError:
        print('Correctly caught negative index error for removal')
    print(new2, ' has length ', len(new2))

    new3 = Linked_List()
    new3.append_element(1)
    new3.append_element(2)
    new3.append_element(3)
    new3.append_element(4)
    new3.append_element(5)
    print(new3, ' has length ', len(new3))
    try:
        print(new3.get_element_at(0), len(new3))
        print(new3.get_element_at(4), len(new3))
        print(new3.get_element_at(2), len(new3))
        print(new3.get_element_at(3), len(new3))
    except IndexError:
        print('Error: Unexpected no get allowed')
    print(new3, ' has length ', len(new3))
    try:
        print(new3.get_element_at(len(new3)))
    except IndexError:
        print('Correctly caught too large index error for get')
    print(new3, ' has length ', len(new3))
    try:
        print(new3.get_element_at(-1))
    except IndexError:
        print('Correctly caught negative index error for get')
    print(new3, ' has length ', len(new3))

    new4 = Linked_List()
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))
    new4.append_element(1)
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))
    new4.append_element(2)
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))
    new4.append_element(3)
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))
    new4.append_element(4)
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))
    new4.append_element(5)
    print(new4, ' has length ', len(new4))
    new4.rotate_left()
    print(new4, 'has length ', len(new4))

    new5 = Linked_List()
    print(new5)
    for val in new5:
        print(val)
    new5.append_element(1)
    print(new5)
    for val in new5:
        print(val)
    new5.append_element(2)
    print(new5)
    for val in new5:
        print(val)
    new5.append_element(3)
    print(new5)
    for val in new5:
        print(val)
