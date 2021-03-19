from retrieve_url import RetrieveUrl
from ask_input import AskInput
from utils_method import Utils


class ParseData:
    """
    Class used to parse the data from the endpoint
    """
    @classmethod
    def parse_data(cls):
        """
        Method used to parse the data from the endpoint according to user's input
        """
        AskInput.ask_choice()
        odd_even = AskInput.odd_even
        data = RetrieveUrl.retrieve_endpoint(AskInput.choice, AskInput.joke_type, AskInput.chosen_number)
        Utils.check_type(data, AskInput.joke_type)
        data = Utils.show_odd_even(data, odd_even)
        data = Utils.get_formatted_data(data)
        print(data)


ParseData.parse_data()
