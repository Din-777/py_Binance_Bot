
class API_keys(object):

    def __init__(self, path):

        self.path = path
        fileRead = open(self.path, "r")

        self.tl_id  = int(fileRead.readline()[11:])
        self.tl_sec = fileRead.readline()[14:-1]

        self.binance_apiKey = fileRead.readline()[10:-1]
        self.binance_api_secret = fileRead.readline()[13:-1]

        fileRead.close()

        pass

