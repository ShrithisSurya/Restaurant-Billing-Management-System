from tkinter import*
import datetime                   # import datetime as dt
import random
import csv
import os.path
from General_concept.GUI_Exercise.Restaurant_Db import insertbillingdetails

root = Tk()
root.geometry("1600x700")
#root.resizable(0,0)
root.title("Restaurant Management System")
root.config(background="Steel Blue")
Tops = Frame(root,width = 1600,height=50,relief=SUNKEN,background="Steel Blue")
Tops.pack(side=TOP)
Bottoms = Frame(root,width = 1600,height=50,relief=SUNKEN,background="Steel Blue")
Bottoms.pack(side=BOTTOM,)          # always in caps
f1 = Frame(root,width = 1200,height=700,relief=SUNKEN,background="Steel blue")
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
currenttime=datetime.datetime.now()                   #dt.date.today() ,,,,,dt.datetime.now()
print(currenttime)
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Billing Management System By Shrithis Surya P",fg="Black",background="steelblue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=currenttime,fg="Black",background="Steel blue",anchor=W)
lblinfo.grid(row=1,column=0)
lblinfo = Label(Bottoms, font=( 'aria' ,30, 'bold' ),text="contact no:+91 6379481496",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=1,column=4)
lblinfo = Label(Bottoms, font=( 'aria' ,20, ),text="email:shrithis2002@gmail.com",fg="Black",background="Steel Blue",anchor=W)
lblinfo.grid(row=2,column=4)
lblinfo=Label(Bottoms,font=('Times New Roman',30,'bold'),text="Person Name : P.Shrithis Surya",fg="Black",background="Steel Blue",anchor=W)
lblinfo.grid(row=0,column=4)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="powder blue",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator   # global used to save previous calc. step by step will proceed
    operator=operator + str(numbers)
    print(operator)
    text_Input.set(operator)
btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
btnc.grid(row=5,column=1)

def eqals():
    global operator
    sumup=str(eval(operator))               # evaluate

    text_Input.set(sumup)
    operator = ""

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="powder blue")#, command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="powder blue")#, command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="-By Aravind",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)
#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No :",fg="Black",background="Steel Blue",bd=10,)
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)
lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')        # justify right  means right la irunthu  type aagum
txtLargefries.grid(row=2,column=1)                                                # bd = border  box border


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total :",fg="Black",background="Steel Blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)
#-----------------------------------------buttons------------------------------------------



def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    # Retrieve the values from input fields
    cof = float(Fries.get() or 0)  # Default to 0 if input is empty
    colfries = float(Largefries.get() or 0)
    cob = float(Burger.get() or 0)
    cofi = float(Filet.get() or 0)
    cochee = float(Cheese_burger.get() or 0)
    codr = float(Drinks.get() or 0)

    # Calculate costs
    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 50
    costofdrinks = codr * 35

    # Calculate totals
    total_meal_cost = costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks
    PayTax = total_meal_cost * 0.33
    Ser_Charge = total_meal_cost / 99

    # Calculate overall cost
    OverAllCost = PayTax + total_meal_cost + Ser_Charge

    # Update displayed values (use str.format for formatting)
    Service_Charge.set("Rs. {:.2f}".format(Ser_Charge))
    Tax.set("Rs. {:.2f}".format(PayTax))
    Subtotal.set("Rs. {:.2f}".format(total_meal_cost))
    Total.set("Rs. {:.2f}".format(OverAllCost))

    # Insert billing details into the database
    insertbillingdetails(
        randomRef,
        costoffries,
        costoflargefries,
        costofburger,
        costoffilet,
        costofcheeseburger,
        costofdrinks,
        total_meal_cost,  # Pass the total meal cost here
        Ser_Charge,  # Pass service charge as float
        PayTax,  # Pass tax as float
        total_meal_cost,  # Pass subtotal (the same as total meal cost)
        OverAllCost  # Pass overall cost
    )



    fileexist=os.path.isfile('restaurant.csv')
    if fileexist:
        with open('restaurant.csv','a',newline='')as file:
            writer=csv.writer(file)
            writer.writerow([randomRef, cof, colfries, cob, cofi, cochee, codr, costoffries, costoflargefries, costofburger,
                 costoffilet, costofcheeseburger, costofdrinks,total_meal_cost, PayTax, Total, Ser_Charge,
                 OverAllCost,PayTax])
    else:
        with open('restaurant.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['randomRef', 'cof', 'colfries', 'cob', 'cofi', 'cochee', 'codr', 'costoffries', 'costoflargefries', 'costofburger',
                 'costoffilet', 'costofcheeseburger', 'costofdrinks', 'costofmeal', 'PayTax', 'Totalcost', 'Ser_Charge',
                 'OverAllCost', 'PaidTax'])
            writer.writerow(
                [randomRef, cof, colfries, cob, cofi, cochee, codr, costoffries, costoflargefries, costofburger,
                 costoffilet, costofcheeseburger, costofdrinks,total_meal_cost, PayTax, Total, Ser_Charge,
                 OverAllCost,PayTax])

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

def reset():
    rand.set('')                                  #('') means blank
    Fries.set('')
    Largefries.set('')
    Burger.set('')
    Filet.set('')
    Subtotal.set('')
    Total.set('')
    Service_Charge.set('')
    Drinks.set('')
    Tax.set('')
    cost.set('')
    Cheese_burger.set('')

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

def qexit():
    root.destroy()
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()
btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)


root.mainloop()



'''bd border 
justify
insertwidth , box '''