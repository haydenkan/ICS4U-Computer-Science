class NODE:
    def __init__(self, VALUE, PREV = None, NEXT = None):
        self.VALUE = VALUE
        self.PREV = PREV
        self.NEXT = NEXT

class LINKED_LIST:
    def __init__(self):
        self.HEAD = None

    def ADD_ELEMENT(self, VALUE):
        NEW_NODE = NODE(VALUE)
        if self.HEAD == None:
            self.HEAD = NEW_NODE
            return
        while self.HEAD.NEXT != None:
            self.HEAD = self.HEAD.NEXT
        self.HEAD.NEXT = NEW_NODE
        NEW_NODE.PREV = self.HEAD

    def PRINT(self, NODE):
        NODE = NODE.PREV
        while NODE != None:
            print(NODE.VALUE)
            NODE = NODE.NEXT

l = LINKED_LIST()
l.ADD_ELEMENT(12)
l.ADD_ELEMENT(13)
l.ADD_ELEMENT(14)
l.PRINT(l.HEAD)