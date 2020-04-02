import igtools3, sys

u = sys.argv[1]
p = sys.argv[2]
l = igtools3.Session()
print (l.login(u, p))
