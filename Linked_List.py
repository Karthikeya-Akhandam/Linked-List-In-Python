class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data,data1=None):
        nn = Node(data)
        if data1 == None:
            if not self.head:
                self.head = nn
            else:
                self.head.next = nn
        elif data1 == "beginning":
            if not self.head:
                self.head = nn
            else:
                nn.next = self.head
                self.head = nn
    
        else:
            ptr = self.head
            while ptr and ptr.val != data1:
                ptr = ptr.next
            if ptr:
                nn.next = ptr.next
                ptr.next = nn
            else:
                print(f"Node with value {data1} not found.")
            
    def delete(self,data):
        ptr = self.head
        pptr = None
        while ptr and ptr.val != data:
            if ptr:
                pptr = ptr
                ptr = ptr.next
            else:
                print(f"Node with value {data} not found.")
        if ptr == self.head:
            self.head = ptr.next
            del(ptr)
        elif ptr.next == None:
            pptr.next = None
            del(ptr)
        else:
            pptr.next = ptr.next
            del(ptr)
        ptr = None
        pptr = None
                
    def printlist(self):
        ptr = self.head
        while ptr:
            print(ptr.val, "->", end=" ")
            ptr = ptr.next
        print("End")

if __name__ == "__main__":
    l = LinkedList()
    l.append(5)
    l.printlist()
    l.append(10,5)
    l.printlist()
    l.append(12,5)
    l.printlist()
    l.delete(12)
    l.printlist()
    l.delete(5)
    l.printlist()
    l.append(5,"beginning")
    l.printlist()
    l.append(12,5)
    l.printlist()