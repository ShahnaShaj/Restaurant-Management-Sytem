import datetime
import random
import pickle
import mysql.connector as sql
con=sql.connect(host="localhost",user="root",password="adis")
cur=con.cursor()
if con.is_connected():
    cur.execute("create database if not exists restaurant")
    cur.execute("use restaurant")
    cod="create table if not exists customers(name varchar(20),phone char(10),time varchar(10),dateofbooking varchar(15))"
    par="create table if not exists party(name varchar(20),phone char(10),time varchar(10),date varchar(15))"
    staff="create table if not exists staff(empid int primary key, name varchar(15), number varchar(10))"
    cur.execute(par)
    cur.execute(cod)
    cur.execute(staff)
    tht1='''
                                       THERE IS NO SINCERE LOVE THAN THE LOVE OF 
                                    ---------------------------------------------------
                                                     FOOD           
                                            ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht2='''
                                            LAUGHTER IS BRIGHTEST
                                        -----------------------------
                                       IN THE PLACE WHERE FOOD IS GOOD
                                            ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht3='''
                                    NOTHING CAN BRING PEOPLE TOGETHER LIKE
                                ----------------------------------------------
                                                GOOD FOOD
                                          ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂     
    '''
    tht4='''
                                    OUR SECRET INGREDIENT IS ALWAYS LOVE
                                        ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht5='''
                                            COUNT THE MEMORIES
                                    ----------------------------------------
                                            NOT THE CALORIES
                                          ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht6='''
                                        YOUR DIET IS A BANK ACCOUNT
                                    --------------------------------
                                GOOD FOOD CHOICES ARE GOOD INVESTMENTS
                             ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht7='''
                                        GOOD FOOD IS GOOD MOOD
                                      WAKE UP! IT'S FOOD O'CLOCK    
                                        ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂
    '''
    tht8='''
                                        PEOPLE WHO GIVE FOOD
                                    -----------------------------
                                     ARE THOSE WHO GIVE HEART
                                      ⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂'''
    th=(tht1,tht2,tht3,tht4,tht5,tht6,tht7,tht8)
    print("""
     ˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚
       _   _   _   _   _   _   _     _   _     _   _   _   _   _     _   _   _   _   _   _     _   _   _   _   _   _   _   _   _   _  
      / \ / \ / \ / \ / \ / \ / \   / \ / \   / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
     ( w | e | l | c | o | m | e ) ( t | o ) ( s | p | i | c | e ) ( e | m | p | i | r | e ) ( r | e | s | t | a | u | r | a | n | t )
      \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/   \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ """)

    choice=random.choice(th)
    print(choice)
    d=datetime.date.today()
    t=datetime.datetime.now()
    print(" ")
    print("	DATE:-",d.strftime("%A, %d %B %Y"))
    print(" ")
    print("	TIME:-",t.strftime("%H:%M:%S"))
    print("")
main='y'
while main=='yes' or main in 'Yy':
    print("""
                                ✧･ﾟ: *✧･ﾟ:*       ✧･ﾟ: *✧･ﾟ:*		✧･ﾟ: *✧･ﾟ:*	
                               *1.CUSTOMER*       * 2. STAFF  *		*3.EXIT    *
                                ✧･ﾟ: *✧･ﾟ:*       ✧･ﾟ: *✧･ﾟ:*		✧･ﾟ: *✧･ﾟ:*
""")
    e=int(input("꧁༺ SELECT ༻꧂"))
    if e==1:
        def menu():
            print("""
     ˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊
     
        I.STARTERS
            1. chicken lollipop  {20dhs}
            2. soup              
            3. salad             
        II. MAIN COURSE
            4. Biriyani          
            5. Noodles           
            6. Al Faham          {30dhs}
        III. DESSERTS
            7. Milkshake         
            8. Falooda           
            9. Fruit Salad       (15dhs)
            
    ˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊""")
        def order():
            menu()
            s=0
            ff={1:'chicken lollipop',2:'soup',3:'salad',4:'biriyani',5:'noodles',6:'al faham',7:'milkshake',8:'falooda',9:'fruit salad'}
            f={1:20,2:15,3:10,4:25,5:21,6:30,7:10,8:15,9:15}
            oh='y'
            p=[]
            while oh=='yes' or oh in 'Yy':
                l=[]
                item=int(input("What would you like to buy"))
                if item in f:
                    if item==2:
                        print("""
                               1.chicken soup    35dhs
                               2.vegetable soup  30dhs 
                               3.corn egg soup   25dhs 
                               4.mutton soup     35dhs """)
                        ta=int(input("CHOOSE"))
                        dic={1:35,2:30,3:25,4:35}
                        s=s+dic[ta]
                        l=[ff[item],dic[ta]]
                        p.append(l)
                    elif item==3:
                        print("""
                               1.green salad            10dhs
                               2.pasta salad            10dhs 
                               3.empire special salad   15dhs 
                               4.Broccoli salad         20dhs """)
                        qa=int(input("CHOOSE"))
                        ic={1:10,2:10,3:15,4:20}
                        s=s+ic[qa]
                        l=[ff[item],ic[qa]]
                        p.append(l)
                    elif item==4:
                        print("""
                               1.mutton biriyani            25dhs
                               2.chicken biriyani           25dhs 
                               3.beef biriyani              25dhs 
                               4.vegetable biriyani         20dhs """)
                        bir=int(input("CHOOSE"))
                        bic={1:25,2:25,3:25,4:20}
                        s=s+bic[bir]
                        l=[ff[item],bic[bir]]
                        p.append(l)
                    elif item==5:
                        print("""
                               1.schezwan chicken noodles  20 dhs
                               2.Hakka noodles             20dhs 
                               3.vegetable noodles         18dhs """)
                        noo=int(input("CHOOSE"))
                        ils={1:20,2:20,3:18}
                        s=s+ils[noo]
                        l=[ff[item],ils[noo]]
                        p.append(l)
                    elif item==7:
                        print("""
                               1.chocolate               10dhs
                               2.oreo                    10dhs 
                               3.strawberry              10dhs 
                               4.empire special          15dhs """)
                        milk=int(input("CHOOSE"))
                        shk={1:10,2:10,3:10,4:15}
                        s=s+shk[milk]
                        l=[ff[item],shk[milk]]
                        p.append(l)
                    elif item==8:
                        print("""
                               1.royal falooda      20dhs     
                               2.rose falooda       20dhs 
                               3.mango falooda      20dhs 
                               4.kulfi falooda      15dhs """)
                        fal=int(input("CHOOSE"))
                        da={1:10,2:10,3:10,4:15}
                        s=s+da[fal]
                        l=[ff[item],da[fal]]
                        p.append(l)    
                    else:    
                        s=s+f[item]
                        l=[ff[item],f[item]]
                        p.append(l)
                    oh=input("Would like to order anything else?")
                else:
                    print("Sorry! Item not available")
            print("-----------------\t")
            print("    BILL\t")        
            for i in range(len(p)):
                print(p[i])
            print("Total=",s)    
            print("-----------------\t")
            print("""
                ˗ˏˋ1.´ˎ˗COUPON CODES         ˗ˏˋ2.´ˎ˗EXIT
                """)
            ty=input("Looking for offers?[1/2]")
            tr='y'
            while tr in'y':
                if ty=='1' or ty in 'Yy':
                    print("")
                    print("COUPONS OF THE DAY!")
                    print("50% off on orders above 50dhs with code [FOOD50]")
                    print("Flat 10dhs off on orders at or above 25dhs with code[FLAT10]")
                    print("30% off on orders at or above 40dhs with code [MY30]")
                    print("")
                    cou=input("˚ · .ENTER COUPON CODE˚ · .")
                    if cou.lower()=='food50' or cou.lower()=='[food50]':
                        if s>=50:
                            s=s/2
                            print("")
                            print("Coupon redeemed")
                            print("Please pay",s,"dhs")
                            print("")
                            break
                        else:
                            print("")
                            print("Code valid for orders at or above 50dhs only")
                            ty='y'
                            
                    elif cou.lower()=='flat10' or cou.lower()=='[flat10]':
                        if s>=25:
                            s=s-10
                            print("")
                            print("Coupon redeemed")
                            print("Please pay",s,"dhs")
                            print("")
                            break
                        else:
                            print("")
                            print("Code valid for orders at or above 25dhs only")
                            ty='y'
                            
                    elif cou.lower()=='my30' or cou.lower()=='[my30]':
                        if s>=40:
                            p=(30/100)*s
                            s=s-p
                            print("")
                            print("Coupon redeemed")
                            print("Please pay",s,"dhs")
                            print("")
                            break
                        else:
                            print("")
                            print("Code valid for orders at or above 40dhs only")
                            ty='y'
                            
                    else:
                        print("Code invalid")
                else:
                    print("Please pay",s,'dhs')
                    break
                tr=input("TRY AGAIN? ")
            print("THANK YOU")
        def book():
            ok='y'
            while ok in 'Yy': 
                print("""
                     ╔══ ❀•°❀°•❀ ══╗        ╔══ ❀•°❀°•❀ ══╗        ╔══ ❀•°❀°•❀ ══╗
                      1.SHOW BOOKINGS         2. BOOK A TABLE          	3.CANCEL BOOKING 
                     ╚══ ❀•°❀°•❀ ══╝        ╚══ ❀•°❀°•❀ ══╝        ╚══ ❀•°❀°•❀ ══╝
        """)
                bo=int(input("Select an option"))
                def display():
                    cur.execute("Select name,time,dateofbooking from customers")
                    d=cur.fetchall()
                    if d!=[]:
                        for i in d:
                            print(i)
                    else:
                        print("No Bookings yet!")
                    con.commit()

                def insert():
                    a=input("Enter name")
                    while True:
                        b=input("Enter phone")
                        if len(b)==10:
                            break
                        else:
                            print("10 digits required")
                    cc=input("Enter time")
                    d=input("Enter date of booking")
                    sql="insert into customers(name,phone,time,dateofbooking)values('{}','{}','{}','{}')".format(a,b,cc,d)
                    cur.execute(sql)
                    print ("Table booked successfully")
                    con.commit()
                    
                def dele():
                    n=input("Enter your name")
                    p=input("Enter your phone number")
                    cur.execute("Select * from customers")
                    d=cur.fetchall()
                    for i in d:
                        if p in i:
                            print("Are you sure you want to cancel the booking?")
                            su=input("Y/N")
                            if su in "Yy":
                                cur.execute("delete from customers where name='%s'and phone='%s'"%(n,p))
                                print("Your booking is cancelled")
                                print("Thank you")
                                con.commit()
                                break
                            else:
                                pass
                        else:
                            print("Order not found. Try again with the correct credentials")
                            break
                    
                if bo==1:
                    display()
                elif bo==2:
                    insert()
                elif bo==3:
                    dele()
                    con.commit()
                ok=input("RETURN TO BOOKING MENU?[Y/N] ")    
        def buffet():
            print("""
              *********************        *********************      *********************   
               1.INDIAN                      2.CONTINENTAL              3.ORIENTAL
               
                 Chicken biriyani            Osso Bucco                 Noodles 
                 Curd Rice                   Lobster Thermidor          Kimchi
                 Paratha/chappathi           Roast chicken              Sushi
                 Masala Dosa                 Filet mignon
                 Aloo gobi                   
                 Chana masala                Pizza
                 
              *********************        *********************      *********************
                                   -----------------------------------
                                           $ per adult: 85
                                           $ per child: 50
                                   -----------------------------------        
  """)
            a=int(input("SELECT YOUR CUISINE"))
            b=int(input("Enter the number of adults:"))
            c=int(input("Enter the number of children:"))
            t=(b*85)+(c*50)
            print("Please pay",t,"dirhams")
                  
        def party():
            qw='y'
            while qw in 'Yy':
                print("""
                 ^^^^^^^^^^^^^^^        ^^^^^^^^^^^^^^^      ^^^^^^^^^^^^^^^^
                 1.Show bookings         2.Book a hall       3.Cancel booking
                 ^^^^^^^^^^^^^^^        ^^^^^^^^^^^^^^^      ^^^^^^^^^^^^^^^^
                         """)
                sel=int(input("SELECT: "))
                def HALL():
                    nn=input("Enter name")
                    while True:
                            pp=input("Enter phone number")
                            if len(pp)==10:
                                break
                            else:
                                print("10 digits required")
                    tt=input("Enter time")
                    dd=input("Enter date")
                    sql="insert into party(name,phone,time,date)values('{}','{}','{}','{}')".format(nn,pp,tt,dd)
                    cur.execute(sql)
                    con.commit()
                    print("Hall booked successfully")

                def SHOW():
                    cur.execute("Select name,time,date from party")
                    d=cur.fetchall()
                    if d!=[]:
                        for i in d:
                            print(i)
                            
                    else:
                        print("No bookings yet!")
                    con.commit()
                        
                def CANCEL():
                    ph=input("Enter your phone number ")
                    cur.execute("Select * from party where phone='%s'"%(ph))
                    d=cur.fetchall()
                    if d!=[]:    
                        print("Are you sure you want to cancel the booking?")
                        su=input("Y/N")
                        if su in "Yy":
                            can="delete from party where phone='%s'"%(ph)
                            cur.execute(can)
                            print("Booking cancelled")
                        else:
                            pass
                    else:
                        print("BOOKING NOT FOUND")
                        pass
                cur.execute("Select * from party")
                d=cur.fetchall()
                co=len(d)    
                if sel==1:
                    SHOW()
                elif sel==2:
                    if co<5:
                        HALL()
                    else:
                        print("Sorry! All five halls are booked")
                elif sel==3:
                    CANCEL()
                else:
                    print("INVALID OPTION")
                    con.commit()
                qw=input("RETURN TO PARTY MENU?[Y/N] ")    
        def Us():
            f=open("us.dat","wb")
            pickle.dump("""
                    Since our modest beginnings in 2005 with a little space in Toronto’s stylish Yorkville locale, ‘Spice Empire’'s
        development has been enlivened with the energy to cook and serve solid, Indian-roused takeout food.
        
                       Spire Empire is situated in Salam Street,opposite Al Mubadalah.
            Extraordinary administration and a fun vibe keep local people returning and guests raving.
            
                                    CONTACT US:0569510657
                                    EMAIL: salamempirelove@gmail.com""",f)
            f=open("us.dat","rb")
            try:
                while True:
                    l=pickle.load(f)
                    print(l)
            except EOFError:
                pass
            f.close()
        def feed():
            show='y'
            while show in 'yY':
                p=open("FEED.dat",'ab')
                print(" *1.SHOW PUBLIC REVIEW*     *2.POST A REVIEW")
                sel=int(input("SELECT::"))
                if sel==1:
                    p=open("FEED.dat",'rb')
                    try:
                        while True:
                            print("***********************")
                            l=pickle.load(p)
                            print(l)
                    except EOFError:
                        pass
                elif sel==2:    
                    print(":1.POST PUBLICLY:            :2.PRIVATE COMMENNT:")
                    t=int(input("HOW?! "))
                    if t==1:
                        p=open("FEED.dat",'ab')
                        te=input("Enter your comment")
                        pickle.dump(te,p)
                        print("Comment added successfully")
                        print()
                    elif t==2:
                        fe=input("Do mention your valuable suggestions")
                        while True:
                            rate=int(input("Rate us on 5"))
                            if rate<=5:
                                print("Thank you")
                                break
                            else:
                                print("Please rate between 0-5")
                    else:
                        print("INVALID CHOICE")
                show=input("RETURN TO FEEDBACK?   ")                
        cho='y'
        while cho in 'yY' or cho=='yes':
            print("""
               ━◦○◦━◦○◦━━◦○◦━◦○◦━
                  1.Show Menu
                  2.Order Food
                  3.Booking
                  4.Buffet
                  5.Party hall
                  6.Feedback
                  7.About Us
                  8.Return
               ━◦○◦━◦○◦━━◦○◦━◦○◦━   """)
            ur=int(input("Enter a choice"))
            if ur==1:
                menu()
            elif ur==2:
                order()
            elif ur==3:
                book()
            elif ur==4:
                buffet()
            elif ur==5:
                party()
            elif ur==6:
                feed()
            elif ur==7:
                Us()
            elif ur==8:
                break
            else:
                print("INVALID OPTION")
            cho=input("Would you like to do another operation")
    elif e==3:
        print("∘°∘♡∘°∘ THANK YOU! ∘°∘♡∘°∘")
        print("DO VISIT US AGAIN")
        break

    elif e==2:
        kh='y'
        while kh=='yes' or kh in 'Yy':
            print("""
                ━◦○◦━◦○◦━━◦○◦━◦○◦━━◦○◦━◦○◦━
                   A. STAFF DETAILS
                   B. INSERT A RECORD
                   C. MODIFY YOUR RECORD
                   D. DELETE YOUR RECORD
                   E. SEARCH A STAFF
                   F. LEAVE APPLICATION
                   G. COMPLAINTS/SUGGESTIONS
                   H. EXIT
                ━◦○◦━◦○◦━━◦○◦━◦○◦━━◦○◦━◦○◦━   
                   """)
            lo=input("What do you want?")
            def DETAILS():
                cur.execute("select name,number from staff")
                d=cur.fetchall()
                if d!=[]:
                    for i in d:
                        print(i)
                    con.commit()
                else:
                    print("The list is empty")
                
            def RECORD():
                i=int(input("Enter the employee id"))
                n=input("Enter name")
                while True:
                    p=input("Enter phone number")
                    if len(p)==10:
                        break
                    else:
                        print("10 digits required")
                sql="insert into staff(empid,name,number)values({},'{}','{}')".format(i,n,p)
                cur.execute(sql)
                print("Record inserted successfully")
                con.commit()
                
            def MODIFY():
                print("[name]     [phone number]")
                mod=input("What do you want to modify?")
                if mod=='name' or mod=='1':
                    a=input("Enter your empid")
                    cur.execute("select * from staff where empid=%s"%(a))
                    d=cur.fetchall()
                    if d!=[]:
                        p=input("Enter new name")
                        q="update staff set name='%s' where empid=%s"%(p,a)
                        cur.execute(q)
                        print ("RECORD UPDATED SUCCESSFULLY")
                        con.commit()
                    else:
                        print("ID NOT FOUND")
                        
                elif mod=='phone number' or mod=='number' or mod=='2':
                    a=input("Enter your empid")
                    while True:
                        p=input("Enter new number")
                        if len(p)==10:
                            break
                        else:
                            print("10 digits required")
                    cur.execute("select * from staff where empid=%s"%(a))
                    d=cur.fetchall()
                    if d!=[]:
                        q="update staff set number='%s' where empid=%s"%(p,a)
                        cur.execute(q)
                        print ("RECORD UPDATED SUCCESSFULLY")
                        con.commit()
                    else:
                        print("ID NOT FOUND")
                else:
                    print("INVALID ENTRY")
           
            def DELETE():
                a=int(input("Enter empid to be deleted"))
                n=input("Enter the name to be deleted")
                cur.execute("Select * from staff")
                d=cur.fetchall()
                for i in d:
                    if a in i and n in i:
                        sql="delete from staff where empid=%s and name='%s'"%(a,n)
                        cur.execute(sql)
                        print("RECORD DELETED SUCCESSFULLY")
                        con.commit()
                        break
                    else:
                        print("RECORD NOT FOUND")
                        print("TRY AGIAN WITH THE CORRECT CREDENTIALS")
                        break

            def SEARCH():
                po='y'
                while po in "Yy":
                    print("""
                    ◈━◈━◈━◈━◈━◈     	◈━◈━◈━◈━◈━◈━◈       	◈━◈━◈━◈━◈━◈━◈━◈
                    1)search by id      2)search by name    	3)search by number
                    ◈━◈━◈━◈━◈━◈     	◈━◈━◈━◈━◈━◈━◈       	◈━◈━◈━◈━◈━◈━◈━◈
""")
                    ser=int(input("How do you want to search?"))
                    try:
                        if ser==1:
                            i=int(input("Enter the id to be searched"))
                            cur.execute("select * from staff where empid=%s"%i)
                            d=cur.fetchall()
                            if d==[]:
                                print("RECORD NOT FOUND")
                            else:    
                                for i in d:
                                    print("RECORD FOUND!")
                                    print(i)
                        elif ser==2:
                            n=input("Enter the name to be searched")
                            cur.execute("select * from staff where name='%s'"%n)
                            d=cur.fetchall()
                            if d==[]:
                                print("RECORD NOT FOUND")
                            else: 
                                for i in d:
                                    print("RECORD FOUND!")
                                    print(i)
                            con.commit()
                        elif ser==3:
                            no=input("Enter the number to be searched")
                            cur.execute("select * from staff where number='%s'"%no)
                            d=cur.fetchall()
                            if d==[]:
                                print("RECORD NOT FOUND")
                            else: 
                                for i in d:
                                    print("RECORD FOUND!")
                                    print(i)
                        else:
                            print("INVALID OPTION")
                    except:
                        print("Data not found")
                    po=input("CONTINUE SEARCHING?[Y/N] ")   
            
            def LEAVE():
                nam=input("Enter your name")
                ph=input("Enter phone number")
                cur.execute("select * from staff where name='%s' and number='%s'"%(nam,ph))
                d=cur.fetchall()
                if d!=[]:
                    lev=input("Enter the date of leavee")
                    rea=input("Enter the reason")
                    print("Application sent")
                    print("Please wait until your leave is approved")
                    pass
                else:
                    print("EMPLOYEE NOT FOUND! ")
                    print("PLEASE TRY AGAIN")
            def COMPLAIN():
                nam=input("Enter your name")
                cur.execute("select * from staff where name='%s'"%(nam))
                d=cur.fetchall()
                if d!=[]: 
                    com=input("Let us know your thoughts ")
                    print("")
                    print("Thank you for your valuable opinion")
                    print("We will look into the matter and get back to you")
                else:
                    print("EMPLOYEE NOT FOUND!")
                    print("PLEASE TRY AGAIN")
            if lo=='1' or lo in'Aa':
                DETAILS()
                break
            else:    
                pas=input("Enter the staff password")
                if pas=='adis':
                    
                    if lo=='2' or lo in'Bb':
                        RECORD()
                    elif lo=='3' or lo in 'Cc':
                        MODIFY()
                    elif lo=='4' or lo in 'Dd':
                        DELETE()
                    elif lo=='5' or lo in 'Ee':
                        SEARCH()
                    elif lo=='6' or lo in 'Ff':
                        LEAVE()
                    elif lo=='7' or lo in 'Gg':
                        COMPLAIN()
                    elif lo=='8' or lo in 'Hh':
                        print("Thank you")
                        break
                    else:
                        print("Invalid option")
                    kh=input("Do you want to go to the staff menu?")
                else:
                    print("INCORRECT PASSWORD. ACCESS DENIED")
                    break
    main=input("Do you want to return to main menu?")
    print("")
    print("∘°∘♡∘°∘ THANK YOU! ∘°∘♡∘°∘")
    print("DO VISIT US AGAIN")

            
        
    
        
        
    
              
              
    
        
    
