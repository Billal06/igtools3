# New Update IGTools3 v0.6
# Install Now
#  $ pip install igtools3

# Example v0.6
import igtools3
ses  = igtools3.Session()
user = "username"
old  = "old password"
new  = "new password"
try:
	change = ses.changePassword(user, old=old, new=new)
	print ("New Password: "+change[1])
except igtools3.exception.ChangeFailed:
	print ("Change Failed")







