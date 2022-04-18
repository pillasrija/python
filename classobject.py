class Myclass:
    def myfunc(self):
        pass

    def display(self,name):
        print("name is:", name)


mc=Myclass()
mc.myfunc()
mc.display('scott')


# instance method and static method
class Myclass:
    def m1(self):
        print("instance method")

    @staticmethod
    def m2(self):
        print("static method")


mc=Myclass()
mc.m1()
Myclass.m2(10)

# declaring variables inside the class
class Myclass:
    a,b=100,200
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=Myclass()
mc.add()
mc.mul()


# local variables, class variables, global variables

i,j=15,25

class Myclass:
    a,b=10,20

    def add(self,x,y):
        print(x+y)
        print(self.a+self.b)
        print(i+j)

mc=Myclass()
mc.add(100,200)


# multiple objects for one class

class Myclass:
    def display(self):
        print("good morning")

obj1=Myclass()
obj1.display()

obj2=Myclass()
obj2.display()


# name object and nameless object

class Myclass:
    def display(self):
        print("good morning")

obj1=Myclass()
obj1.display()

Myclass().display()

# checking memory locations of objects
class Myclass:
     def m1(self):
         pass

c1=Myclass()
c2=Myclass()
c3=c1

print(id(c1))
print(id(c2))
print(id(c3))
print(c1 is c2)
print(c1 is c3)
print(c1 is not c2)
print(c1 is not c3)