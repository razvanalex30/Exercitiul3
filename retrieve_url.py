import requests
import random


class StatusCode(ValueError):
    pass


class RetrieveUrl:

    @classmethod
    def retrieve_endpoint_1(cls):
        path_choices = ["/random_joke", "/jokes/random"]
        url = "https://official-joke-api.appspot.com"
        path = random.choice(path_choices)
        result = requests.get(url + path)
        joke = result.json()
        return joke

    @classmethod
    def retrieve_endpoint_2(cls):
        path_choices = ["/random_ten", "/jokes/ten"]
        url = "https://official-joke-api.appspot.com"
        path = random.choice(path_choices)
        result = requests.get(url + path)
        joke = result.json()
        return joke

    @classmethod
    def retrieve_endpoint_3(cls, typee, number):
        url = "https://official-joke-api.appspot.com/jokes/"
        types = ["programming","general","knock-knock"]
        if typee in types:
            url += typee
        if number == 1 :
            url += "/random"
        else:
            url += "/ten"
        result = requests.get(url)
        joke = result.json()
        return joke





