import itertools

class BuiltIn_func:

    def __init__(self, list1, days, filename, chars, grades):
        self.list1 = list1
        self.days = days
        self.filename = filename
        self.chars = chars
        self.grades = grades

        self.utilities()
        self.iterator()
        self.transform_start()
        self.itertool_eg()

    def utilities(self):

        # use any() and all() to test sequences for boolean values
        print("To check any values in list : ",any(self.list1)) #True

        print("To check all values in list : ",all(self.list1)) #False because it contains zero

        print("To check minimum values in list : ",min(self.list1))
        print("To check maximum values in list : ",max(self.list1))
        print("To check sum of values in list : ",sum(self.list1))

    def iterator(self):

        # Using iterators like enumerators, zip, iter, next
        i = iter(self.days)
        print(next(i))
        print(next(i))
        print(next(i))

        # with open("test.txt", "r") as fp:
        #     for line in iter(fp.readline, ''):
        #         print(line)
        for d in range(len(self.days)):
            print(d+1, self.days[d])
        print()
        # enumerate
        for x,y in enumerate(self.days, start=1):
            print(x,y)

    @staticmethod
    def filter_func(x):
        if x%2 == 0:
            return False
        return True
    
    @staticmethod
    def filter_upper_lower(x):
        if x.isupper():
            return False
        return True
    
    @staticmethod
    def to_grades(x):
        if x >= 90:
            return 'A'
        elif (x >= 81 and x < 90):
            return 'B'
        elif (x >= 71 and x < 80):
            return 'C'
        elif (x >= 61 and x < 70):
            return 'D'
        elif (x >= 51 and x < 60):
            return 'E'
        return 'F'

    def transform_start(self):
        
        odds = list(filter(self.filter_func, self.list1))
        print(odds)

        upper_check = list(filter(self.filter_upper_lower, self.chars))
        print(upper_check)


        grade_check = list(map(self.to_grades, sorted(self.grades)))
        print(grade_check)

    def itertool_eg(self):
        # Cycle iterator
        cycle1 = itertools.cycle(self.days)
        print(next(cycle1))

        # Count itertor for Counter operation
        count1 = itertools.count(10, 10)
        print(next(count1))
        print(next(count1))
        print(next(count1))

        # accumulate iterator do accumulate sum from asc to desc order
        acc = itertools.accumulate(self.list1)
        print(list(acc))

        chain1 = itertools.chain('ABCD','1234')
        print(list(chain1))

        print(list(itertools.dropwhile(self.filter_upper_lower, self.chars)))
        print(list(itertools.takewhile(self.filter_upper_lower, self.chars)))


builtin_obj = BuiltIn_func(list1 = [1,2,3,4,0,9], days = ['sun','mon','tue','wed','thur','fri','sat'], \
                           filename = "test1.txt", chars = 'qishdekFBEHVNW', grades = [90,67,55,35,76,83] )

