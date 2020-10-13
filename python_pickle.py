import pickle
import os
DB = {}
def New_User():
    f=open('Database.dat','wb')
    flag = True
    while flag:
        user_name = raw_input("Enter your name : ")
        user_pin = input("Enter your new 4 - digit pin linked to this account : ")
        confrm_pin = input("Renter you pin to confirm : ")
        user_id = raw_input("Enter you mail ID : ")
        user_mob = raw_input("Enter you mobile number : ")
        user_savings=100
        if user_pin == confrm_pin:
            DB[(user_name,user_pin)]=[user_id,user_mob,user_savings,user_id]
            pickle.dump(DB,f)
            f.close()
            flag = False
            print "Account has been creted in the database...."
            Display_Details(user_name,user_pin)
        else:
            print "The passwords you entered do not match. Please try again!!"
    

def Display_Details(x,y):
    #x = raw_input("Please enter your name : ")
    #y = input("Enter you 4 - digit pin : ")
    f=open('Database.dat','wb')
    for j in DB.keys():
        if j == (x,y):
            print
            print "--------------------PERSONAL DETAILS--------------------"
            print ">>>>> Full Name : ",x
            print ">>>>> Email ID : ",DB[j][3]
            print ">>>>> Mobile Number : ",DB[j][1]
            print "--------------------ACCOUNT DETAILS--------------------"
            print ">>>>> Savings Account Balance : ",DB[j][2]
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
            print
    pickle.dump(DB,f)
    f.close()

def Withdraw(x,y):
    #x = raw_input("Please enter your username : ")
    #y = input("Enter you 4 - digit pin : ")
    for j in DB.keys():
        if j == (x,y):
            wid = input("Enter amount to be withdrawed : ")
            if DB[j][2]>=wid:
                DB[j][2]=DB[j][2]-wid
                print "Withdrawal complete."
            else:
                print "insufficient balance"
    Display_Details(x,y)            
                
def Deposit(x,y):
    #x = raw_input("Please enter your username : ")
    #y = input("Enter you 4 - digit pin : ")
    for j in DB.keys():
        if j == (x,y):
            dep = input("Enter amount to be deposited : ")
            DB[j][2]=DB[j][2]+dep
            print "Deposit complete."
    Display_Details(x,y)
    
print "============================================================================"
print "------------------------------UNIVERSAL AXIS BANK----------------------------"
print "============================================================================"
ch = "y"
f=open('Database.dat','ab+')
e='Database.dat'
k=os.path.abspath(e)
if os.stat(k).st_size==0:
    f.close()
else:
    #f=open('Database.dat','rb')
    DB=pickle.load(f)
    f.close
while ch == "y" or ch == "Y":
    new = raw_input("New User? [y/n] ")
    if new in [ 'y' ,' Y' , 'yes' , 'YES' ]:
        New_User()
               
    else:
        x = raw_input("Please enter your name : ")
        y = input("Enter you 4 - digit pin : ")
        j = (x,y)
        if j in DB.keys():
            while x = "y":
                print "-----------SERVICES-----------"
                print "1. Withdraw money "
                print "2. Deposit money "
                print "3. Check account details "
                choice = input("Enter one of above choices to continue : ")
                if choice == 1:
                    Withdraw(x,y)
                elif choice == 2:
                    Deposit(x,y)
                else:
                    Display_Details(x,y)
                x = raw_input("Continue with this account?? [y/n]")
        else:
            print "Invalid PIN or USERNAME"
    ch=raw_input("DO YOU WISH TO CONTINUE? [y/n]")
else:
    print "THANK YOU FOR USING OUR SERVICES"
            



            
