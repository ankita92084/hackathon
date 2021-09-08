print("WELCOME TO UBER APPLICATION")
vehicle=input("select vehicle: -")
if vehicle=="cab" or vehicle=="bike" :
    print("thnkyou for selecting vehicle")
else:
    print("sorry it's booked nd nto avilable")

pickup_location=input("enter pickup location :")
print("thnkyou for entering location please wait ")

destination=(input("type your destination:-"))
print("your desination is",destination)
i=4
while i<=5:
    print("you are far from ",pickup_location ,"to",destination,i*2,"kilo meter and your price is 200 rupees")
    i+=1
    break
drivers=input("choose driver name: ")
if drivers == "salman":
    print("age=20"," \n ","phone no.=4567876523")
elif drivers=="sharukh":
    print("age=22"," \n ","phone no.=9675438623")
else:
    print("no driver available")
payment=input("choose the option  you want to pay:  ")
if payment=="cash":
    print("for cash you have to wait for the rider or driver: ")
if  payment=="online":
    print("now you have to select online method ")
else:
    print(" first please select any option of payment :-")
options_of_payment=input("select an option for payment of online /upi/debit crad:- ")
if options_of_payment=="UPI" :
    print("your payment getway is ready")
upi=int(input("enter the upi pin"))
if upi<=0:
    print("your payment is success full")
elif options_of_payment=="debit card":
    print("your payment is successfully done ")
else:
    print("please make your payment")
print("thnkyou for visiting uber app keep visiting ")







