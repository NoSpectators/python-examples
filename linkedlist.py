#Node of a Singly Linked List
class Node:
    def __init__(self):
        self.data = None
	self.next = None
    def setData(self, data):
	self.data = data
    def getData(self):
	return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
 	return self.next != None
    def listLength(self):
        current = self.head
	count = 0
	while current != None:
	    count += 1
	    current = current.getNext()
	return count
singlelist=Node()
