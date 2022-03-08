import requests
import pandas as pd

def request_wrapper(request):
    print(request)
    return requests.get(request)

def parse_response(response):
    js=response.json()
    assert js['status'] == '1', js
    return pd.DataFrame(js['result'])
    
# etherscan or snowtrace
class Explorer:
    def __init__(self, api_key):
        self.api_key=api_key
    def get_account_balance(self,address):
        pass
    def get_account_history(self,address,block_range):
        pass
    
    
class Etherscan(Explorer):
    def __init__(self,api_key):
        Explorer.__init__(self,api_key)
    def get_account_balance(self,address):
        r = request_wrapper("https://api.etherscan.io/api?module=account&action=balancemulti&address={}&tag=latest&apikey={}".format(address,self.api_key))
        return parse_response(r)
    def get_account_history(self,address,block_range=[0,99999999]):
        r = request_wrapper("https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock={}&endblock={}&sort=asc&apikey={}".format(address,block_range[0],block_range[1],self.api_key))
        return parse_response(r)            

class SnowTrace(Explorer):
    def __init__(self,api_key):
        Explorer.__init__(self,api_key)
    def get_account_balance(self,address):
        pass #r = request_wrapper()
    def get_account_history(self,address,block_range=[0,99999999]):
        r = request_wrapper('https://api.snowtrace.io/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&sort=asc&apikey={}'.format(address, block_range[0], block_range[1], self.api_key))
        return parse_response(r)
    
class Account:
    def __init__(self, explorer, address):
        self.explorer=explorer
        self.address=address
    def get_balance(self):
        return self.explorer.get_account_balance(self.address)
    def get_history(self):
        return self.explorer.get_account_history(self.address)
    