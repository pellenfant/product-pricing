robot = {"price": 900, "count": 2, "tax":1.25}
#här har jag använt en dictionary för att samla all info om produkten robot.

book = {"price":100, "count":1, "tax": 1.06}

print(robot["price"]*robot["count"]*robot["tax"]+ book["price"]*book["count"]*book["tax"])

#för att använda värdena ur min dictionary skriver jag så här: 
#jag åberopar listan (t.ex. robot9 genom att inleda med dictionaryns namn.
#sedan väljer jag värden ur listan genom tt skriva dem inom hakparenteser och citattecken. 
