class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): 
                self.insert(item)


    def __iter__(self):

        def val_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return val_generator()

    def __str__(self):

        output = ""

        for value in self:
            output += f"[ {value} ] -> "

        return output + "None"

    def __len__(self):
      
        return len(list(iter(self)))

    def __eq__(self, other):
    
        return list(self) == list(other)

    def __getitem__(self, idx):


    
        if idx < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == idx:
                return item

        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    
    def gen():
        i = 0
        while True:
            yield i
            i += 1


    num_gtr = gen()

    for i in range(50):
        print(next(num_gtr))    




if __name__ == "__main__":

    food = LinkedList()
    food.insert("apple")
    food.insert("banana")

    num=LinkedList()
    num.insert(3)
    num.insert(2)
    num.insert(1)


    print (food.__str__())
    print (num.__str__())


   

    
