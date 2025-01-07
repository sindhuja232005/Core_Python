# class college:
#     def __init__(self,name,course):
#         self.n=name
#         self.c=course
#     def print(self):
#         print(self.n,self.c)
#         print("hello")
# c=college("mec",2026)
# c.print()

# ##
# class A:
#     def __init__(self,age,place):
#         self.A=age;
#         self.p=place;
#     def display(self):
#         print(self.A,self.p)
# s=A(20,"MEC")
# s.display()

###single inheritance
# class Account:
#     accountNo=0
#     accountBal=0.0
#     accountHolder=""
#     def __str__(self):
#         return str(self.accountNo)+" "+self.accountHolder+" "+str(self.accountBal)+"\n"
# #single
# class Card(Account):
#     cardNumber=0
#     def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
#         self.cardNumber=cn
#         self.transactions=[]
#         self.accountNo=anum
#         self.accountHolder=ahold
#         self.accountBal=abal
#     def __add__(self,amt):
#         self.accountBal+=amt
#         print(amt,"deposited to",self.accountHolder)
#         self.transactions.append('Credit')
#     def __sub__(self, draw):
#         if self.accountBal>=draw:
#             self.accountBal-=draw
#             print(draw,"has been withdrawn from ",self.accountHolder)
#             self.transactions.append('Debit')
#         else:print("Insufficient account balance")
#     def countTrans(self):
#         creCount=self.transactions.count('Credit')
#         debCount = self.transactions.count('Debit')
#         charges=0
#         if creCount>=5:
#             charges+=(creCount-5)*10
#         if debCount>=3:
#             charges+=(debCount-3)*20
#         print("Total charges on transaction count is",charges)
#         self.accountBal-=charges
#         print("Charges debited in your account")
#     def __str__(self):
#         return str(super(Card, self).__str__())+"\n"+str(self.cardNumber)+" "+str(self.accountBal)+"\n"
# a1=Account()
# a1.accountNo=1456;a1.accountHolder="Nandha";a1.accountBal=15000.0
# print(a1)

# c1=Card(789456123,9876787,"Annamalai",777.9)
# c1+4000
# print(c1)
# c1-1800
# print(c1)
# c1-200
# c1+1000
# c1-100
# c1-500
# c1+10000    
# c1-100
# c1+4000
# print(c1)
# c1.countTrans()


        
###multilevel inheritance
# class college:
#     def getstudentinfo(self):
#         self.__rollno=input("Enter Roll Number: ")
#         self.__name=input("Enter Name: ")

#     def printstudentinfo(self):
#         print("Roll Number: ", self.__rollno,"Name: ",self.__name)

# class BE(college):
#     def getBE(self):
#         self.getstudentinfo()
#         self.__p = int(input("Enter Physics marks: "))
#         self.__c = int(input("Enter Chem marks: "))
#         self.__m = int(input("Enter Maths mark: "))

#     def printBE(self):
#         self.printstudentinfo()
#         print("Marks in different subject: ",self.__p,self.__c,self.__m)

#     def calctotalmarks(self):
#         return(self.__p+self.__m+self.__c)

# class Result(BE):
#     def getResult(self):
#         self.getBE()
#         self.__total=self.calctotalmarks()

#     def putResult(self):
#         self.printBE()
#         print("Total Marks out of 300: ",self.__total)
# college = Result()
# college.getResult()
# college.putResult() 

# # Encapsulation

# class Mobile:
#     __model=""
#     __price=0.0
#     __ram=0
#     __internal=0
#     def setModel(self, mod=""):self.__model=mod
#     def getModel(self):return self.__model
#     def setPrice(self, pri=""):self.__price=pri
#     def getPrice(self):return self.__price
#     def setRam(self, ra=""):self.__ram=ra
#     def getRam(self):return self.__ram
#     def setInternal(self, inte=""):self.__internal=inte
#     def getInternal(self):return self.__internal


# mob1=Mobile()
# mob1.setModel("Iphone 13")
# mob1.setPrice(73000)
# mob1.setRam(128)
# mob1.setInternal(128)
# print(mob1.getModel(),mob1.getPrice(),mob1.getRam(),mob1.getInternal())


# mob2=Mobile()
# mob2.setRam(12)
# mob2.setModel("One plus 10R")
# mob2.setInternal(256)
# mob2.setPrice(45000)
# print(mob2.getModel(),mob2.getPrice(),mob2.getRam(),mob2.getInternal())

# Hierarchy inheritance:
# from array import *

# class Stocks:
#     products=array('i')
#     def show(self):print("Products are: ",self.products)

