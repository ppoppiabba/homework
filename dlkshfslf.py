class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.Head = None
    def printList(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
myLinkedList = LinkedList()
myNode1=ListNode(10)
myNode2=ListNode(20)
myNode3=ListNode(30)
myNode4=ListNode(40)
myLinkedList.Head=myNode1
myNode1.next=myNode2
myNode2.next=myNode3
myNode3.next=myNode4
print("The elements in the linked list are:")
myLinkedList.printList()
