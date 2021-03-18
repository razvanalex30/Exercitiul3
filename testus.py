from parse_data import ParseData
print("""
Hello! Please choose one of the following three inputs:
1 - One random joke
2 - Ten random joke
3 - One/Ten random jokes by type
""")
while True:
    try:
        chosen_input = int(input("Enter your choice [1/2/3]: "))
        if chosen_input == 1:
            print("You have chosen One random joke!")
            ParseData.parse_data(chosen_input)
            break
        elif chosen_input == 2:
            print("You have chosen Ten random jokes!")
            ParseData.parse_data(chosen_input)
            break
        elif chosen_input == 3:
            types = ["general", "programming", "knock-knock"]
            numbers = [1, 10]
            type_value = None
            number = None
            while type_value not in types:
                type_value = str(input("Please choose a type [general|programming|knock-knock]: "))
                if type_value in types:
                    break
                else:
                    print("Invalid type! Please choose a correct value\n")
            print("Your type chosen was {}".format(type_value))
            while number not in numbers:
                number = int(input("Please choose the number of jokes [1/10]: "))
                if number in numbers:
                    break
                else:
                    print("Invalid! Please choose 1 or 10")
            ParseData.parse_data(chosen_input, type_value, number)
            break
        print("Please enter a valid number!\n")
    except Exception as e:
        print(e, "Please choose a valid input!\n")