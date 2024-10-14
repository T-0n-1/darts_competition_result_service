import unittest
from pathlib import Path
from io import StringIO
import sys
from ratkaisu import lisaaTulos, tulostaKilpailu, tallennaKilpailu, lataaKilpailu


class TestTikkakilpailu(unittest.TestCase):
    def setUp(self):
        # Tämä funktio suoritetaan ennen jokaista testiä
        self.kilpailu = {}
        self.kilpailun_nimi = "testikilpailu"

    def test_lisaaTulos(self):
        # Testaa lisaaTulos-funktiota
        lisaaTulos(self.kilpailu, "Matti", "100")
        self.assertIn("Matti", self.kilpailu)
        self.assertEqual(self.kilpailu["Matti"], "100")

    def test_tulostaKilpailu(self):
        # Testaa tulostaKilpailu-funktiota
        lisaaTulos(self.kilpailu, "Matti", "100")
        lisaaTulos(self.kilpailu, "Kaisa", "90")

        kaapattu_tuloste = StringIO()  # Luo StringIO-objekti tulosteen kaappaamiseen
        sys.stdout = kaapattu_tuloste  # Uudelleenohjaa stdout StringIO-objektiin
        tulostaKilpailu(self.kilpailun_nimi, self.kilpailu)
        sys.stdout = sys.__stdout__  # Palauta stdout takaisin

        tuloste = kaapattu_tuloste.getvalue()
        odotettu_tuloste = "Kilpailu: testikilpailu\nMatti: 100\nKaisa: 90\n"
        self.assertEqual(tuloste, odotettu_tuloste)

    def test_tallennaKilpailu(self):
        # Testaa tallennaKilpailu-funktiota
        lisaaTulos(self.kilpailu, "Matti", "100")
        lisaaTulos(self.kilpailu, "Kaisa", "90")

        tulos = tallennaKilpailu(self.kilpailun_nimi, self.kilpailu)
        tiedoston_polku = Path(f"{self.kilpailun_nimi}.txt")

        self.assertTrue(tulos)
        self.assertTrue(tiedoston_polku.exists())

        # Poista tiedosto testin jälkeen
        tiedoston_polku.unlink()

    def test_lataaKilpailu(self):
        # Testaa lataaKilpailu-funktiota
        # Ensin tallenna joitakin tietoja tiedostoon
        lisaaTulos(self.kilpailu, "Matti", "100")
        tallennaKilpailu(self.kilpailun_nimi, self.kilpailu)

        # Sitten lataa tiedot uuteen dictionary-objectiin
        uusi_kilpailu = {}
        tulos = lataaKilpailu(self.kilpailun_nimi, uusi_kilpailu)

        self.assertTrue(tulos)
        self.assertIn("Matti", uusi_kilpailu)
        self.assertEqual(uusi_kilpailu["Matti"], "100")

        # Poista tiedosto testin jälkeen
        tiedoston_polku = Path(f"{self.kilpailun_nimi}.txt")
        tiedoston_polku.unlink()


if __name__ == "__main__":
    unittest.main()