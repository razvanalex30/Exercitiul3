print("Hi! Please choose 1 of these 3 inputs")
print("1 - Random joke, 2 - 10 Random jokes, 3 - Random jokes by type")
while True:
  try:
    inputus = int(input("Enter your choice: "))
    if inputus == 1:
        print("You have chosen a random joke!")
        break
    elif inputus == 2:
        print("You have chosen 10 Random Jokes!")
        break
    elif inputus == 3:
        types = ["general","programming","knock-knock"]
        numbers = [1, 10]
        typee = None
        number = None
        while typee not in types:
            typee = str(input("Please choose a type: "))
            if typee in types:
                break
            else:
                print("Try again!")
        print("Your type chosen was {}".format(typee))
        while number not in numbers:
            number = int(input("Please choose the number of jokes: "))
            if number in numbers:
                break
            else:
                print("Try again!")
        print("Here are your jokes!")
        break

    print("Please enter a valid number!\n")
  except Exception:
        print("Please choose a valid input\n")