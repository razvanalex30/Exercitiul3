import requests


class RetrieveUrl:
    base_url = "https://official-joke-api.appspot.com/jokes/"
    """
    Class used to retrieve the url path based on user's input
    """
    @classmethod
    def retrieve_endpoint(cls, choice, joke_type=None, number=None):
        """
        Method used for retrieving data from the URL
        :param choice: The choice from the user (1 random joke, 10 random jokes or 1/10 random jobes by type)
        :param joke_type: The type of joke, if selected
        :param number: Number of jokes in case of jokes by type

        """
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
            cls.base_url += joke_type
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
