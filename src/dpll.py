import os
from rakenteet import Klausuuli
from rakenteet import Literaali
from syote_purku import syote_purku

## Tämän hetkisessä muodossaan ohjelma ainoastaan muuttaa datan käsiteltävään muotoon.
## Algoritmin toteutus puuttuu vielä kokonaisuudessaan.

def main():
    """Pääfunktio, joka kutsuu algoritmin osat toteuttavia funktioita.
    Ohjelman kulku kuvailtu tarkemmin funktiokutsuja edeltävissä kommenteissa, sekä alifunktioiden kuvauksissa."""
    ## Kysy syötteen sijaintia
    syote = syotteen_kysyja()
    ## Lue syöte ja muunna syöte listojen listaksi
    alku_klausuuli = syote_purku(syote)
    ## Tarkistustuloste, poistetaan lopputuoteesta
    tulosta_lista(alku_klausuuli)
    ##TODO: Etsi listojen listasta totuusjakauma
    jakauma = karsinnan_alustus(alku_klausuuli, None)
    ##TODO: Tulosta lopputulos
    print(jakauma_merkkijonoksi(jakauma))
    

def karsinnan_alustus(lista, jakauma):
    ##TODO: Puhtaan literaalin poisto
    ## Toteutusjakauman haku
    return karsinta(lista, jakauma)

def karsinta(lista, jakauma):
    pass
    ## Onnistumisen tarkistus
    if lista is None:
        return jakauma
    ## Epäonnistumisen tarkistus
    if tyhja_klausuuli(lista):
        return None
    ##TODO: Yksikköpropagaatio
    ##TODO: Literaalin valinta
    ##TODO: Literaalin karsinta
    ##TODO: Literaalin negaation karsinta

def tyhja_klausuuli(lista):
    if lista is None:
        return False
    if lista.arvot is None:
        return True
    return lista.linkki

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
        print("Viallinen syöte, yritä uudelleen")

def tulosta_lista(lista):
    """Apufunktio, joka tulostaa listan terminaaliin suhteellisen luettavassa muodossa,
    käytetään debuggaukseen."""
    tama_klausuuli = lista
    tama_literaali = lista.arvot
    klausuuli_indeksi = 1
    while tama_klausuuli is not None:
        while tama_literaali is not None:
            print(tama_literaali.arvo)
            tama_literaali = tama_literaali.linkki
        print("Klausuulin " + str(klausuuli_indeksi) + " loppu")
        klausuuli_indeksi += 1
        tama_klausuuli = tama_klausuuli.linkki
        if tama_klausuuli is not None:
            tama_literaali = tama_klausuuli.arvot

def jakauma_merkkijonoksi(jakauma):
    if jakauma is None:
        return "Ei toteutuva"
    tuloste = ""
    jatkuu = True
    while jatkuu:
        tuloste += str(jakauma.arvo)
        if jakauma.linkki is None:
            jatkuu = False
        else:
            tuloste += ", "
            jakauma = jakauma.linkki
    return tuloste

if __name__=="__main__":
    main()