# class Jaysurya(Stocks):
#     def __init__(self,hey):
#         self.products=array('i')
#         self.products.extend(hey)
#     def search(self):
#         budget=int(input("Enter the price  search:"))
#         for x in self.products:
#             if x<=budget:print(x)
# class Reliance(Stocks):
#     def __init__(self,hai):
#         self.products = array('i')
#         self.products.extend(hai)
#     def getByPosition(self,start,stop):
#         print(self.products[start:stop])

# j=Jaysurya([5000,300,800,780,150])
# r=Reliance([100,200,300,400,500,600,800,1000])

# j.search()

# r.getByPosition(0,5)
# r.show()
# j.show()


# from abc import *

# class Falcon(ABC):
#     def __init__(self):
#         self.mine={78,33,10,40,923,42,56,5,75,477,3,56}
#     #abstract function        
#     def heyThere(self):
#         pass
    

# class Winter(Falcon):
#     def heyThere(self):
#         print(self.mine)


# win=Winter()
# win.heyThere()

# POLYMORPHISM
# class Bird:
#     def sound(self):
#         print("CUCKKOO")

#     def fly(self):
#         print("its can be flying the birds")
# class Bird1(Bird):
#     def cockatail(self):
#         print("cuteiee")
# class Bird2(Bird):
#     def Lovebirds(self):
#         print("couple of love")
# obj1=Bird()
# obj2=Bird1()
# obj3=Bird2()
# obj1.sound()
# obj1.fly();
# obj1.sound()
# obj2.cockatail()
# obj1.sound()
# obj3.Lovebirds()

# #overloading
# class sam:
#     def aa(self,a):
#         print(a)
#     def aa(self,a,b):
#         print(a+b)
#     def aa(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.aa(10)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# o=over()

# print("Sum",o.load(10))
# print("sum1",o.load(10,20)) 
# print("sum",o.load(10,20,30))


#multiple args passing 
#class multiple:
#     def add(self,*args):
#         sum=40;
#         for i in args:
#             sum+=i
            
#         print("add values:",sum)
            
# m=multiple()
# #m.add(20)
# m.add(40,50)
# m.add(40,50,100)
# m.add(40,50,100,200)
# m.add(10,20,60,100,150)
# m.add(10,20,30,40,50,60,70)


# OVERRIDING
# class sam:
#     def name(self):
#         print("sampk")
# class raja(sam):
#     def name(self):
#         super().name()
#         print("raja")
# class arun(raja):
#     def name(self):
#         super().name()
#         print("ARUN")
# s=arun()
# s.name()
# s1=raja()
# s1.name()
# s=arun()
# s.name()

##multiple
# class travels:
#     def name(self):
#         print("ybm travels")
# class travels1:
#     def name1(self):
#         print("kpn travels")
# class main(travels,travels1):
#     def luxary(self):
#         print("enjoy the journey of the happiness")
# m=main()
# m.name()
# m.name1()
# m.luxary()

# # Parent Class
# class Bank:
#     def __init__(self, name):
#         self.name = name

#     def display_bank_name(self):
#         print(f"Welcome to {self.name} Bank!")

# # Child Class 1: Savings Account
# class SavingsAccount(Bank):
#     def __init__(self, name, interest_rate):
#         super().__init__(name)
#         self.interest_rate = interest_rate

#     def calculate_interest(self, balance):
#         interest = balance * (self.interest_rate / 100)
#         print(f"Interest on your savings balance is: ${interest:.2f}")

# # Child Class 2: Current Account
# class CurrentAccount(Bank):
#     def __init__(self, name, overdraft_limit):
#         super().__init__(name)
#         self.overdraft_limit = overdraft_limit

#     def check_overdraft(self, amount):
#         if amount > self.overdraft_limit:
#             print("Overdraft limit exceeded!")
#         else:
#             print(f"Transaction approved. Remaining overdraft limit: ${self.overdraft_limit - amount:.2f}")

# # Creating objects of SavingsAccount and CurrentAccount
# savings = SavingsAccount("Global Bank", 4.5)
# current = CurrentAccount("Global Bank", 1000)

# # Accessing parent and child methods
# savings.display_bank_name()  # From Parent Class
# savings.calculate_interest(2000)  # From SavingsAccount Class

# current.display_bank_name()  # From Parent Class
# current.check_overdraft(800)  # From CurrentAccount Class
# current.check_overdraft(1200)  # Overdraft limit exceeded

##operator overloading
# class operator:
#     def __init__(self,a):
#         self.a=a
        
#         print(self.a+self.a)
# obj=operator(10)
# obj1=operator(20)
# print("sam: ",obj.a+obj1.a)
##using operator over loading
# class oper:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,b):
#         return self.a+b.a
    
# o=oper(50)
# o1=oper(100)
# print("value:",o+o1)

