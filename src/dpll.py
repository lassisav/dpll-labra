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
    tulosta_klausuulilista(alku_klausuuli)
    ##TODO: Etsi listojen listasta totuusjakauma
    jakauma = karsinnan_alustus(alku_klausuuli, None)
    ##TODO: Tulosta lopputulos
    print(literaalit_merkkijonoksi(jakauma))
    

def karsinnan_alustus(lista, jakauma):
    """Funktio, joka toteuttaa algoritmin alkuvaiheessa tehtävät toimet, ja siirtää toteutuksen eteenpäin karsinta-funktiolle."""
    ##TODO: Puhtaan literaalin poisto
    ## Toteutusjakauman haku
    return karsinta(lista, jakauma)

def karsinta(lista, jakauma):
    """Funktio, joka toteuttaa algoritmin toistettavat toimet."""
    ## Onnistumisen tarkistus
    if lista is None:
        return jakauma
    ## Epäonnistumisen tarkistus
    if tyhja_klausuuli(lista):
        return None
    ##TODO: Yksikköpropagaatio
    ## Literaalin valinta
    valittu = literaalin_valinta(lista)
    ## Yritetään literaalilla
    yritys_lista = luo_kopio_klausuuli(lista)
    yritys_jakauma = luo_kopio_literaali(jakauma)
    yritys_jakauma = lisaa_loppuun_literaali(yritys_jakauma, valittu)
    yritys_lista = poista_annettu(yritys_lista, valittu)
    mahdollisuus = karsinta(yritys_lista, yritys_jakauma)
    if mahdollisuus is not None:
        return mahdollisuus
    ## Yritetään literaalin negaatiolla
    valittu = valittu * (-1)
    yritys_lista = luo_kopio_klausuuli(lista)
    yritys_jakauma = luo_kopio_literaali(jakauma)
    yritys_jakauma = lisaa_loppuun_literaali(yritys_jakauma, valittu)
    yritys_lista = poista_annettu(yritys_lista, valittu)
    mahdollisuus = karsinta(yritys_lista, yritys_jakauma)
    if mahdollisuus is not None:
        return mahdollisuus
    ## Palautetaan tyhjä
    return None

def poista_annettu(lista, annettu):
    """Poistaa listasta klausuulit, joissa on annetun arvoinen literaali,
    sekä annetun arvon negaatioiset literaalit."""
    if lista is None:
        return lista
    viime = None
    tama = lista.arvot
    while True:
        if tama.arvo == annettu:
            return poista_annettu(lista.linkki, annettu)
        if tama.arvo == (annettu * (-1)):
            if viime is None:
                lista.arvot = tama.linkki    
            else:
                viime.linkki = tama.linkki
            lista.linkki = poista_annettu(lista.linkki, annettu)
            return lista
        if tama.linkki is None:
            lista.arvot = tama.linkki
            lista.linkki = poista_annettu(lista.linkki, annettu)
            return lista
        viime = tama
        tama = tama.linkki


def tyhja_klausuuli(lista): ## Yksikkötestit tehty
    """Tarkistaa, onko syötteenä annetussa listassa tyhjää klausuulia."""
    pohja = lista
    while True:
        if pohja is None:
            return False
        if pohja.arvot is None:
            return True
        pohja = pohja.linkki

def literaalin_valinta(lista): ## Yksikkötestit tehty
    """Saa syötteenä listan klausuuleja, ja palauttaa ensimmäisen klausuulin ensimmäisen literaalin.
    Palauttaa None, jos syötteellä ei ole Klausuulin arvot-kenttää,
    tai arvot:lla Literaalin arvo-kenttää,
    tai arvo:ssa on jotain muuta kuin kokonaisluku.
    Ei harkitse, onko totuusjakaumaan lisättyjä arvoja vastaavat literaalit poistettu."""
    if hasattr(lista, 'arvot'):
        if hasattr(lista.arvot, 'arvo'):
            if isinstance(lista.arvot.arvo, int):
                return lista.arvot.arvo
    return None

def syotteen_kysyja():
    """Kysyy käyttäjältä DIMACS CNF -tiedoston polun.
    Tarkistaa että tiedosto on olemassa, mutta olettaa sen olevan formaatin mukainen.
    Palauttaa kysytyn polun."""

    print("Syötä tiedoston kansion nimi ja tiedoston nimi.")
    print("Käytä tiedoston polkua dpll-labra -kansiosta lähtien")
    print("Esimerkiksi esimerkkidata/esim1.cnf")
    while True:
        syote = "./" + input()
        if os.path.exists(syote):
            return syote
        print("Viallinen syöte, yritä uudelleen")

def tulosta_klausuulilista(lista):
    """Apufunktio, joka tulostaa klausuulilistan terminaaliin suhteellisen luettavassa muodossa,
    käytetään debuggaukseen."""
    tama_klausuuli = lista
    tama_literaali = lista.arvot
    klausuuli_indeksi = 1
    while tama_klausuuli is not None:
        print("Klausuuli " + str(klausuuli_indeksi))
        print(literaalit_merkkijonoksi(tama_literaali))
        klausuuli_indeksi += 1
        tama_klausuuli = tama_klausuuli.linkki
        if tama_klausuuli is not None:
            tama_literaali = tama_klausuuli.arvot

def literaalit_merkkijonoksi(jakauma):
    """Ottaa syötteenä listan literaaleja, ja palauttaa listaa kuvaavan merkkijonon."""
    if jakauma is None:
        return "Tyhjä"
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

def luo_kopio_klausuuli(lista):
    """Luo kopion annetusta listasta ja palauttaa sen."""
    if lista is None:
        return None
    uudet_arvot = luo_kopio_literaali(lista.arvot)
    uusi = Klausuuli(uudet_arvot)
    uusi.linkki = luo_kopio_klausuuli(lista.linkki)
    return uusi

def luo_kopio_literaali(lista):
    """Luo kopion annetusta listasta ja palauttaa sen."""
    if lista is None:
        return None
    uusi = Literaali(lista.arvo)
    uusi.linkki = luo_kopio_literaali(lista.linkki)
    return uusi

def lisaa_loppuun_literaali(lista, arvo):
    """Lisää listan loppuun literaalin annetulla arvolla."""
    if lista is None:
        return Literaali(arvo)
    pohja = lista
    while True:
        if pohja.linkki is None:
            pohja.linkki = Literaali(arvo)
            return lista
        pohja = pohja.linkki

if __name__=="__main__":
    main()

