import datetime
number = int(input("enter your number"))
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd") 


    now = datetime.datetime.now()

    print(now.strftime("%Y-%m-%d %H:%M:%S"))
