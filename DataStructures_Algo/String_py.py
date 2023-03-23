from string import Template

def main():

    str1 = "This is {} formatting method used in {}".format('first','python')
    print(str1)

    temp1 = Template("This is ${num} formatting method used in ${pl}")
    str2 = temp1.substitute(num='second', pl='python')
    print(str2)

    data = {
        'num':'third',
        'pl':'python'
    }

    str3 = temp1.substitute(data)
    print(str3)

if __name__ == "__main__":
    main()
    