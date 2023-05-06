import sys
import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_simulator_database_script',
         user='SrdPa',
         password='Ratgai#1!',
         autocommit=True
         )
distance1 = int(input("Enter the distance (Between 400-900): "))
direction1 = str(input("Enter the direction: "))

#INDIA PHASE 1
if distance1 in range(650,750):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction1 == "+15D":
    print("You are at Moscow airport")
else:
    sys.exit("☠GAME OVER!☠")
#INDIA PHASE 2

distance2 = int(input("Enter the distance (Between 800-1100: "))
direction2 = str(input("Enter the direction: "))

if distance2 in range(900,1000):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction2 == "-5D":
    print("You are at Izhevsk airport (Above kazakhstan")
else:
    sys.exit("☠GAME OVER!☠")

#INDIA PHASE 3

distance3 = int(input("Enter the distance (Between 500-2200: "))
direction3 = str(input("Enter the direction: "))

if distance3 in range(600,2000):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction3 == "+45S":
    print("You are in kazakhstan airport")
else:
    sys.exit("☠GAME OVER!☠")

#PHASE 4

distance4 = int(input("Enter the distance (Between 1850-2200: "))
direction4 = str(input("Enter the direction: "))

if distance4 in range(1950,2050):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction4 == "+15S":
    print("You are about to reach India's border")
    print("✪✪✪CONGRATULATIONS YOU REACHED INDIA!✪✪✪")
    sys.exit("press run to play again")
else:
    sys.exit("☠GAME OVER!☠")




#GERMANY VIA ICELAND
distance5 = int(input("Enter the distance (Between 300-500): "))
direction5 = str(input("Enter the direction: "))

#GERMANY VIA ICELAND PHASE 1
if distance5 in range(350,450):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction5 == "0A":
    print("You are at Stockholm airport")
else:
    sys.exit("☠GAME OVER!☠")


#GERMANY VIA ICELAND PHASE 2

distance6 = int(input("Enter the distance (Between 700-800: "))
direction6 = str(input("Enter the direction: "))

if distance6 in range(680,780):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction6 == "+80A":
    print("You are at Ålesund airport")
else:
    sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 3

distance7 = int(input("Enter the distance (Between 300-500: "))
direction7 = str(input("Enter the direction: "))

if distance7 in range(350,450):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction7 == "+85A":
    print("You are in Reykjavik airport")
else:
    sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 4

distance8 = int(input("Enter the distance (Between 1400-1600: "))
direction8 = str(input("Enter the direction: "))

if distance8 in range(1450-1550):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction8 == "+30S":
    print("You are in Dublin airport (Ireland)")
else:
    sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 5

distance7 = int(input("Enter the distance (Between 350-550: "))
direction7 = str(input("Enter the direction: "))

if distance7 in range(400-500):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction7 == "+85S":
    print("You are in Heathrow airport")
else:
    sys.exit("☠GAME OVER!☠")

#GERMANY VIA ICELAND PHASE 6

distance8 = int(input("Enter the distance (Between 550-750: "))
direction8 = str(input("Enter the direction: "))

if distance8 in range(600-700):
    print("Your are at heading the correct direction")
else:
    sys.exit("☠GAME OVER☠!")
if direction8 == "+80S":
    print("You are about to reach Frankfurt airport")
    print("✪✪✪CONGRATULATIONS YOU REACHED GERMANY!✪✪✪")
    sys.exit("press run to play again")
else:
    sys.exit("☠GAME OVER!☠")



#ALASKA
direction9 = str(input("Enter the direction: "))
if direction9 == "A":
    print("You flew across sweden and norway, you are in Iceland (Reykjavik airport)")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 2
direction10 = str(input("Enter the direction: "))
if direction10 == "A":
    print("You are in Greenland")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 3
direction11 = str(input("Enter the direction: "))
if direction11 == "S":
    print("You are in Thunder Bay airport(Ontario, Canada)")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 4
direction12 = str(input("You flying in inside Canada's provinces now enter direction: "))
if direction12 == "A":
    print("You are in the province of Manitoba")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 5
direction13 = str(input("Enter the direction: "))
if direction13 == "A":
    print("You are in the province of Saskatchewan")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 6
direction14 = str(input("Enter the direction: "))
if direction14 == "W":
    print("You are in the province of Northwest Territories ")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 7
direction15 = str(input("Enter the direction: "))
if direction15 == "A":
    print("You are in the province of Yukon (Canada)")
else:
    sys.exit("☠GAME OVER!☠")

# ALASKA PHASE 8
direction16 = str(input("Enter the direction: "))
if direction16 == "A":
    print("✪✪✪CONGRATULATIONS YOU REACHED ALASKA!✪✪✪")
    sys.exit("press run to play again")
else:
    sys.exit("☠GAME OVER!☠")







