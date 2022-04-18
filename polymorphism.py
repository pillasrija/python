# this program is polymorphism with class & objects
# class rabbit:
#     def age(self):
#         print("from rabbit age")
#     def color(self):
#         print("from rabbit color")
#
# class bear:
#     def age(self):
#         print("from bear age")
#     def color(self):
#         print("from bear color")
#
# r_obj=rabbit()
# b_obj=bear()
# for objects in (r_obj,b_obj):
#     objects.color()
#     objects.age()

# class A:
#     x=100
#     def method_a(self):
#         print("from class A")
#
# class B(A):
#     def method_b(self):
#         print("from class B")
#         print(super().x)
#         super().method_a()
#
#
# obj=B()
# obj.method_b()


# overriding method
class A:
    def method(self):
        print("from class A")

class B(A):
    def method(self):
        print("from class B")

b=B()
b.method()

# overloading method
a=10
a=200
print(a)

def print_name():
    return "Hello" + "Madhu"

def print_name(name):
    return "Hello" + "{}".format(name)

print(print_name("python"))

