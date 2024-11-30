import mysql.connector as con
project=con.connect(host="localhost",user='root',password='amritaryamysql@001234', database="railway")
mycur=project.cursor()
mycur.execute("create database if not exists railway")
mycur.execute("use railway")
mycur.execute("create table if not exists train(tno int,tname varchar(50),tsource varchar(30),tdest varchar(20),tnos int,tfare int)")
mycur.execute("create table if not exists reserve(tno int(20),tname varchar(40),tsource varchar(40),tdest varchar(50),tnos int,tfare int, da int(40),pnr int primary key)")
mycur.execute("create table if not exists canc(tno int(20),tname varchar(40),tsource varchar(40),tdest varchar(50),tnos int,tfare int, da int(40),pnr int primary key)")
project.commit()

#*****************************************************************************
#                            TRAIN CLASS USED IN PROJECT 
#*****************************************************************************"""
def create_train():                                                 #function to get data from user
    tno=int(input("Enter Train Number : "))
    tname=input("Enter the name of the Train : ")
    tname=tname.upper()
    tsource=input("Enter the Source Station : ")
    tsource=tsource.upper()
    tdest=input("Enter the Destination Station : ")
    tdest=tdest.upper()
    tnos=int(input("Enter Number of Seats : "))
    tfare=int(input("Enter Fare of the Train : "))
    q = "insert into train values(%s,%s,%s,%s,%s,%s)"
    data =(tno,tname,tsource,tdest,tnos,tfare)
    cr1 = project.cursor()
    cr1.execute(q,data)
    project.commit()
        
