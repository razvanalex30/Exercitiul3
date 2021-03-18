# import requests
from retrieve_url import RetrieveUrl
from ask_input import AskInput


def get_formatted_data(retrieved_data):
    if isinstance(retrieved_data, list):
        for elem in retrieved_data:
            print(f'''
            id = {elem['id']} ; 
            type = {elem['type']} ;
            setup: {elem['setup']}
            punchline: {elem['punchline']}
            ''')
        return ""

    elif isinstance(retrieved_data, dict):
        return f'''
        id = {retrieved_data['id']} ; 
        type = {retrieved_data['type']} ;
        setup: {retrieved_data['setup']}
        punchline: {retrieved_data['punchline']}
        '''
    else:
        return "Error!"


def check_type(input_list, chosen_type):
    count = 0
    for elem in input_list:
        if elem['type'] == chosen_type:
            count += 1
    if count == len(input_list):
        print(f"All jokes are of type {chosen_type}!")
    else:
        print(f"Not all jokes are of type {chosen_type}")


def show_odd_even(input_list, choice):
    returned_list = []
    if choice == "even":
        for elem in input_list:
            if int(elem['id']) % 2 == 0:
                returned_list.append(elem)
        return returned_list
    elif choice == "odd":
        for elem in input_list:
            if int(elem['id']) % 2 != 0:
                returned_list.append(elem)
        return returned_list
    else:
        return input_list


class ParseData:

    @classmethod
    def parse_data(cls):
        AskInput.ask_choice()
        choice = AskInput.choice
        typee = AskInput.type
        nr = AskInput.chosen_number
        odd_even = AskInput.odd_even
        if choice == 1:
            data = RetrieveUrl.retrieve_endpoint_1()
            jokes_formatted = get_formatted_data(data)
            print(jokes_formatted)
        elif choice == 2:
            data = RetrieveUrl.retrieve_endpoint_2()
            chosen_jokes = show_odd_even(data, odd_even)
            jokes_formatted = get_formatted_data(chosen_jokes)
            print(jokes_formatted)
        elif choice == 3:
            data = RetrieveUrl.retrieve_endpoint_3(typee, nr)
            check_type(data, typee)
            chosen_jokes = show_odd_even(data, odd_even)
            jokes_formatted = get_formatted_data(chosen_jokes)
            print(jokes_formatted)


ParseData.parse_data()
