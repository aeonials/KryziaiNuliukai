
zaidejas1 = input("Zaidejas 1 pasirink X arba O")
if zaidejas1 == "x":
    zaidejas2 = "O"
    zaidejas1 = "X"
else:
    zaidejas2 = "X"
    zaidejas1 = "O"

print(f"Zaidejas 1 yra {zaidejas1} ir Zaidejas 2 yra {zaidejas2}")

lentele = [" " for x in range(9)]

def startas():
    print("Sveiki atvyke i Kryziukai ir Nuliukai!")
    p_lentele()
    zaidejo_eile("1")

def p_lentele():
    print("     |     |     ")
    print("  " + lentele[0] + "  |  " + lentele[1] + "  |  " + lentele[2] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + lentele[3] + "  |  " + lentele[4] + "  |  " + lentele[5] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + lentele[6] + "  |  " + lentele[7] + "  |  " + lentele[8] + "  ")
    print("     |     |     ")

def zaidejo_eile(eile):
    print(f"Zaidejas {eile}, yra tavo eile.")
    pozicija = input("Issirink pozicija nuo 1-9: ")
    while pozicija not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        pozicija = input("Neteisinga pozicija. Issirink nuo 1-9: ")

    pozicija = int(pozicija)
    simbolis = zaidejas1 if eile == "1" else zaidejas2

    if lentele[pozicija - 1] == " ":
        lentele[pozicija - 1] = simbolis
        p_lentele()
        if patikrinti():
            return

        eile = "2" if eile == "1" else "1"
        zaidejo_eile(eile)
    else:
        print("Pozicija jau uzimta!")
        zaidejo_eile(eile)

def patikrinti():
    for i in range(0, 3):
        if lentele[i] == lentele[i + 3] == lentele[i + 6] != " ":
            if lentele[i] == zaidejas1:
                print("Zaidejas 1 laimejo!")
            elif lentele[i] == zaidejas2:
                print("Zaidejas 2 laimejo!")
            return True

    for i in range(0, 9, 3):
        if lentele[i] == lentele[i + 1] == lentele[i + 2] != " ":
            if lentele[i] == zaidejas1:
                print("Zaideajs 1 laimejo!")
            elif lentele[i] == zaidejas2:
                print("Zaidejas 2 laimejo!")
            return True

    if lentele[0] == lentele[4] == lentele[8] != " ":
        if lentele[0] == zaidejas1:
            print("Zaidejas 1 laimejo!")
        elif lentele[0] == zaidejas2:
            print("Zaidejas 2 laimejo!")
        return True
    if lentele[2] == lentele[4] == lentele[6] != " ":
        if lentele[2] == zaidejas1:
            print("Zaidejas 1 laimejo!")
        elif lentele[2] == zaidejas2:
            print("Zaidejas 2 laimejo!")
        return True

    if " " not in lentele:
        print("Lygu!")
        return True

startas()