       #biodata
# name=input("Enter your name: ")
# mob=int(input("Enter your mobile number: "))
# mail=input("Enter your mail: ")
# father=input("Enter your father name:")
# gender=input("Enter your gender: ")
# dob=(input("Enter your dob: "))
# age=int(input("Enter your age: "))
# place = input("Where are you from: ")
# dep=input("Which department you are: ")
# religion=input("Enter your religion: ")
# print("My name is: ",name)
# print("My mobile number is: ",mob)
# print("My mail is: ",mail)
# print("My father name is: ",father)
# print("My dob is: ",dob)
# print("My age is: ",age)
# print("My gender is: ",gender)
# print("I am from: ",place)
# print("My department is: ",dep)
# print("My religion is: ",religion)

                            #theme part 
##Write a Python program that allows a user to select different rides at a theme park. The program should display a menu with the following options:
               ##Roller Coaster 2.Ferris Wheel 3.Bumper Cars 4.Exit
# choice=int(input("Enter your choice: 1/2/3/4 "))
# if choice==1: print("You are selected the Roller coaster! Hold on tight!")
# elif choice==2: print("You are selected the Ferris Wheel! Enjoy the view!")
# elif choice==3: print("You selected the Bumper cars! Get ready for some fun!")
# else:  print("Thankyou for visiting the themepark! and exit")

##Write a Python program that asks the user for their age and determines their ticket price for a theme park. The ticket prices are as follows:
##Ages 0-3: Free
##Ages 4-12: ₹100
##Ages 13-59: ₹250
##Ages 60 and above: ₹150
##If the user enters a negative number or an invalid age, display "Invalid age. Please try again." 
# age=int(input("Enter your age: "))
# if(0<=age<=3):
#     print("free")
# elif 4<=age<=12:
#     print("Rs 100")
# elif 13<=age<=59:
#     print("Rs 250")
# elif age>=60:
#     print("Rs.150")
# else:
#     print("Invalid age")

                            ##calculator
# a=int(input("Enter a value: "))
# b=int(input("Enter b value:"))
# operation=input("Enter the operation: add/sub/mul/div: ")
# if(operation=="add" or operation=="Add"):
#     c=a+b
#     print("The Addition is: ",c)
# elif(operation=="sub" or operation=="Sub"):
#     c=a-b
#     print("The Subtraction is: ",c)
# elif(operation=="mul" or operation=="Mul"):
#     c=a*b
#     print("The Multiplication is: ",c)
# elif(operation=="div" or operation=="Div"):
#     c=a/b
#     print("The Division is: ",c)
# else:
#     print("invalid input")

                            ##factorial of number
# num=int(input("Enter a number "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
  #  print("Factorial of ",i, "is",fact)
    # print(fact)
