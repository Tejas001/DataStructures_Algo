from collections import defaultdict
import collections
import string

class AdvancedColl:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.namedTuple()
        self.DefaultDict()
        self.Counter_demo()
        self.OrderDictEg()
        self.dequeCheck()

    def namedTuple(self):
        Point = collections.namedtuple("Point", "x y")
        p1 = Point(self.x, self.y)
        p2 = Point(10, 20)

        print(p1, p2)
        print(p1.x, p2.y)

        # Use _replace
        p1 = p1._replace(x = 100)
        print(p1) 

    def DefaultDict(self):

        self.fruits = ['apple', 'mango', 'apple', 'banana', 'banana']

        fruitCounter = defaultdict(int)

        for fruit in self.fruits:
            fruitCounter[fruit] += 1

        for x,y in fruitCounter.items():
            print(x + ": " + str(y))

    def Counter_demo(self):

        c1 = collections.Counter(self.fruits)

        print(c1['apple'])

        print(sum(c1.values()), " fruits in list")

        print(c1.most_common(1))

    def OrderDictEg(self):

        d1 = collections.OrderedDict({'a':1, 'b':2})
        d2 = collections.OrderedDict({'a':1, 'b':2})

        print('Equality check: ', d1==d2)

    def dequeCheck(self):

        d = collections.deque(string.ascii_lowercase)

        print("Item count: ",str(len(d)))

        for ele in d:
            print(ele.upper(), end=", ")

        d.rotate(3)

        print(d)


coll_obj = AdvancedColl(2, 3)