import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dumps(s):
    with open('/Users/huabin.wen/Puma/p3/python3/files/json.txt', 'w') as f:
        json.dump(s, f)

def loadDumps():
    with open('/Users/huabin.wen/Puma/p3/python3/files/json.txt', 'r') as f:
        print(json.load(f))
    
        

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
dumps([1,2,3])
loadDumps()

