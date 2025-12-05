print("Welches Rezept:")
print("(1)Pfannkuchen")
print("(2)Waffeln")
print("(3)Käsekuchen")
auswahl = input("Welches Rezept willst du auswählen:")
print("")

if  auswahl == "1":
    print("Pfannkuchen")
    print("")

    portions_pfannkuchen = input("Für wie viele Menschen:" )
    print("")

    for x in [str(int(portions_pfannkuchen) * 2) + " Eier",
          str(int(portions_pfannkuchen) * 200) + "g Mehl",
          str(int(portions_pfannkuchen) * 100) + "g Zucker"]:
     print(x)


elif auswahl == "2":
    print("Waffeln")
    print("")

    portions_waffeln = input("Für wie viele Menschen:")
    print("")

    for y in [str(int(portions_waffeln) * 1) + " Eier",
         str(int(portions_waffeln) * 250) + "g Mehl",
         str(int(portions_waffeln) * 60) + "g Zucker"]:
       print(y)


elif auswahl == "3":
    print("Käsekuchen")
    print("")

    portions_käsekuchen = input("Für wie viele Menschen:")
    print("")

    for y in [str(int(portions_käsekuchen) * 50) + "g Käse",
              str(int(portions_käsekuchen) * 250) + "g Mehl",
              str(int(portions_käsekuchen) * 100) + "g Zucker"]:
        print(y)
print("")
input("Belibige Taste drücken um zu Beenden:")