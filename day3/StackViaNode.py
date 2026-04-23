from Doubly import Box
class Stk:
    def __init__(self):
        self.head = self.tail = None
    # CRUD Operations
    # Insertion At Beginning
    def __add__(self,val):
        box = Box(val)
        if not self.head: self.head = self.tail = box
        else:
            box.next = self.head
            self.head.prev = box
            self.head = box
        print(val,"pushed")
    # head to tail
    def readHead(self):
        explorer = self.head
        while explorer:
            print(explorer.data)
            explorer = explorer.next
        else: print("Reached EnD")
    # Deletion beginning
    def __neg__(self):
        if not self.head: print("Can't delete")
        elif self.head==self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("Popped")
stk = Stk()
stk+10;stk+"Razak";stk+False
stk.readHead()
-stk;-stk;
stk.readHead()
