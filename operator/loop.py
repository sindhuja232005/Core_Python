# for i in "image":
#     print(i)
# alpha={
#     9,78,90,65,"book","note"}
# for i in alpha:
#     print(i)
# tup=("in" , 89, "and", 78, "or")
# for i in tup:print(i)
# pos=0
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1
# for hai in range(1,10,+1):
#     print(hai)
# stock=5
# for stock in range(5,0,-1):
#     amt=int(input("Enter the amt: "))
#     if amt>=10000:
#         print("stock quality one has purchased")
#         stock-=1
#     else:
#         print("Insufficient amount to purchase")

# hire=3
# while hire>0:
#     skill=input("Tell us your skill set you know: ")
#     poc=int(input("Tell us how may POC done on "+skill+ ":"))
#     if(skill=="java" or skill=="python") and poc>=4:
#         print("You are received to our company")
#         hire-=1
#     else:
#         print("Try to update your skill/work on more project")

# seats=1
# while seats<=10:
#     if seats%5!=0 and seats%2!=0:
#         amt=int(input("tell us amount to book ticket: "))
#         if amt>=190:
#             print("ticket booked @",seats)
#             seats+=1
#         else:
#             print("insufficient amount")
#     else:
#         seats+=1
#         continue#break

# def name():
#     print("sindhuja")
# name()
    
# def sum():
#     a=100
#     b=200
#     c=a+b
#     return c
# print("Add is",sum())

#         #without return
# def sum():
#     a=100
#     b=200
#     c=a+b
# print("Add is",sum())

           #arguments 
# def name1(name):
#     print("saara",name)
# name1("sindhu")

# def ask(purpose):
#     if purpose == 'Economy' :print("dont worry everything sold to corporate")
#     elif purpose == 'Health':print("That's state govt business")
#     elif purpose == 'Relief' :print("lift the light")
#     else: print("Bharat matha ji jay")
# ask('Health')
# ask('Relief')
# ask('Women safety')

# def greet():
#     ans=input("Tell us ur desired city: ")
#     if ans == 'chennai' :print("too dangerous to live to now")
#     elif ans == 'salem' :print("safe tgo go out")
#     elif ans == 'vllupuram' :print("Don't evr think to go")
#     else: print("stay where you are")
# greet()

# def prompt(qual,ref):
#     if qual == 'ug' and ref == 'HR':
#         print("You are in uk team")
#     elif qual == 'diploma' and ref =='Testlead':
#         print("Test Associate")
#     elif qual =='diploma' and ref =='Test lead':
#         print("Test Associate")
#     else:print("You are hired")
# prompt('engg','project manager')
# prompt('ug','HR')
# prompt(ref='Testlead' , qual='diploma')

                 #function with default argument
# def register(name,location,prefix="Mr/Miss/mrs"):
#     if location =='Salem':
#         print(prefix,name,"has approved in",location)
#     elif location == 'Chennai':
#         print(prefix,name,"has gone under waiting state since its",location)
#     else:print("Business not approved")
# register("Zealoir tech Corp","Salem")
# register("Priya automobiles","Chennai","Mr.")
# register("has been completed","sss")

                        
