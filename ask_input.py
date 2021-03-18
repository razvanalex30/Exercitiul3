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
                    AskInput.ask_even_odd()
                    break
                elif chosen_input == 3:
                    cls.choice = chosen_input
                    AskInput.ask_type_jokes()
                    AskInput.ask_number_jokes()
                    if cls.chosen_number == "10":
                        AskInput.ask_even_odd()
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

    @classmethod
    def ask_type_jokes(cls):
        types = ["general", "programming", "knock-knock"]
        type_value = None
        while type_value not in types:
            type_value = str(input("Please choose a type [general|programming|knock-knock]: "))
            if type_value in types:
                cls.type = type_value
                break
            else:
                print("Invalid type! Please choose a correct value\n")

    @classmethod
    def ask_number_jokes(cls):
        numbers = ["1", "10"]
        nr = None
        while nr not in numbers:
            nr = str(input("Please choose the number of jokes [1/10]: "))
            if nr in numbers:
                cls.chosen_number = nr
                break
            else:
                print("Invalid! Please choose 1 or 10")