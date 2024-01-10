# Generator
def gene():
    yield 1
    yield 2
    yield 3

day = gene()
print("Hello it is day",next(day))
print("and i'm practicing python advance")
print(next(day),"working at 4 am")
print(next(day),"will see what happens")

# Iterator
print("-----------\n")

lis = "I'm making a list for practicing".split()
it = iter(lis)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Lambda
print("------------\n")
lmbda = lambda x:x*x
print(lmbda(3))

# Map

lis = [1,2,3,4,5,6]
l = list(map(lambda x:x+6,lis))
print(l)

# Filter

lis = [1,2,3,4,5,6]
l = list(filter(lambda x:x%2,lis))
print(l)

# Decorator

def design(funx):
    def inner():
        print("------ starting decoration ------")
        funx()
        print("------ ending decoration --------")
    return inner

@design
def hello():
    print("Hello")

def world():
    print("World")

hello()
design(world)()

# file Handling
print("\n-------------------")
f = open("hello.txt",'w')
f.write("Harry potter")
f.close()

a = open("hello.txt",'a')
a.write(" - best story ever")
a.close()

with open("hello.txt",'r') as o:
    print(o.read())

print("----------------------")