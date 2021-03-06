class Utils:
    """
    Class used to store the methods regarding data parsing
    """

    @classmethod
    def get_formatted_data(cls, retrieved_data):
        """
        Method used to return the jokes in an easy to read format
        :param retrieved_data: the list or the dictionary
        :return: the jokes
        """
        if isinstance(retrieved_data, list):
            try:
                for elem in retrieved_data:
                    print(f'''
                    id = {elem['id']} ; 
                    type = {elem['type']} ;
                    setup: {elem['setup']}
                    punchline: {elem['punchline']}
                    ''')
            except KeyError as e:
                print(e, "There was an error!\n")
            except ValueError as e:
                print(e, "VALUE ERROR!\n")
            else:
                return ""
        elif isinstance(retrieved_data, dict):
            try:
                return f'''
                id = {retrieved_data['id']} ;
                type = {retrieved_data['type']} ;
                setup: {retrieved_data['setup']}
                punchline: {retrieved_data['punchline']}
                '''
            except ValueError as e:
                print(e, "There was an error!\n")

        # if isinstance(retrieved_data, list):
        #     for elem in retrieved_data:
        #         print(f'''
        #         id = {elem['id']} ;
        #         type = {elem['type']} ;
        #         setup: {elem['setup']}
        #         punchline: {elem['punchline']}
        #         ''')
        #     return ""
        #
        # elif isinstance(retrieved_data, dict):
        #     return f'''
        #     id = {retrieved_data['id']} ;
        #     type = {retrieved_data['type']} ;
        #     setup: {retrieved_data['setup']}
        #     punchline: {retrieved_data['punchline']}
        #     '''
        # else:
        #     return "Error!"

    @classmethod
    def check_type(cls, input_list, chosen_type):
        """
        Method used for checking the type of jokes
        :param input_list: Input list of jokes
        :param chosen_type: The type of jokes chosen
        :return: A message to confirm whether the jokes are the same type or not
        """
        count = 0
        if chosen_type:
            for elem in input_list:
                if elem['type'] == chosen_type:
                    count += 1
            if count == len(input_list):
                print(f"All jokes are of type {chosen_type}!")
            else:
                print(f"Not all jokes are of type {chosen_type}")
        else:
            return ""

    @classmethod
    def show_odd_even(cls, input_list, choice):
        """
        Method used to show the odd/even jokes from 10 random jokes
        :param input_list: the input list of jokes
        :param choice: choose odd/even or all the jokes
        :return: the jokes
        """
        returned_list = []
        if not choice:
            return input_list
        if choice == "even":
            returned_list = [elem for elem in input_list if int(elem['id']) % 2 == 0]
        elif choice == "odd":
            returned_list = [elem for elem in input_list if int(elem['id']) % 2 != 0]
        return returned_list
