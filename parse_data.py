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


print("Hi! Please choose 1 of these 3 inputs")
print("1 - Random joke, 2 - 10 Random jokes, 3 - Random jokes by type")
while True:
    try:
        chosen_input = int(input("Enter your choice: "))
        if chosen_input == 1:
            paths = ["/random_joke", "/jokes/random"]
            print("You have chosen a random joke!")
            chosen_path = random.choice(paths)
            ParseData.parse_data(chosen_path)
            break
        elif chosen_input == 2:
            paths = ["/random_ten", "/jokes/ten"]
            print("You have chosen 10 Random Jokes!")
            chosen_path = random.choice(paths)
            ParseData.parse_data(chosen_path)
            break
        elif chosen_input == 3:
            types = ["general", "programming", "knock-knock"]
            numbers = [1, 10]
            type_value = None
            number = None
            while type_value not in types:
                type_value = str(input("Please choose a type: "))
                if type_value in types:
                    break
                else:
                    print("Try again!\n")
            chosen_path = "/jokes/" + type_value
            print("Your type chosen was {}".format(type_value))
            while number not in numbers:
                number = int(input("Please choose the number of jokes: "))
                if number in numbers:
                    break
                else:
                    print("Try again!")
            if number == 1:
                chosen_path += "/random"
            else:
                chosen_path += "/ten"
            print("Here are your jokes!")
            ParseData.parse_data(chosen_path)
            break

        print("Please enter a valid number!\n")
    except Exception as e:
        print(e, "Please choose a valid input!\n")
