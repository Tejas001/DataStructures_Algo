from enum import Enum, unique, auto

# @unique
# class Fruits(Enum):

#     Apple = 1
#     Banana = 2
#     Guava = 3
#     Orange = 4
#     Pear = auto()
#     Grapes = auto()

class Person():

    def __init__(self) -> None:
        self.fname = 'fname'
        self.lname = 'lname'
        self.age = 27

    def __repr__(self):
        return "<Person Class - fname:{}, lname:{} and age:{}".format(self.fname, self.lname, self.age)
    
    def __str__(self) -> str:
        return "Person {} {} is {}".format(self.fname, self.lname, self.age)
    
class myColor:

    def __init__(self) -> None:
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self,attr) :
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError
        
    def __setattr__(self, attr, val) :
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr,val)

def main():

    # for fruit in Fruits:
    #     print(fruit.value)
    # print(type(Fruits.Apple))
    # print(repr(Fruits.Apple))

    # cls1 = Person()

    # print(repr(cls1))
    # print(str(cls1))

    cls1 = myColor()

    print(cls1.rgbcolor)
    print(cls1.hexcolor)    

    cls1.rgbcolor = (125, 100, 150)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

if __name__ == "__main__":
    main()

