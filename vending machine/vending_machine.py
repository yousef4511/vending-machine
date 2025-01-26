#creating a vending machine

print("                     Hello          ")
print("           WELCOME TO VENDING MACHINE")

#codes of the items in the shop
items={
"1111":"Oreo",
"2222":"Kitkat",
"3333":"Mars",
"4444":"Twix",
"5555":"Bounty",
"6666":"Mirinda",
"7777":"Fanta",
"8888":"Pepsi",
"9999":"Water",
"1222":"Redbull",
"1333":"Doritos",
"1444":"Snickers",
"1555":"Chokichoki",
"1666":"Hershys",
"1777":"Milka", 
}

print("                MENU OF snackshop                  ")
print("**************************************************************************************")
print("1.Oreo                                 AED 7, *Code:1111,  *  Stock:30")
print("2.kitkat                               AED 7, *code:2222,  *  stock:20")
print("3.Mars                                 AED 10,*Code:3333,  *  Stock:50")
print("4.Twix                                 AED 10,*Code:4444,  *  Stock:10")
print("5.Bounty                               AED 9, *Code:7777,  *  Stock:30")
print("6.Doritos                              AED 7, *Code:1333,  *  Stock:80")
print("7.Snickers                             AED 10,*Code:1444,  *  Stock:10")
print("8.Chokichoki                           AED 7, *Code:1555,  *  Stock:20")
print("9.Hershys                              AED 10,*Code:1666,  *  Stock:20")
print("10.Milka                               AED 10,*Code:1777,  *  Stock:60")
print("                  ...MENU OF DRINKS...              ")
print("11.Mirinda                           1  AED 10,*Code:6666,  *  Stock:80")
print("12.Fanta                               AED 10,*Code:7777,  *  Stock:10")
print("13.Pepsi                               AED 10,*Code:8888,  *  Stock:85")
print("14.Water                               AED 5,*Code:9999,  *  Stock:45")
print("15.Redbull                             AED 10,*Code:1222,  *  Stock:15")
print("***************************************************************************************")


#Price of items in the shop
Oreo=7
Kitkat=7
Mars=10
Twix=10
Bounty=9
Mirinda=10
Fanta=10
Pepsi=10
water=5
Redbull=10
Doritos=7
Snickers=10
Chokichoki=5
Hershys=10
Milka=10

# check stock
stock=3000
if stock > 0:
    print("________")
    print("We have snacks and beverages in stock. Please make your selection.")
    print("_________")


#This is for Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

# Enter the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money"))



#Choice for Additional Item
choice = {
   '1': 'yes' ,
   '2': 'no'
}
choice=input('Snackers and Drinkers would like to suggest you to have some chocolate? (ok/no):')
if choice== 'ok':
   print("...............................")
   print("Thankyou for your Selection")
elif choice== 'no':
   print("Thankyou for your Selection")

   #Calculating and Returning the Correct Change Of Oreo
   if items_code=='1111':
      if money >= Oreo:
         money=money-Oreo 

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Kitkat
   if items_code=='2222':
      if money >= Kitkat:
         money=money-Kitkat

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Mars
   if items_code=='3333':
      if money >= Mars:
         money=money-Mars

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Twix
   if items_code=='4444':
      if money >= Twix:
         money=money-Twix

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Bounty
   if items_code=='5555':
      if money >= Bounty:
         money=money-Bounty

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Mirinda
   if items_code=='6666':
      if money >= Mirinda:
         money=money-Mirinda

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Fanta
   if items_code=='7777':
      if money >= Fanta:
         money=money-Fanta
          
         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Pepsi
   if items_code=='8888':
      if money >= Pepsi:
         money=money-Pepsi

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of water
   if items_code=='9999':
      if money >= water:
         money=money-water

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Redbull
   if items_code=='1222':
      if money >= Redbull:
         money=money-Redbull

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Doritos
   if items_code=='1333':
      if money >= Doritos:
         money=money-Doritos

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Snickers
   if items_code=='1444':
      if money >= Snickers:
         money=money-Snickers

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Chokichoki
   if items_code=='1555':
      if money >= Chokichoki:
         money=money-Chokichoki

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Hershys
   if items_code=='1666':
      if money >= Hershys:
         money=money-Hershys

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")

         



         #Calculating and Returning the Correct Change Of Milka
   if items_code=='1777':
      if money >= Milka:
         money=money-Milka

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")






