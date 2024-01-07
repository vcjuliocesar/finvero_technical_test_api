import httpx
import base64
from datetime import datetime
from src.infrastructure.config.enviroment import get_enviroment_settinngs


class Belvo:

    def __init__(self) -> None:

        self.env = get_enviroment_settinngs()
        self.user = self.env().SECRETID
        self.password = self.env().SECRETPASSWORD
        self.link = self.env().LINKID
        self.base_url = self.env().BASE_URL
        self.base = "%s:%s" % (self.user, self.password)
        self.encoded_bytes = base64.b64encode(self.base.encode('utf-8'))
        self.encoded_string = self.encoded_bytes.decode('utf-8')
        self.headers = {'Authorization': f'Basic {self.encoded_string}'}

    async def get_transactions(self,page_size:str = '100'):
        
        async with httpx.AsyncClient() as client:
            try:
                url = f"{self.base_url}/api/transactions/"
                params = {
                    'page_size':page_size,
                    'link':self.link,
                }
                retrive_response = await self.post_retrieve_transactions()
                
                if retrive_response == 201:
                    
                    response = await client.get(url, headers=self.headers,params=params)
                    
                    if response.status_code == 200:

                        return response.json()
                    
                    else:
                        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
                    
                return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
            except httpx.HTTPError as e:
                return {"error": f"HTTP error occurred: {e}"}

    async def get_accounts(self):
        
        async with httpx.AsyncClient() as client:
            try:
                
                retrive_accounts = await self.post_retrieve_accounts()
                
                if retrive_accounts == 201:
                    
                    url = f"{self.base_url}/api/accounts/"
                    response = await client.get(url, headers=self.headers)

                    if response.status_code == 200:

                        return response.json()
                    else:
                        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
                    
                return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
            except httpx.HTTPError as e:
                return {"error": f"HTTP error occurred: {e}"}
    
    async def post_retrieve_transactions(self):
        date_from: str = datetime(datetime.now().year,1,1).strftime("%Y-%m-%d")
        date_to: str = datetime.now().strftime("%Y-%m-%d")
        body = {'link': self.link, 'date_from': date_from, 'date_to': date_to}
        

        async with httpx.AsyncClient() as client:
            try:
                url = f"{self.base_url}/api/transactions/"
                response = await client.post(url, headers=self.headers, json=body)

                if response.status_code == 201:

                    return response.status_code
                else:
                    return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
            except httpx.HTTPError as e:
                return {"error": f"HTTP error occurred: {e}"}
            
    async def post_retrieve_accounts(self):
        body = {'link': self.link}
        
        async with httpx.AsyncClient() as client:
            try:
                url = f"{self.base_url}/api/accounts/"
                response = await client.post(url, headers=self.headers, json=body)

                if response.status_code == 201:

                    return response.status_code
                else:
                    return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
            except httpx.HTTPError as e:
                return {"error": f"HTTP error occurred: {e}"}
            
