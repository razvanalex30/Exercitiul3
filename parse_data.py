# import requests
from retrieve_url import RetrieveUrl
from testus import AskInput


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


class ParseData:

    @classmethod
    def parse_data(cls):
        AskInput.ask_choice()
        data = None
        choice = AskInput.choice
        typee = AskInput.type
        nr = AskInput.chosen_number
        if choice == 1:
            data = RetrieveUrl.retrieve_endpoint_1()
        elif choice == 2:
            data = RetrieveUrl.retrieve_endpoint_2()
        elif choice == 3:
            data = RetrieveUrl.retrieve_endpoint_3(typee, nr)
        jokes_formatted = get_formatted_data(data)
        print(jokes_formatted)


# print("""
# Hello! Please choose one of the following three inputs:
# 1 - One random joke
# 2 - Ten random joke
# 3 - One/Ten random jokes by type
# """)
# while True:
#     try:
#         chosen_input = int(input("Enter your choice [1/2/3]: "))
#         if chosen_input == 1:
#             print("You have chosen One random joke!")
#             ParseData.parse_data(chosen_input)
#             break
#         elif chosen_input == 2:
#             print("You have chosen Ten random jokes!")
#             ParseData.parse_data(chosen_input)
#             break
#         elif chosen_input == 3:
#             types = ["general", "programming", "knock-knock"]
#             numbers = [1, 10]
#             type_value = None
#             number = None
#             while type_value not in types:
#                 type_value = str(input("Please choose a type [general|programming|knock-knock]: "))
#                 if type_value in types:
#                     break
#                 else:
#                     print("Invalid type! Please choose a correct value\n")
#             print("Your type chosen was {}".format(type_value))
#             while number not in numbers:
#                 number = int(input("Please choose the number of jokes [1/10]: "))
#                 if number in numbers:
#                     break
#                 else:
#                     print("Invalid! Please choose 1 or 10")
#             ParseData.parse_data(chosen_input, type_value, number)
#             break
#         print("Please enter a valid number!\n")
#     except Exception as e:
#         print(e, "Please choose a valid input!\n")

# AskInput.ask_choice()
ParseData.parse_data()
