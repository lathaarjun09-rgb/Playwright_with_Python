import requests

class APIClient:
    def __init__(self,base_url):
        self.base_url=base_url.rstrip("/")
        
    def get(self,endpoint,params=None):
        return requests.get(f"{self.base_url}{endpoint}",params=params)
    
    def post(self,endpoint,params=None):
        return requests.post(f"{self.base_url}{endpoint}",params=params)    
    def put(self,endpoint,params=None):
        return requests.put(f"{self.base_url}{endpoint}",params=params)
    
    def patch(self,endpoint,params=None):
        return requests.patch(f"{self.base_url}{endpoint}",params=params)
    
    def delete(self,endpoint,params=None):
        return requests.delete(f"{self.base_url}{endpoint}",params=params)