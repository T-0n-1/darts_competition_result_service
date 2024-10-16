# modulien ja pakettien tuonnit (import)
from pathlib import Path

# määritä luokat (class)


# määritä funktiot (function)
def lisaaTulos(kilpailu: dict, kilpailija: str, tulos: str) -> None:
    kilpailu[kilpailija] = tulos


def tulostaKilpailu(nimi: str, kilpailu: dict) -> None:
    print(f'Kilpailu: {nimi}')
    for avain in kilpailu:
        print(f'{avain}: {kilpailu[avain]}')


def tallennaKilpailu(nimi: str, kilpailu: dict) -> bool or None:
    tiedoston_nimi = Path(nimi)
    tiedoston_nimi = tiedoston_nimi.with_suffix(".txt")
    try:
        with open(tiedoston_nimi, "w") as tiedosto:
            for key in kilpailu.keys():
                    tiedosto.write("%s,%s" % (key, kilpailu[key]))
                    tiedosto.write('\n')
    except FileNotFoundError:
        pass
    return tiedoston_nimi.exists()


def lataaKilpailu(nimi: str, kilpailu: dict) -> bool or None:
    tiedoston_nimi = Path(nimi)
    tiedoston_nimi = tiedoston_nimi.with_suffix(".txt")
    try:
        with open(tiedoston_nimi, "r") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.rstrip('\n')
                avain, arvo = rivi.split(',')
                kilpailu[avain]=arvo
    except FileNotFoundError:
        pass
    return tiedoston_nimi.exists()


# PÄÄOHJELMA
def main():
    # muuttujien alustus
    global nimi
    kilpailu = {}       # kilpailu tulossäiliö
    nimi = ""           # kilpailun nimi
    valinta = ""        # valinta käyttöliittymässä

    # varsinainen ohjelman runko
    menu = True
    while menu:
        valinta = input(
            '''TIKKAKILPAILUJEN TULOSPALVELU
            Anna valinta:
                n - aloita uusi
                l - lataa vanha
                s - tallenna
                p - tulokset
                i - lisää
                q - lopeta)
                ------------
                Valinta: '''
        )
        if valinta == "n":
            nimi = input("Anna kilpailun nimi: ")
            kilpailu = {}
        elif valinta == "l":
            nimi = input("Anna kilpailun nimi: ")
            kilpailu = {}
            if lataaKilpailu(nimi, kilpailu):
                pass
            else:
                print("Kilpailua ei löytynyt!")
                nimi = ""
        elif valinta == "s":
            tallennaKilpailu(nimi, kilpailu)
        elif valinta == "p":
            tulostaKilpailu(nimi, kilpailu)
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
            menu = False
        else:
            pass

if __name__ == "__main__":
    main()