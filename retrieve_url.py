import requests


# import random


class StatusCode(ValueError):
    pass


class RetrieveUrl:
    base_url = "https://official-joke-api.appspot.com/jokes/"

    # @classmethod
    # def retrieve_endpoint_1(cls):
    #     path_choices = ["/random_joke", "/jokes/random"]
    #     url = "https://official-joke-api.appspot.com"
    #     path = random.choice(path_choices)
    #     result = requests.get(url + path)
    #     joke = result.json()
    #     return joke
    #
    # @classmethod
    # def retrieve_endpoint_2(cls):
    #     path_choices = ["/random_ten", "/jokes/ten"]
    #     url = "https://official-joke-api.appspot.com"
    #     path = random.choice(path_choices)
    #     result = requests.get(url + path)
    #     joke = result.json()
    #     return joke
    #
    # @classmethod
    # def retrieve_endpoint_3(cls, typee, number):
    #     url = "https://official-joke-api.appspot.com/jokes/"
    #     types = ["programming", "general", "knock-knock"]
    #     if typee in types:
    #         url += typee
    #     if number == "1":
    #         url += "/random"
    #     else:
    #         url += "/ten"
    #     result = requests.get(url)
    #     joke = result.json()
    #     return joke

    @classmethod
    def retrieve_endpoint(cls, choice, typee=None, number=None):
        if choice == 1:
            cls.base_url += "random"
            result = requests.get(cls.base_url)
            joke = result.json()
            return joke
        elif choice == 2:
            cls.base_url += "ten"
            result = requests.get(cls.base_url)
            joke = result.json()
            return joke
        elif choice == 3:
            cls.base_url += typee
            if number == "1":
                cls.base_url += "/random"
                result = requests.get(cls.base_url)
                joke = result.json()
                return joke
            elif number == "10":
                cls.base_url += "/ten"
                result = requests.get(cls.base_url)
                joke = result.json()
                return joke
