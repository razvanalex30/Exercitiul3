import requests


class RetrieveUrl:

    @classmethod
    def retrieve_url(cls, path):
        url = "https://official-joke-api.appspot.com"
        result = requests.get(url + path)
        try:
            # result = requests.get(url + path)
            # print(result.status_code)
            joke = result.json()
            return joke
        except:
            print("Error!!!!",result.status_code)