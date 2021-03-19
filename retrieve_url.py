import requests


class RetrieveUrl:
    base_url = "https://official-joke-api.appspot.com/jokes/"

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
