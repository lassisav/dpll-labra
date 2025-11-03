from rakenteet import Klausuuli
from rakenteet import Literaali


def syote_purku(tiedosto):
    """Funktio hakee annetun nimisestä tiedostosta DIMACS CNF -formaattiseksi oletetun datan,
    muuntaa jokaisen tiedostossa olevan klausuulimerkkijonon Klausuuli-tyyppiseksi,
    ja palauttaa linkitetyn listan Klausuuleja."""

    alku_klausuuli = None
    loppu_klausuuli = Klausuuli(None)
    with open(tiedosto, 'r', encoding='UTF-8') as syote:
        for rivi in syote:
            if rivi[0] != 'c' and rivi[0] != 'p':
                if alku_klausuuli is None:
                    alku_klausuuli = Klausuuli(yhdista_literaalit(rivi))
                    loppu_klausuuli = alku_klausuuli
                else:
                    loppu_klausuuli.linkki = Klausuuli(yhdista_literaalit(rivi))
                    loppu_klausuuli = loppu_klausuuli.linkki
    return alku_klausuuli

def jako_vali(syote, alku):
    """Funktio ottaa syötteenä merkkijonon ja totuusarvon,
    ja palauttaa merkkijonon ensimmäisen välilyönnin vasemman puolen truella ja oikean falsella."""

    n = syote.find(" ")
    if n == -1:
        return None
    if alku:
        return syote[:n]
    return syote[(n+1):]

def yhdista_literaalit(rivi):
    """Funktio ottaa syötteenä DIMACS CNF -formaattisen klausuulimerkkijonon,
    ja palauttaa linkitetyn listan klausuulissa olevista Literaaleista."""

    alku_literaali = None
    loppu_literaali = None
    while jako_vali(rivi, False) is not None:
        seuraava = int(jako_vali(rivi, True))
        rivi = jako_vali(rivi, False)
        if alku_literaali is None:
            alku_literaali = Literaali(seuraava)
            loppu_literaali = alku_literaali
        else:
            loppu_literaali.linkki = Literaali(seuraava)
            loppu_literaali = loppu_literaali.linkki
    
    return alku_literaali