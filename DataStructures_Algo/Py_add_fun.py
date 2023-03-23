class AddFunction:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

        self.myFunc()
        self.temp_change()

    def myFunc(self):
        """
        myFunc(arg1, arg2) --> It only prints the sum

        Parameters:
        arg1: First argument is to be numeric
        arg2: Second argument is to be numeric
        """
        myNums = [1, 2, 3, 4, 6]
        print(self.addition(self.arg1 + self.arg2))

        print(self.addition(*myNums))

    def temp_change(self):
        temp = [32, 65, 100, 50]

        print(list(map(self.FahrenheitToCelsius, temp)))

        # Using lambda func
        print(list(map(lambda t: (t - 32) * 5/9, temp)))

    @staticmethod
    def addition(*args):
        tmp = 0
        for arg in args:
            tmp += arg
        return tmp

    @staticmethod
    def FahrenheitToCelsius(temp):
        return (temp - 32) * 5/9

    def test():

        var1 = [1, 2, 3, 4]

        return var1


AddFunc1 = AddFunction(2, 2)
# print(AddFunc1.myFunc.__doc__)
