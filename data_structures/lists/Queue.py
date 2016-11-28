
class Queue(object):

    class node(object):
        def __init__(self, data):
            self.data = data
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "Queue(head->[])"

        if self.head == self.tail:
            return "Queue(head->[{}])".format(self.head.data)

        chars = ["Queue(head->[{}".format(self.head.data)]
        curr = self.head.prev
        while curr != self.tail:
            chars.append(str(curr.data))
            curr = curr.prev
        chars.append("{}])".format(self.tail.data))
        return ", ".join(chars)

    def top(self):
        return self.head.data

    def push(self, item):
        # print 'enquing item'
        new = self.node(item)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.prev = new
            self.tail = new
        self.size += 1

    def pop(self):
        # print 'popping item off queue'
        if self.head is None:
            return None

        ret = self.head.data
        self.head = self.head.prev
        self.size -= 1
        return ret

    def delete(self, item):
        if item == self.head.data:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.prev
            self.size -= 1 
            return True

        prv = self.head
        curr = self.head.prev
        while curr is not None:
            if item == curr.data:
                prv.prev = curr.prev
                if curr == self.tail:
                    self.tail = prv
                self.size -= 1
                return True
            prv = curr
            curr = curr.prev
        return False

    def empty(self):
        return self.size == 0

