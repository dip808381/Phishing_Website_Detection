def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

def plus(a):
    s = 0
    for i in a:
        s = s + i
    return s
    
def name():
    nam = input("Please enter your name: ")
    return 'Your name is:' + nam
        
