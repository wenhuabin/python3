import os

def getOSParams():
    print(os.name)
    print(os.uname())
    print(os.environ)


def createFolder(foldername):
    path = os.path.join(os.path.abspath('.'), foldername)
    os.mkdir(path)

def deleteFolder(foldername):
    path = os.path.join(os.path.abspath('.'), foldername)
    os.rmdir(path)

def getFileName():
    print(os.path.split('/Users/michael/testdir/file.txt'))
    print(os.path.splitext('/Users/michael/testdir/file.txt'))

def getAllPyFiles():
    files = [x for x in os.listdir('.') if os.path.isfile(x) 
            and os.path.splitext(x)[1]=='.py']
    print(files)

def getAllFolders():
    folders = [x for x in os.listdir('.') if 
            os.path.isdir(x)]
    print(folders)

def renameFile():
    os.rename('hello.text', 'hello.py')
    os.remove('hello.py')




getOSParams()
createFolder('test')
deleteFolder('test')
getFileName()
getAllPyFiles()
getAllFolders()



