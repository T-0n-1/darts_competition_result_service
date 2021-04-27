# modulien ja pakettien tuonnit (import)
from pathlib import Path

# määritä luokat (class)


# määritä funktiot (def (function))
def loppu():
    pass


def lisaaTulos(kilpailu, kilpailija, tulos):
    kilpailu[kilpailija] = tulos
    # no return


def tulostaKilpailu(nimi, kilpailu):
    pass
    # no return


def tallennaKilpailu(nimi, kilpailu):
    tiedoston_nimi = Path(nimi)
    tiedoston_nimi = tiedoston_nimi.with_suffix(".txt")
    try:
        with open(tiedoston_nimi, "w") as tiedosto:
            for arvo, avain in kilpailu:
                tiedosto.write(str(avain) + ": " + str(arvo) + "\n")
    except FileNotFoundError:
        pass
    return tiedoston_nimi.exists()


def lataaKilpailu(nimi, kilpailu):
    tiedoston_nimi = Path(nimi)
    tiedoston_nimi = tiedoston_nimi.with_suffix(".txt")
    try:
        with open(tiedoston_nimi, "r") as tiedosto:
            kilpailu = tiedosto.read()
            kilpailu = dict(kilpailu)  # w3schools file handling --> readline etc JOS EI TOIMI
    except FileNotFoundError:
        pass
    return tiedoston_nimi.exists()


# PÄÄOHJELMA
# muuttujien alustus
kilpailu = {}  # kilpailu tulossäiliö
nimi = ""  # kilpailun nimi
valinta = ""  # valinta käyttöliittymässä
# kilpailija = ''   # kilpailijan nimi
# tulos = ''        # kilpailijan tulos

# varsinainen ohjelman runko
menu = True
while menu:
    valinta = input(
        "Anna valinta (n - aloita uusi, l - lataa vanha, s - tallenna, p - tulokset, i - lisää, q - lopeta): "
    )
    if valinta == "n":
        nimi = input("Anna kilpailun nimi: ")
        kilpailu = {}
    elif valinta == "l":
        nimi = input("Anna kilpailun nimi: ")
        if lataaKilpailu(nimi, kilpailu):
            pass
        else:
            print("Kilpailua ei löytynyt!")
            nimi = ""
    elif valinta == "s":
        tallennaKilpailu(nimi, kilpailu)
    elif valinta == "p":
        pass
    elif valinta == "i":
        if not nimi:
            nimi = input("Anna kilpailun nimi: ")
        lisää = True
        while lisää:
            kilpailija = input("Anna kilpailija: ")
            if not kilpailija:
                break
            tulos = input("Anna tulos: ")
            lisaaTulos(kilpailu, kilpailija, tulos)
    elif valinta == "q":
        loppu()
    else:
        pass
