class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def contains(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Create a new linked list to store the union
    union_list = LinkedList()

    # Traverse the first linked list and add its elements to the union list
    node = llist_1.head
    while node:
        union_list.append(node.value)
        node = node.next

    # Traverse the second linked list and add its elements to the union list
    node = llist_2.head
    while node:
        if not union_list.contains(node.value):
            union_list.append(node.value)
        node = node.next

    return union_list

def intersection(llist_1, llist_2):
    # Create a new linked list to store the intersection
    intersection_list = LinkedList()

    # Traverse the first linked list
    node = llist_1.head
    while node:
        # Check if the element is present in the second linked list
        if llist_2.contains(node.value):
            intersection_list.append(node.value)
        node = node.next

    return intersection_list

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Normal Case
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

elements_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
elements_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in elements_1:
    linked_list_1.append(i)

for i in elements_2:
    linked_list_2.append(i)

print("Test Case 1: Normal Case")
print("Union:", union(linked_list_1, linked_list_2))  # Expected output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11

# Test Case 2: Edge Case - Empty Lists
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

print("\nTest Case 2: Edge Case - Empty Lists")
print("Union:", union(linked_list_3, linked_list_4))  # Expected output: (empty)

# Test Case 3: Edge Case - One Empty List
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

elements_3 = [10, 20, 30]

for i in elements_3:
    linked_list_5.append(i)

print("\nTest Case 3: Edge Case - One Empty List")
print("Union:", union(linked_list_5, linked_list_6))  # Expected output: 10 -> 20 -> 30