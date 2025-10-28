import requests
class Client():
	def __init__(self):
		self.api="https://internxt.com/api"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.token=None
	def create_email(self):
		req=requests.get(f"{self.api}/temp-mail/create-email",headers=self.headers).json()
		self.token=req["token"]
		return req
	def get_inbox(self,token:str=None):
		if token:token=token
		else:token=self.token
		return requests.get(f"{self.api}/temp-mail/get-inbox?token={token}",headers=self.headers).json()