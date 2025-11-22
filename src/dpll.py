import os
from rakenteet import Klausuuli
from rakenteet import Literaali
from syote_purku import syote_purku

## Tämän hetkisessä muodossaan ohjelma ainoastaan muuttaa datan käsiteltävään muotoon.
## Algoritmin toteutus puuttuu vielä kokonaisuudessaan.

def main(): ## Ei yksikkötestata, pääfunktio jossa mahdollisimman vähän omia toiminnallisuuksia.
    """Pääfunktio, joka kutsuu algoritmin osat toteuttavia funktioita.
    Ohjelman kulku kuvailtu tarkemmin funktiokutsuja edeltävissä kommenteissa,
    sekä alifunktioiden kuvauksissa."""
    ## Kysy syötteen sijaintia
    syote = syotteen_kysyja()
    ## Lue syöte ja muunna syöte listojen listaksi
    alku_klausuuli = syote_purku(syote)
    ## Etsi listojen listasta totuusjakauma, aka DPLL-algoritmi
    jakauma = karsinnan_alustus(alku_klausuuli, None)
    ## Tulosta lopputulos
    print(literaalit_merkkijonoksi(jakauma))

def karsinnan_alustus(lista, jakauma): ##Ei yksikkötestata, funktio vain kutsuu muita ja palauttaa.
    """Funktio, joka toteuttaa algoritmin alkuvaiheessa tehtävät toimet,
    ja siirtää toteutuksen eteenpäin karsinta-funktiolle."""
    ##TODO: Puhtaan literaalin poisto
    ## Toteutusjakauman haku
    return karsinta(lista, jakauma)

def karsinta(lista, jakauma): ## Ei yksikkötestata, irroitetaan mahdollisimman paljon yksiköitä.
    """Funktio, joka toteuttaa algoritmin toistettavat toimet."""
    ## Onnistumisen tarkistus
    if lista is None:
        return jakauma
    ## Epäonnistumisen tarkistus
    if tyhja_klausuuli(lista):
        return None
    ## Yksikköpropagaatio
    yksikoita_loytyy = True
    while yksikoita_loytyy:
        valittu = yksikkopropagaation_valinta(lista)
        if valittu == 0:
            yksikoita_loytyy = False
        else:
            lista = poista_annettu(lista, valittu)
            jakauma = lisaa_jakaumaan_literaali(jakauma, valittu)
            if lista is None:
                return jakauma
            if tyhja_klausuuli(lista):
                return None
    ## Literaalin valinta
    valittu = literaalin_valinta(lista)
    ## Yritetään literaalilla
    yritys_lista = luo_kopio_klausuuli(lista)
    yritys_jakauma = luo_kopio_literaali(jakauma)
    yritys_jakauma = lisaa_jakaumaan_literaali(yritys_jakauma, valittu)
    yritys_lista = poista_annettu(yritys_lista, valittu)
    mahdollisuus = karsinta(yritys_lista, yritys_jakauma)
    if mahdollisuus is not None:
        return mahdollisuus
    ## Yritetään literaalin negaatiolla
    valittu = valittu * (-1)
    yritys_lista = luo_kopio_klausuuli(lista)
    yritys_jakauma = luo_kopio_literaali(jakauma)
    yritys_jakauma = lisaa_jakaumaan_literaali(yritys_jakauma, valittu)
    yritys_lista = poista_annettu(yritys_lista, valittu)
    mahdollisuus = karsinta(yritys_lista, yritys_jakauma)
    if mahdollisuus is not None:
        return mahdollisuus
    ## Palautetaan tyhjä
    return None

def poista_annettu(lista, annettu): ##TODO: Yksikkötestaus
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

def yksikkopropagaation_valinta(lista): ##TODO: Yksikkötestaus
    """Saa syötteenä listan klausuuleja, ja palauttaa kokonaislukumuotoisen totuusarvon,
    joka esiintyy ensimmäisessä yksikköklausuulissa, eli yhden literaalin sisältävässä klausuulissa.
    Jos listassa ei ole yksikköklausuulia, palauttaa 0."""
    while True:
        if lista is None:
            return 0
        if lista.arvot.linkki is None:
            return lista.arvot.arvo
        lista = lista.linkki

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

##TODO: Eriytä omaan tiedostoonsa.
def syotteen_kysyja(): ## Ei yksikkötestata, käyttöliittymäfunktio
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

def literaalit_merkkijonoksi(jakauma): ## Yksikkötestit tehty
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
            tuloste += " "
            jakauma = jakauma.linkki
    return tuloste

def luo_kopio_klausuuli(vanha_lista): ##TODO: Yksikkötestaus
    """Luo kopion annetusta klausuulien listasta ja palauttaa sen."""
    vanha_klausuuli = vanha_lista
    uusi_lista = Klausuuli(luo_kopio_literaali(vanha_lista.arvot))
    uusi_klausuuli = uusi_lista
    while True:
        if vanha_klausuuli.linkki is not None:
            uusi_klausuuli.linkki = Klausuuli(luo_kopio_literaali(vanha_klausuuli.linkki.arvot))
            vanha_klausuuli = vanha_klausuuli.linkki
            uusi_klausuuli = uusi_klausuuli.linkki
        else:
            return uusi_lista

def luo_kopio_literaali(lista): ##TODO: Yksikkötestaus
    """Luo kopion annetusta literaalien listasta ja palauttaa sen."""
    if lista is None:
        return None
    tama_kopioitava = lista
    tama_kopio = Literaali(lista.arvo)
    lista_kopio = tama_kopio
    while True:
        if tama_kopioitava.linkki is None:
            return lista_kopio
        tama_kopioitava = tama_kopioitava.linkki
        tama_kopio.linkki = Literaali(tama_kopioitava.arvo)
        tama_kopio = tama_kopio.linkki

def lisaa_jakaumaan_literaali(jakauma, arvo): ## Yksikkötestit tehty
    """Lisää jakaumaan literaalin annetulla arvolla.
    Olettaa jakauman olevan lista literaaleja, ja arvon kokonaisluku."""
    uusi = Literaali(arvo)
    if jakauma is None:
        return uusi
    pohja = jakauma
    if abs(pohja.arvo) > abs(arvo):
        uusi.linkki = pohja
        return uusi
    while True:
        if pohja.linkki is None:
            pohja.linkki = uusi
            return jakauma
        if abs(pohja.linkki.arvo) > abs(arvo):
            jalki = pohja.linkki
            pohja.linkki = uusi
            uusi.linkki = jalki
            return jakauma
        pohja = pohja.linkki

if __name__=="__main__":
    main()
