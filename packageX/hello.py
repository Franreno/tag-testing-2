import requests


class GetHelloWorld():

    @staticmethod
    def get_hello_world():
        URL = "http://localhost:3000/hello-world"

        response = requests.get(URL)
        return response.text
