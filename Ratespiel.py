import random
#zufällige zahl generieren
x = random.randrange(1,100)
# erste definiton von x damit die while schleife funktioniert
raten = 4
# einführung für den user in das spiel
print("Hallo, Willkommen beim Zahlen raten. Wir haben uns eine Zahl zwischen 1 und 100 überlegt.")
print("Gib solange ganze Zahlen an, bis du unsere Zahl erraten hast.")
print("Wir sagen Bescheid, ob unsere Zahl größer oder kleiner ist.")
print("Um das Programm abzubrechen, schreib 'e'.")
# While x = input false schleife einfügen
while x != raten:
#eingabe des geratenen, ausgabe bei zu großer geratener Zahl
    print("Gib eine Zahl zwischen 1 und 100 an.")
    raten = input()
    # einbauen eines vorzeitigen exits der schleife
    if raten == "e":
        break
    raten = int(raten)
    # ausgabe bei zu groß geratener zahl
    if raten > x:
        print ("zu groß!"),
    # ausgabe bei zu kleiner geratener Zahl
    elif raten < x:
        print ("zu klein!")
#rückmeldung an den user, was die korrekte Zahl ist, falls er korrekt geraten hat oder ob seine Eingabe von e erfolgreich war.
if raten == x:
    print("herzlichen Glückwunsch, du hast richtig geraten!", x)
else:
    print("Du hast das Programm abgebrochen.")
