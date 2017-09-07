import hashlib

if __name__ == '__main__':
    #test work on terminal python command
    #m = hashlib.md5()
    #m.update('Welcome to Merlin!') #return null
    #print(m.hexdigest())
    
    sha1 = hashlib.sha1()
    sha1.update('Welcome to Puma')
    print(sha1.hexdigest())
