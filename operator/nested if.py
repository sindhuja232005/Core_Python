# age=int(input("Enter your age: "))
# if age>=18:
#     print("welcome to theme park")
#     print("you allowed for water games")
#     gender=input("Enter your gender: ")
#     if gender=="MALE" or gender=="male":
#         print("your zone number is 234")
#     else:
#         print("your zone number is 123")
# else:
#     print("you are not allowed")
    
ward = int(input("Enter the ward number: "))
if 35<ward<75:
    partno=int(input("Enter the part number: "))
    if partno==123:
        print("your room number is 12")
    elif partno==234:
        print("Your room number is 23")
    elif partno==345:
        print("Your room number is 34")
    else:
        print("invalid partno")
else:
    print("You are not in the ward")