'''
#Private Varible(Encapsulation)...!
class A:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print("Here it is..!")
a=A("Rahul",23)
a__age=54
print(a.name)
print(a._A__age)

#Calling Static method using another method...!
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @staticmethod
    def show(a,b):
        c=a+b
        print(c)
    def display(self):
        self.show(self.a,self.b)
a,b=int(input()),int(input())
a1=A(a,b)
a1.display()

#Method Overriding(Polymorphism)
class Phone:
    def __init__(self,name):
        self.name=name
    def buy(self):
        print("Yes you can buy...!")
class smartPhone(Phone):
    def __init__(self,Price):
        self.Price=Price
    def buy(self):
        super().buy()
        print("Buy that phone..!",self.Price)

s1=smartPhone(23400)
s1.buy()
'''

#Multiple Inheritance
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def buy(self):
        print("Go and buy that...!")
class B:
    def buy(self):
        print("Ok,I am going to buy...!")
class C(B,A):
    def buy(self):
        super().buy()
        print("--- Buying ---")
c1=C("George Washington",32)
c1.buy()
