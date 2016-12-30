import sys
class ListNode:
    def __init__(self, data, next):
	self.data = data
	self.next = next

class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, node, data):
	new_node = ListNode(data, node.next)
	node.next = new_node
        if self.tail == node:
	    self.tail = new_node
    def insert_end(self, data):
	if self.tail is None:
	    new_node = ListNode(data, None)
	    self.head = self.tail = new_node
	else:
	    self.insert(self.tail, data)
    def insert_beginning(self, data):
	new_node = ListNode(data, self.head)
	self.head = new_node
    def remove_after(self, node):
	node.next = node.next.next
	if node.next is None:
	    self.tail = node
    def remove_beginning(self):
	self.head = self.head.next
	if self.head is None:
	    self.tail = None
    def iterate(self, func):
	node = list.head
	while node is not None:
	    func(node.data)
            node = node.next
    def find_first(self, data):
	node = list.head
	while node is not None:
	    if node.data == data:
		return node
	    node = node.next
    def find_first_func(self, func):
	node = list.head
	while node is not None:
	    if func(node.data):
		return node
	    node = node.next

list = List()
for x in range(1,10):
    list.insert_end(x)

node = list.head
while node is not None:
    print node.data
    node = node.next
print ""

 
