types = ["general","programming","knock-knock"]
numbers = ["1","10"]
typee = None
number = None
while typee not in types:
    typee = str(input("Please enter the type & the number: "))
    if typee in types:
        break
    else:
        print("Try again!")
print("Your choices are: {}".format(typee))