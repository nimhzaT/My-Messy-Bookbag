a= 250#a has global scope and is visible everywhere

def f1():
    b = 250 +10#this function can see the variable and has a local scope
    print(b)

def f2():
    a = 50
    print(a)

f1()
f2()
print(a)

statement = ("End Program Here")
print(statement)
    

a = 250

def f1():
    global a
    a = 100
    print(a)

def f2():
    a = 50
    print(a)

f1()
f2()
print(a)

print(statement)

a = [1,2,3]

def f1():
    global a
    a[0] = 5
    print(a)

def f2():
    a = 50
    print(a)

f1()
f2()
print(a)
print(statement)
#you can overwite a global function with a local value
#use the global keyword to change the value being defined, that has a value
