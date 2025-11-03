import os
from rakenteet import Klausuuli
from rakenteet import Literaali
from syote_purku import syote_purku

## Tämän hetkisessä muodossaan ohjelma ainoastaan muuttaa datan käsiteltävään muotoon.
## Algoritmin toteutus puuttuu vielä kokonaisuudessaan.

def main():
    """Pääfunktio, joka kutsuu algoritmin osat toteuttavia funktioita.
    Ohjelman kulku kuvailtu tarkemmin funktiokutsuja edeltävissä kommenteissa, sekä alifunktioiden kuvauksissa."""
    ##Kysy syötteen sijaintia
    syote = syotteen_kysyja()
    ## Lue syöte ja muunna syöte listojen listaksi
    alku_klausuuli = syote_purku(syote)
    ## Tarkistustuloste, poistetaan lopputuoteesta
    tulosta_lista(alku_klausuuli)
    ##TODO: Etsi listojen listasta totuusjakauma
    ##TODO: Tulosta lopputulos

def syotteen_kysyja():
    """Kysyy käyttäjältä DIMACS CNF -tiedoston polun.
    Tarkistaa että tiedosto on olemassa, mutta olettaa sen olevan formaatin mukainen."""

    print("Syötä tiedoston kansion nimi ja tiedoston nimi.")
    print("Käytä tiedoston polkua dpll-labra -kansiosta lähtien")
    print("Esimerkiksi esimerkkidata/esim1.cnf")
    while True:
        syote = "./" + input()
        if os.path.exists(syote):
            return syote
        else:
            print("Viallinen syöte, yritä uudelleen")

def tulosta_lista(a):
    """Apufunktio, joka tulostaa listan terminaaliin suhteellisen luettavassa muodossa,
    käytetään debuggaukseen."""
    tama_kla = a
    tama_lit = a.arvot
    klausuuli_indeksi = 1
    while tama_kla is not None:
        while tama_lit is not None:
            print(tama_lit.arvo)
            tama_lit = tama_lit.linkki
        print("Klausuulin " + str(klausuuli_indeksi) + " loppu")
        klausuuli_indeksi += 1
        tama_kla = tama_kla.linkki
        if tama_kla is not None:
            tama_lit = tama_kla.arvot

if __name__=="__main__":
    main()

