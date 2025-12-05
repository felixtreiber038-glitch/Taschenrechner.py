portions = input("Für wie viele Menschen: ")

for x in [str(int(portions) * 2) +' Eier',str(int(portions) * 200) +'g Mehl',str(int(portions) * 100) +'g Banane']:
    print(x)

input("Drücke eine Taste um das Program zu Beenden:")