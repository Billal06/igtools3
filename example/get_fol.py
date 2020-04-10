# Update igtools v0.7
# Install Now
#   $ pip inatall igtools3

# Example v0.7
import igtools3

id = "31085556612"
ses = igtools3.Session()
print (ses.get_followers_name(id, max=100))
