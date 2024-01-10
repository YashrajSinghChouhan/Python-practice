def hello():
    print("Hello World")
    
hello()

def add(a = 0, b = 0, c=0):
    return a+b+c

print(add()," ",add(1)," ",add(1+1)," ",add(1+1+1))


class A:
    def display(self):
        print("A class display")

class B(A):
    def display(self):
        print("B class display")

    def superdisplay(self):
        super().display()

obj = A()
obj.display()
obj1 = B()
obj1.display()
obj1.superdisplay()