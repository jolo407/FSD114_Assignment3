class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#def balance_check(s):
    #stack = []
    #for i in s:
      #  if s in parameter1
       #     stack.push()

def balance_check(s):
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0

if __name__=="__main__":
print(balance_check("{[({])]}"))
print(balance_check("{[({})]}"))



class Queue2Stacks:
    def __init__(self):
        #Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        #Fill out code here
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        #Fill out Code here
        

def test():
    """This should print: 0,1,2,3,4,
    Note: It will print vertically"""
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())





if __name__=="__main__":
    test()