def show_train():     #function to show data on screen
    c2=project.cursor()
    c2.execute("select * from train")
    z=c2.fetchall()
    print('-'*100)
    print( "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Train_Source","%-20s"%"Train_Destination","%-10s"%"Train_nos","%-10s"%"Train_Fare")
    print(' '*100)
    print("-"*100)
    for i in z:
         print( "%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5])
         print("-"*100)


def delete_train(t):          #function to get new data from user
    c3=project.cursor()
    q="delete from train where tno="+str(t)
    c3.execute(q)
    project.commit()
    print("Train data updated sucessfully  ")

def display_train(num):
    q="select * from train where tno="+str(num)
    c5=project.cursor()
    
    c5.execute(q)
    z=c5.fetchall()
    print('-'*100)
    print( "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Train_Source","%-20s"%"Train_Destination","%-10s"%"Train_nos","%-10s"%"Train_Fare")
    print(' '*100)
    print("-"*100)
    for i in z:
         print( "%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5])
         print("-"*100)
   

#******************************************************
#         RESERVATION CLASS USED IN PROJECT
#******************************************************

def reservation():
    n=int(input("Enter Train Number="))
    pnr=int(input("enter pnr(6)="))
    c6=project.cursor()
    q="select * from train where tno="+str(n)
    c6.execute(q)
    z=c6.fetchall()
    for i in z:
        print('Train_no=',i[0])
        print('Train_Name=',i[1])
        print("Source=",i[2])
        print("Destination=",i[3])
        print('fare=',i[5])
        print("no of seats avialable=",i[4])
        nos=int(input("No seats required"))
        a=int(i[5])*nos
        print("total fare=",a)
        print("Detail of travel:")
        da =(input("enter date= datedayyear"))
        print("...............................................")
        print("...............................................")
        print("Pnr no:",pnr)
        print("Train no:",i[0])
        print("Train name:",i[1])
        print("Boarding point:",i[2])
        print("Destination pt:",i[3])
        print("No of seats reserved:",nos)
        print("Date of reservation:",da)
        print("You must pay:",a)
        print("***********************************************")
        print(".........END OF RESERVATION.................")
        print("***********************************************")
        q="insert into reserve values(%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(i[0],i[1],i[2],i[3],nos,a,da,pnr)
        c7=project.cursor()
        c7.execute(q,value)
        project.commit()
        print("Reservation done sucessfully")

def display_reserv(num):
    q="select * from reserve where pnr="+str(num)
    c5=project.cursor()
    
    c5.execute(q)
    z=c5.fetchall()
    print('-'*100)
    print("%-10s"%"PNR", "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Boarding station","%-20s"%"Destination","%-10s"%"no of seats booked","%-10s"%"date of journey")
    print(' '*100)
    print("-"*100)
    for i in z:
         print("%-10s"%i[7],"%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5],"%-10s"%i[6])
         print("-"*100)
   
def display_allReservation():     #function to show data on screen
    c2=project.cursor()
    c2.execute("select * from reserve")
    z=c2.fetchall()
    print('-'*100)
    print("%-10s"%"PNR", "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Boarding station","%-20s"%"Destination","%-10s"%"no of seats booked","%-10s"%"date of journey")
    print(' '*100)
    print("-"*100)
    for i in z:
         print("%-10s"%i[7],"%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5],"%-10s"%i[6])
         print("-"*100)

def write_cancel():
    n=int(input("Enter pnr no= "))
    c8=project.cursor()
    q="select * from reserve where pnr="+str(n)
    c8.execute(q)
    z=c8.fetchall()
    print('-'*100)
    print("%-10s"%"PNR", "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Boarding station","%-20s"%"Destination","%-10s"%"no of seats booked","%-10s"%"date of journey")
    print(' '*100)
    print("-"*100)
    for i in z:
         print("%-10s"%i[7],"%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5],"%-10s"%i[6])
         print("-"*100)
         b=int(i[6])-int(i[6])*0.1
         print("Refund amount=",b)
         input("Press enter to cancel your reservation")
         q="insert into canc values(%s,%s,%s,%s,%s,%s,%s,%s)"
         data=(i[0],i[1],i[2],i[3],i[4],b,i[6],i[7])
         c8.execute(q,data)
         v="delete from rest where pnr="+str(n)
         c8.execute(v)
         print("Reservation cancelled susscefully!!!!")

def display_cancel(num):
    c9=project.cursor()
    q="select * from canc where pnr="+str(num)
    c9.execute(q)
    z=c9.fetchall()
    print('-'*100)
    print("%-10s"%"PNR", "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Boarding station","%-20s"%"Destination","%-20s"%"no of seats booked","%-20s"%"Refund Amount","%-20s"%"date of journey")
    print(' '*100)
    print("-"*100)
    for i in z:
         print("%-10s"%i[7],"%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5],"%-10s"%i[6])
         print("-"*100)
    
def display_allcancellation():
    q="select * from canc"
    c4=project.cursor()
    c4.execute(q)
    z=c4.fetchall()
    print('-'*100)
    print("%-10s"%"PNR", "%-12s"%"Train_no","%-20s"%"Train_Name","%-20s"%"Boarding station","%-20s"%"Destination","%-20s"%"no of seats booked","%-20s"%"Refund Amount","%-20s"%"date of journey")
    print(' '*100)
    print("-"*100)
    for i in z:
         print("%-10s"%i[7],"%-12s"%i[0],"%-20s"%i[1],"%-20s"%i[2],"%-20s"%i[3],"%-10s"%i[4],"%-10s"%i[5],"%-10s"%i[6])
         print("-"*100)
   
"""*************************************************"""
    
def welcome():
     print ("This programme is made by :")
     print (" SONAM SARANGI ")
     print (" OF STD. XII 'A'")
     print ("ROLL NO. = ")
     print ("school : JUSCO SCHOOL SOUTH PARK")
     print("****************WELCOME****************")
     print("******to RAILWAY TICKET RESERVATION SYSTEM***********")
     print ("we are here to serve you")

    
"""*****************************************************************************
                        TRAIN MENU FUNCTION
*****************************************************************************"""

def train_menu():
    while True:
        print("\n",60*"=")
        print( "\n\tTRAIN MENU:")
        print("\n",60*"=")
        print( "1.  Add Train")
       
        print( "2.  Search Train")
        print( "3.  All Train List")
        print( "4.  Delete Train")
        print( "5.  Return to Main Menu")
        ch=int(input("Enter Your Choice(1~6): "))
        if ch==1:
            create_train()
            
        elif ch==4:
            num=int(input("\n\nEnter Train Number: "))
            delete_train(num)
        elif ch==2:
            num=int(input("\n\nEnter Train Number: "))
            display_train(num)

        elif ch==3:
            show_train()

        elif ch==5:
            welcome()
            break
            
    

        else:
            print( "Input correct choice...(1-5)=")


       
"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""

def welcome():
    while True:
        print("\n",60*"=")
        print( "\t\tMAIN MENU:")
        print("\n",60*"=")
        print( "1.  Train Menu")
        print( "2.  Train Ticket Reservation")
        print( "3.  Show Reservation")
        print( "4.  Show All Reservation")
        print( "5.  Train Ticket cancellation")
        print( "6.  Show cancellation")
        print( "7.  Show All cancellation")
        print( "8.  Exit")
        ch=int(input("Enter Your Choice(1~4): "))
        if ch==1:
            train_menu()
        elif ch==2:
            reservation()
        elif ch==3:
            num=int(input("\n\nEnter PNR Number: "))
            display_reserv(num)
        elif ch==4:
            display_allReservation()
        elif ch==5:
            write_cancel()
    
        
        elif ch==6:
            num=int(input("\n\nEnter PNR Number: "))
            display_cancel(num)
        elif ch==7:
            display_allcancellation()
        elif ch==8:
            print("Program terminated sucessfully")
            print("-"*50)
            break
        else:
            print( "Input correct choice...(1-5)")
     

    

welcome()
