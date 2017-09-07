import hashlib

#test work on terminal python command
m = hashlib.md5()
m.update('Welcome to Merlin!') #return null
print(m.hexdigest())
