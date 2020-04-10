# New update 'igtools3' v0.5
# Install Now
#  $ pip install igtools3

# Example v0.5
import igtools3
name = input("Username: ")
session = igtools3.Session()
for user in session.search_by_name(name):
	print (user)







