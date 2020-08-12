import requests,json


class euro_oracle:
    def __init__(self,url:str):
        self.url= url
        self.euro_try = 0
        self.resp_json = {}
    def refresh(self)-> None:
        response = requests.get(self.url)
        self.resp_json = json.loads(response.text)
    def get_euro_try_parity(self) -> float:
        pass

class exchangeratesapi(euro_oracle):
    def __init__(self,url:str = 'https://api.exchangeratesapi.io/latest'):
        super().__init__(url)
    def refresh(self)-> None:
        super().refresh()
    def get_euro_try_parity(self) -> float:
        self.euro_try = float(self.resp_json['rates']['TRY'])
        return self.euro_try

class currconv(euro_oracle):
    apikey = '6aa4fce38a7c1405c6b0'
    def __init__(self,url:str='https://free.currconv.com/api/v7/convert?q=EUR_TRY&compact=ultra&apiKey='):
        super().__init__(url + self.apikey)
    def refresh(self)-> None:
        super().refresh()
    def get_euro_try_parity(self) -> float:
        self.euro_try = float(self.resp_json['EUR_TRY'])
        return self.euro_try