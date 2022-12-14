#Example1
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
# bobj=B()
# bobj.m2()
# bobj.m1()

#Example2: single inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# bobj =B()
# bobj.m1() #30
# bobj.m2() #100

#Example3: Multilevel inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj = C()
# cobj.m3()
# cobj.m2()
# cobj.m1()
# print("-----------------------------------------------------------------")
# bobj = B()
# bobj.m2()
# bobj.m1()

#Example4: Hierarchy Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj = C()
# cobj.m1()
# cobj.m3()
# print("-----------------------------------------------------------------")
# bobj=B()
# bobj.m2()
# bobj.m1()

#Example5: Multiple Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B():
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

#Example6: Polymorphism :: Overridden -- calling parent class method using child class (super())
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m1(self):
#         print("this is m1 method from class B")
#         super(B, self).m1()
# bobj = B()
# bobj.m1() #this is m1 method from class B

#Example7:
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self, x,y):
#         print(x+y) #local variables
#         print(self.i+self.j) #class variables
#         print((self.a,self.b)) #class variables from class A
# bobj = B()
# bobj.m(1000,2000)

#Example8: overriding variables
# class Parent:
#     name="Scott"
# class Child(Parent):
#     name="John" #overriding the variable value
#     def test(self):
#         print(super().name)
# cobj = Child()
# cobj.test()
# print(cobj.name)

#Example9: Overriding methods()
# class Bank:
#     def rateOfInterest(self):
#         return 0;
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10;
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12;
#
# objx = XBank()
# print(objx.rateOfInterest()) #10
#
# objy = YBank()
# print(objy.rateOfInterest()) #12

#Example10: Overloading
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")

h=Human()
h.sayhello()
h.sayhello("Scott")

print("--------------------------------------------------------------------------")
class Calculator:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
c=Calculator()
c.add()
c.add(10,20)
c.add(10,20,30)
