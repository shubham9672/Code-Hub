class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        self._size += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        while(node.next != None):
            node = node.next
        node.next = Node(item)
        #print(self)

    def addHead(self, item):
        self._size += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        self.head = Node(item)
        self.head.next = node

    def search(self, item):
        node = self.head
        if self.isEmpty():
            return "Not Found"

        while node.next != None:
            if node.value == item:
                return "Found"
            node = node.next
        if node.value == item:
            return "Found"
        return "Not Found"

    def index(self, item):
        index = 0
        node = self.head
        if self.isEmpty():
            return -1
        
        if self.size() == 1:
            if node.value == item:
                return index

        while node.next != None :
            if node.value == item:
                return index
            node = node.next
            index += 1
        if node.value == item:
            return index
        return -1

    def size(self):
        return self._size

    def pop(self, pos):
        index = 0
        if pos >= self.size() or pos < 0:
            return "Out of Range"

        if pos == 0  and self.size() == 1:
            self.head = self.tail = None
        elif pos == 0:
            self.head.next.previous = None
            self.head = self.head.next
        else:
            node = self.head
            while index != pos - 1:
                index += 1
            node.next = node.next.next

        self._size -= 1
        return "Success"

if __name__ == "__main__":
    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size(), L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "PO":
            before = "{}".format(L)
            k = L.pop(int(i[3:]))
            print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    print("Linked List :", L)