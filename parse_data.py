# import requests
from retrieve_url import RetrieveUrl
import random


def formatted_data(retrieved_data):
    if type(retrieved_data) == list:
        for elem in retrieved_data:
            print('''
            id = {} ; 
            type = {} ;
            setup: {}
            punchline: {}
            '''.format(elem['id'], elem['type'], elem['setup'], elem['punchline']))
        return ""

    elif type(retrieved_data) == dict:
        return '''
        id = {} ; 
        type = {} ;
        setup: {}
        punchline: {}
        '''.format(retrieved_data['id'], retrieved_data['type'], retrieved_data['setup'], retrieved_data['punchline'])
    else:
        return "Error!"


class ParseData:

    @classmethod
    def parse_data(cls, path):
        data = RetrieveUrl.retrieve_url(path)
        jokes_formatted = formatted_data(data)
        print(jokes_formatted)


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
            paths = ["/random_joke", "/jokes/random"]
            print("You have chosen One random joke!")
            chosen_path = random.choice(paths)
            ParseData.parse_data(chosen_path)
            break
        elif chosen_input == 2:
            paths = ["/random_ten", "/jokes/ten"]
            print("You have chosen Ten random jokes!")
            chosen_path = random.choice(paths)
            ParseData.parse_data(chosen_path)
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
            chosen_path = "/jokes/" + type_value
            print("Your type chosen was {}".format(type_value))
            while number not in numbers:
                number = int(input("Please choose the number of jokes [1/10]: "))
                if number in numbers:
                    break
                else:
                    print("Invalid! Please choose 1 or 10")
            if number == 1:
                chosen_path += "/random"
                print("Here is your {} joke!".format(type_value))
            else:
                chosen_path += "/ten"
                print("Here are your ten {} jokes!".format(type_value))
            ParseData.parse_data(chosen_path)
            break

        print("Please enter a valid number!\n")
    except Exception as e:
        print(e, "Please choose a valid input!\n")
