class A:
    def a(self):
        print("running... A")

class B(A):
    def b(self):
        print("running... B")
    
class C(B):
    def c(self):
        print("running... C")

obj = C()
obj.a()
obj.b()
obj.c()
print("-------------------\n")
class A:
    def a(self):
        print("running... A")

class B(A):
    def b(self):
        print("running... B")
    
class C(A):
    def c(self):
        print("running... C")

obj1 = B()
obj1.a()
obj1.b()
print("--------")
obj2 = C()
obj2.a()
obj2.c()