from .request import get, post, sess
from .exception import LoginError, URLError, FileError, ConnectionError
from .core import randomAgent
import json, requests, os
from bs4 import BeautifulSoup as bs

class Session:
	is_login = False
	def __init__(self):
		self.is_login = False
		self.s = sess()
		self.base = "https://instagram.com"
		self.url = self.base + "/accounts/login/ajax"
		self.csrf = self.s.get(self.base).cookies["csrftoken"]

	def _default_header(self):
		head = {
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive',
			'Content-Length': '0',
			'Host': 'www.instagram.com',
			'Origin': 'https://www.instagram.com',
			'Referer': 'https://www.instagram.com/',
			'User-Agent': randomAgent(),
			'X-Instagram-AJAX': '1',
                  'X-Requested-With': 'XMLHttpRequest'
		}
		return head

	def _default_cookies(self):
		kuki = {'sessionid': '', 'mid': '', 'ig_pr': '1',
		'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
		's_network': '', 'ds_user_id': ''}
		return kuki

	def login(self, user, pwd):
		global j
		"Login Tools (No Tested)"
		header = self._default_header()
		self.s.cookies.update(self._default_cookies())
		self.s.headers.update(header)
		self.s.get(self.base)
		csrf = self.s.cookies.get_dict()['csrftoken']
		self.s.headers.update({'X-CSRFToken': csrf})
		data = {"username": user, "password":pwd}
		request = self.s.post(self.url, data=data, allow_redirects=True)
		print (request.text)
		try:
			j = json.loads(request.text)
		except json.decoder.JSONDecodeError:
			raise LoginError("Failed Login")
		if j["status"] == "ok":
			self.is_login = True
			self.s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})

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
		for ul in b.findAll("ul", {"class":"users"}):
			a = (str(ul).findAll("a")["href"]).replace("/", "")
			print (str(a))
		return data
