from igtools3 import Session

# Create Tools
s = Session()
get = s.get_info("cyberghost.id") # Replace To Your Usernamd
try:
	print ("Followers: "+get["followers"])
	print ("Folloings: "+get["followings"])
	print ("Title: "+get["title"])
except KeyError:
	print ("Username not found")
