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
        choice = AskInput.choice
        typee = AskInput.type
        nr = AskInput.chosen_number
        odd_even = AskInput.odd_even
        data = RetrieveUrl.retrieve_endpoint(choice, typee, nr)
        data = Utils.show_odd_even(data, odd_even)
        data = Utils.get_formatted_data(data)
        print(data)


ParseData.parse_data()
