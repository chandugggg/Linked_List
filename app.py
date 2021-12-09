class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linklist :
    def __init__(self):
        self.head = None
    
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def printlinklist(self):
        if self.head is None:
            print("list is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
        
linklist = Linklist()
firstNode = Node("Nibba gsk")
linklist.insert(firstNode)
# secondNode = Node("Bot gsk")
# linklist.insert(secondNode)
# thirdNode = Node("mg gsk")
# linklist.insert(thirdNode)
linklist.printlinklist()