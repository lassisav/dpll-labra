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
    viime_klausuuli = None
    tama_klausuuli = lista
    ylempi_jatkuu = True
    while ylempi_jatkuu:
        alempi_jatkuu = True
        viime_literaali = None
        tama_literaali = tama_klausuuli.arvot
        while alempi_jatkuu:
            if tama_literaali.arvo == annettu:
                if viime_klausuuli is None:
                    lista = tama_klausuuli.linkki
                else:
                    viime_klausuuli.linkki = tama_klausuuli.linkki
                tama_klausuuli = tama_klausuuli.linkki
                if tama_klausuuli is None:
                        ylempi_jatkuu = False
                alempi_jatkuu = False
            elif tama_literaali.arvo == (annettu * (-1)):
                if viime_literaali is None:
                    tama_klausuuli.arvot = tama_literaali.linkki
                else:
                    viime_literaali.linkki = tama_literaali.linkki
                viime_klausuuli = tama_klausuuli
                tama_klausuuli = tama_klausuuli.linkki
                if tama_klausuuli is None:
                        ylempi_jatkuu = False
                alempi_jatkuu = False
            else:
                if tama_literaali.linkki is None:
                    viime_klausuuli = tama_klausuuli
                    tama_klausuuli = tama_klausuuli.linkki
                    if tama_klausuuli is None:
                        ylempi_jatkuu = False
                    alempi_jatkuu = False
                else:
                    viime_literaali = tama_literaali
                    tama_literaali = tama_literaali.linkki
    return lista    

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

def luo_kopio_klausuuli(vanha_lista):
    """Luo kopion annetusta klausuulien listasta ja palauttaa sen."""
    vanha_tama_klausuuli = vanha_lista
    uusi_lista = Klausuuli(luo_kopio_literaali(vanha_lista.arvot))
    uusi_tama_klausuuli = uusi_lista
    while True:
        if vanha_tama_klausuuli.linkki is not None:
            uusi_tama_klausuuli.linkki = Klausuuli(luo_kopio_literaali(vanha_tama_klausuuli.linkki.arvot))
            vanha_tama_klausuuli = vanha_tama_klausuuli.linkki
            uusi_tama_klausuuli = uusi_tama_klausuuli.linkki
        else:
            return uusi_lista

def luo_kopio_literaali(lista):
    """Luo kopion annetusta literaalien listasta ja palauttaa sen."""
    if lista is None:
        return None
    uusi = Literaali(lista.arvo)
    uusi.linkki = luo_kopio_literaali(lista.linkki)
    return uusi

def lisaa_loppuun_klausuuli(lista, arvot):
    """Lisää listan loppuun klausuulin annetulla arvot:lla."""
    if lista is None:
        return Klausuuli(arvot)
    pohja = lista
    while True:
        if pohja.linkki is None:
            pohja.linkki = Klausuuli(arvot)
            return lista
        pohja = pohja.linkki

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

