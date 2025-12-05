
gehaltProStunde = input("Bitte gebe deinen stundenlohn ein: ")

gehaltAmTag = 8 * float(gehaltProStunde)
gehaltProWoche = gehaltAmTag * 5
gehaltProMonat = (gehaltProWoche * 4) + 2
gehaltProJahr = gehaltProMonat * 12



print("Du wirst " + str(gehaltProStunde) + "€ pro stunde verdienen!")
print("Du wirst " + str(gehaltAmTag) + "€ am tag verdienen!")
print("Du wirst " + str(gehaltProWoche) + "€ pro Woche verdienen!")
print("Du wirst " + str(gehaltProMonat) + "€ pro Monat verdienen!")
print("Du wirst " + str(gehaltProJahr) + "€ pro Jahr verdienen!")

input("")