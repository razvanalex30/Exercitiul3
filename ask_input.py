class AskInput:
    """
    Class used for asking the user for inputs
    """
    choice = None
    chosen_number = None
    type = None
    odd_even = None

    @classmethod
    def ask_choice(cls):
        """
        Method used to retrieve the user's choice
        :return: The choice made by the user
        """
        print('''
        Hi, please choose one of the following options:
        1 - One random joke
        2 - Ten random jokes
        3 - One/Ten random jokes by type
        ''')
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
        """
        Method used to check whether the user wants odd/even or all the jokes
        """
        while True:
            try:
                print("Do you want to view only the odd/even jokes? Press Any other key to view them all")
                option = str(input("Your input: "))
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
        """
        Method used to select the type of jokes for option 3 (return jokes by type)
        """
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
        """
        Method used to return the number of jokes by type
        """
        numbers = ["1", "10"]
        nr = None
        while nr not in numbers:
            nr = str(input("Please choose the number of jokes [1/10]: "))
            if nr in numbers:
                cls.chosen_number = nr
                break
            else:
                print("Invalid! Please choose 1 or 10")
