import  mysql.connector
config= {
    'user': 'root',
    'password':'#Sv0912',
    'host':'localhost',
    'database':'restauarant_billing'

}
cnx=mysql.connector.connect(**config)
cursor=cnx.cursor()

def insertbillingdetails( OrderNo , FriesMeal,LunchMeal,BurgerMeal,PizzaMeal,CheeseBurger,Drinks,Cost ,ServiceCharge,Tax ,SubTotal , Total ):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    sql=f"insert into billing values ({OrderNo},{FriesMeal},{LunchMeal},{BurgerMeal},{PizzaMeal},{CheeseBurger},{Drinks},{Cost},{ServiceCharge},{Tax},{SubTotal},{Total})"
    print(sql)
    cursor.execute(sql)
    cnx.commit()

# ord=int(input("Enter your order"))
# fries=int(input("Enter your fries"))
# lunch=int(input("Enter your lunchmeal"))
# burger=int(input("Enter your burger"))
# pizza=int(input("Enter your pizza"))
# cheepizza=int(input("Enter your ChessePizza"))
# drinks=int(input("Enter your drinks"))

# insertbillingdetails(OrderNo , FriesMeal,LunchMeal,BurgerMeal,PizzaMeal,CheeseBurger,Drinks,Cost ,ServiceCharge,Tax ,SubTotal , Total )
