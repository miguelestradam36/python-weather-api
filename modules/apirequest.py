"""

"""
class APIManager:
    #modules (this is one way to avoid having to make the imports on the main code)
    openmeteo_requests =  __import__('openmeteo_requests')
    requests_cache =  __import__('requests_cache')
    pandas =  __import__('pandas')
    retry_requests =  __import__('retry_requests')
    #attributes

    def __init__(self):
        #Entrada city: string
        #Output (no variable): just printing output
        try:
            city = "Mumbai"
            
        except Exception as error:
            print("ERROR: {}.\nERROR_TYPE: {}".format(error, type(error)))