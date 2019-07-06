class LinkedList:
    class Node:
        def __init__(self, value):
            self.val = value
            self.next = None

    def __init__(self):
        self.__head = None

    def add(self, value):
        if self.__head is None:
            self.__head = LinkedList.Node(value)
        else:
            p = self.__head
            while p.next != None:
                p = p.next
            p.next = LinkedList.Node(value)

    def __str__(self):
        out = ""
        if self.__head is None:
            return out
        else:
            p = self.__head
            while p.next != None:
                out += "%s -> " % p.val
                p = p.next
            out += str(p.val)
        return out

ll = LinkedList()
ll.add(1)
ll.add(2)
print(ll)

