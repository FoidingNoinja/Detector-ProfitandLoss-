Cprice = float(input("Enter the Cost Price of the product : "))
Sprice = float(input("Enter the Selling Price of the product : "))

def Profit_Loss() :

    Profit = Sprice - Cprice
    Loss = Cprice - Sprice

    if Sprice > Cprice :
        print(f"The Profit is : {Profit}")
    elif Cprice > Sprice : 
        print(f"The Loss is : {Loss}")
    elif Cprice == Sprice :
        print("There was neither Profit nor Loss")

Profit_Loss()
