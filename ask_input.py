# from parse_data import ParseData

class AskInput:
    choice = None
    chosen_number = None
    type = None
    odd_even = None

    @classmethod
    def ask_choice(cls):
        while True:
            try:
                chosen_input = int(input("Enter your choice [1/2/3]: "))
                if chosen_input == 1:
                    cls.choice = chosen_input
                    break
                elif chosen_input == 2:
                    cls.choice = chosen_input
                    break
                elif chosen_input == 3:
                    cls.choice = chosen_input
                    types = ["general", "programming", "knock-knock"]
                    numbers = [1, 10]
                    type_value = None
                    nr = None
                    while type_value not in types:
                        type_value = str(input("Please choose a type [general|programming|knock-knock]: "))
                        if type_value in types:
                            cls.type = type_value
                            break
                        else:
                            print("Invalid type! Please choose a correct value\n")
                    while nr not in numbers:
                        nr = int(input("Please choose the number of jokes [1/10]: "))
                        if nr in numbers:
                            cls.chosen_number = nr
                            break
                        else:
                            print("Invalid! Please choose 1 or 10")
                    break
                print("Please enter a valid number!\n")
            except Exception as e:
                print(e, "Please choose a valid input!\n")

    @classmethod
    def ask_even_odd(cls):
        while True:
            try:
                option = str(input("Do you want to view only the odd/even jokes? "))
                if option == "odd":
                    cls.odd_even = option
                    break
                elif option == "even":
                    cls.odd_even = option
                    break
                else:
                    cls.odd_even = None
                    break
            except Exception as e:
                print(e, "Please choose a valid input!\n")
