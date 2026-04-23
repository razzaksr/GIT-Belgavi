class Box:
    def __init__(self,val):
        self.data = val
        self.prev = self.next = None

class DList:
    def __init__(self):
        self.head = self.tail = None
        
    # CRUD Operations
    # Insertion At Beginning
    def addFront(self,val):
        box = Box(val)
        if not self.head: self.head = self.tail = box
        else:
            box.next = self.head
            self.head.prev = box
            self.head = box
        print(val,"inserted at beginning")
    # Insert at end
    def addRear(self,val):
        box = Box(val)
        if not self.tail: self.head = self.tail = box
        else:
            self.tail.next = box
            box.prev = self.tail
            self.tail = box
        print(val,"inserted at end")
    # Insertion at middle
    def addMid(self,val,pos):
        if pos == 0: self.addFront(val)
        else:
            explorer = self.head
            for _ in range(pos-1):
                if not explorer: 
                    raise IndexError("Invalid Position")
                explorer = explorer.next
            if explorer == self.tail: self.addRear(val)
            else:
                box = Box(val)
                box.next = explorer.next
                box.prev = explorer
                explorer.next.prev = box
                explorer.next = box
                print(val," inserted at",pos)
    # Read/ Traversal
    # head to tail
    def readHead(self):
        explorer = self.head
        while explorer:
            print(explorer.data)
            explorer = explorer.next
        else: print("Reached EnD")
    # tail to head
    def readTail(self):
        exp = self.tail
        while exp:
            print(exp.data)
            exp = exp.prev
        print("Reached None")
    # Update by position
    def update(self,**kwargs):
        pos = kwargs.get("pos")
        val = kwargs.get("val")
        if pos == 0: self.head.data = val
        else:
            explorer = self.head
            for _ in range(pos-1):
                if not explorer: 
                    raise IndexError("Invalid Position")
                explorer = explorer.next
            if explorer == self.tail: self.tail.data = val
            explorer.data = val
            print(val,"replced @",pos)
    # Deletion beginning
    def __neg__(self):
        if not self.head: print("Can't delete")
        elif self.head==self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("Deletion done @ beginning")      
    # Deletion end
    def __invert__(self):
        if not self.tail: print("Can't delete")
        elif self.head==self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print("Deletion done @ end")
    # Deletion by position
    def __or__(self,pos):
        if not self.head: print("can't delete");return
        if pos == 0: -self
        else:
            exp = self.head
            for _ in range(pos):
                if not exp: raise IndexError("InvalidPos")
                exp=exp.next
            if exp ==self.tail: ~self
            else:
                exp.prev.next = exp.next
                exp.next.prev = exp.prev
                print("Deletion done @",pos)
# Main
dub = DList();
dub|2
dub.addRear("Razak Mohamed");dub.addRear(34);
dub.addRear(5.4);dub.readHead()
dub|1
dub.readHead()
# -dub
# ~dub
