from .request import get, post, sess
from .exception import LoginError, URLError, FileError, ConnectionError
from .core import randomAgent
import json, requests, os
from bs4 import BeautifulSoup as bs

class Session:
	def __init__(self):
		self.is_login = False
		self.s = sess()
		self.base = "https://instagram.com"
		self.url = self.base + "/accounts/login/ajax"
		self.csrf = self.s.get(self.base).cookies["csrftoken"]
		self.header = {
			'origin':'https://www.instgram.com',
			'pragma':'no-cache',
			'referer':'https://www.instagram.com/account/login/',
			'user-agent':randomAgent(),
			'x-csrftoken':self.csrf,
			'x-requested-with':'XMLHttpRequest'
		}

	def login(self, user, pwd):
		"Login Tools (No Tested)"
		data = {"username":user, "password":pwd,'queryParams':'{}'}
		self.s.headers = self.header
		try:
			login = self.s.post(self.url, data=data)
			if '"authenticated": true' in login.text:
				self.is_login = True
				return True
			else:
				raise LoginError("Failed Login")
		except requests.execption.ConnectionError:
			raise ConnectionError("No Connection, Plase Turn On Your Connection or Check")

	def get_info(self, name):
		" Get Info Account (Tested)"
		data = {}
		try:
			r = get("http://www.insusers.com/"+name+"/followers", headers={"User-Agent":randomAgent()})
			b = bs(r.text, "html.parser")
			for a in b.findAll("li"):
				dat = a.find("a")
				if "followings" in str(dat.get("href")):
					data["followings"] = a.text
				if "followers" in str(dat.get("href")):
					data["followers"] = a.text
			for title in b.findAll("div", {"class":"prright"}):
				data["title"] = str(title).replace("<p>", "").replace("</p>", "").replace("<br/>", "\n").replace('<div class="prright">', '').replace("</div>","")
			return data
		except requests.exception.ConnectionEror:
			raise ConnectionError("No Connection, Please Turn On Your Connection or Check")

	def get_photo_profile(self, name):
		"For Get Link Photo Profile With Link Post (Tested)"
		try:
			data = {}
			url = self.base+"/"+name
			r = self.s.get(url, headers={"User-Agent":randomAgent()})
			b = bs(r.text, "html.parser")
			try:
				photo = b.find("meta", {"property":"og:image"})["content"]
				data["photo"] = photo
			except TypeError:
				data["error"] = "Failed To Get Link Profile"
			return data
		except Exception as E:
			raise ConnectionError(str(E))

	def download(self, link, file):
		"Tested"
		if os.path.isfile(file):
			try:
				data = self.s.get(link)
				save = open(file, "wb")
				save.write(data.content)
			except Exception as E:
				raise URLE3rror(str(E))
		else:
			raise FileError("File '%s' already exists"%(file))

	def get_followers(self, name, max=10):
		"Tested"
		data = []
		url = "https://globalinta.com/"
		url += name+"/followers"
		self.s.headers = {"User-Agent":randomAgent()}
		r = self.s.get(url)
		b = bs(r.text, "html.parser")
		print (b)
		for ul in b.findAll("ul", {"class":"users"}):
			print ("Mencari")
			a = ul.findAll("a")["href"]
			print (a)
		return data
