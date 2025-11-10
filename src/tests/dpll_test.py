import unittest
from rakenteet import Klausuuli, Literaali
import dpll

class TestDpllTyhjaKlausuuli(unittest.TestCase):
    """Testaa dpll.py -tiedoston funktion tyhja_klausuuli toimintaa."""

    def test_tyhja_klausuuli_yksi_tyhja_klausuuli(self):
        """Testaa, että tyhja_klausuuli palauttaa toden,
        kun sille annetaan Klausuuli jolla ei ole linkkiä eikä arvoja."""
        self.assertTrue(dpll.tyhja_klausuuli(Klausuuli(None)))

    def test_tyhja_klausuuli_yksi_epatyhja_klausuuli(self):
        """Testaa, että tyhja_klausuuli palauttaa epätoden,
        kun sille annetaan Klausuuli, jolla on literaali."""
        self.assertFalse(dpll.tyhja_klausuuli(Klausuuli(Literaali(1))))

    def test_tyhja_klausuuli_tyhja_olio(self):
        """Testaa, että tyhja_klausuuli palauttaa epätoden,
        kun sille annetaan tyhjä olio (ts. nolla klausuulia)."""
        self.assertFalse(dpll.tyhja_klausuuli(None))

    def test_tyhja_klausuuli_toinen_tyhja(self):
        """Testaa, että tyhja_klausuuli palauttaa toden,
        kun sille annetaan lista jonka ensijäsen on epätyhjä ja toinen jäsen tyhjä."""
        testaaja = Klausuuli(Literaali(1))
        testaaja.linkki = Klausuuli(None)
        self.assertTrue(dpll.tyhja_klausuuli(testaaja))

    def test_tyhja_klausuuli_toinen_epatyhja(self):
        """Testaa, että tyhjä klausuuli palauttaa toden,
        kun sille annetaan lista jonka ensijäsen on tyhjä ja toinen jäsen epätyhjä."""
        testaaja = Klausuuli(None)
        testaaja.linkki = Klausuuli(Literaali(1))
        self.assertTrue(dpll.tyhja_klausuuli(testaaja))

class TestDpllLiteraalinValinta(unittest.TestCase):
    """Testaa dpll.py -tiedoston funktion literaalin_valinta toimintaa."""

    def test_literaalin_valinta_yksi_klausuuli_yksi_literaali(self):
        """Testaa, että literaalin_valinta palauttaa ainoan klausuulin ainoan literaalin,
        kun sille annetaan yhden Literaalin sisältävä yksittäinen Klausuuli."""
        self.assertEqual(1, dpll.literaalin_valinta(Klausuuli(Literaali(1))))

    def test_literaalin_valinta_non_sequitur_syote(self):
        """Testaa, että literaalin_valinta palauttaa None,
        kun sille annetaan täysin sopimaton syöte, testitapauksessa merkkijono"""
        self.assertEqual(None, dpll.literaalin_valinta("Eihän tämä voi toimia."))

    def test_literaalin_valinta_yksi_klausuuli_arvot_ei_literaali(self):
        """Testaa, että literaalin_valinta palauttaa None,
        kun sille annetaan Klausuuli, jonka arvot-kentässä on täysin sopimaton syöte,
        testitapauksessa merkkijono"""
        self.assertEqual(None, dpll.literaalin_valinta(Klausuuli("Eihän tämä voi toimia.")))

    def test_literaalin_valinta_literaalin_sopimaton_arvo(self):
        """Testaa, että literaalin_valinta palauttaa None,
        kun sille annetaan Klausuuli, jonka arvot-kentässä on Literaali, jonka arvo ei ole kokonaisluku,
        testitapauksessa merkkijono"""
        self.assertEqual(None, dpll.literaalin_valinta(Klausuuli(Literaali("Eihän tämä voi toimia."))))
