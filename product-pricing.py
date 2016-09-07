#print(900 * 2 * 1.25 + 100 * 1.06)

# robot = {"price": 900, "count": 2, "tax":1.25}
# #här har jag använt en dictionary för att samla all info om produkten robot.

# book = {"price":100, "count":1, "tax": 1.06}

# print(robot["price"]*robot["count"]*robot["tax"]+ book["price"]*book["count"]*book["tax"])
#för att använda värdena ur min dictionary skriver jag så här: 
#jag åberopar listan (t.ex. robot9 genom att inleda med dictionaryns namn.
#sedan väljer jag värden ur listan genom tt skriva dem inom hakparenteser och citattecken. 


#skriv om med klass
# class Product:
# 	price = 0
# 	count = 1
# 	tax = 1
	#det här är exempel på en klass

#obs, det är viktigt att följande definitioner av produktens värden inte ligger indragna under klassen. 
# robot = Product()
# robot.price = 900
# robot.count = 2
# robot.tax = 1.25

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

	#för att printa och använda klasserna skriver jag så här:

#print (robot.price * robot.count * robot.tax + book.price * book.count * book.tax)

#skriv om med klass OCH metod
class Product:
	price = 0
	count = 1
	tax = 1

	def price_with_tax(self):
		return self.price * self.count * self.tax 

robot = Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25

book = Product()
book.price = 100
book.count = 1
book.tax = 1.06

#här lägger jag till en metod (med def) vilket är en funktion inuti en klass
#det metoden gör är att räkna ut priset med skatt för varje produkt. 


print(book.price_with_tax()+robot.price_with_tax())
#när jag anropar metoder måste jag avsluta med en parentes (ibland tom)
#det gör jag för att visa att det är ett metodanrop






