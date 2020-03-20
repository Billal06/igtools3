from igtools3 import Session

# Create Tools
s = Session()
# Get Link
get = s.get_photo_profile("name") # Replace To Your Username
# Get Link With Photo
print ("Link: "+get["photo"])
