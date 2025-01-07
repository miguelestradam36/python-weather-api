from modules.apirequest import APIManager

#Programa principal
if __name__ == "__main__":
    test = APIManager()
    #This will only print the information, you can modify it how you like now that you have an API at hand.
    test.api_request_connection(longitude_="10", latitude_="10")
    del test