class Klausuuli:
    """Linkitetyn listan solmu.
    Sisältää arvot:n, joka on Literaali, sekä linkin, joka on listan seuraava Klausuuli."""
    def __init__(self, arvot):
        self.arvot = arvot
        self.linkki = None

class Literaali:
    """Linkitetyn listan solmu.
    Sisältää arvon, joka on kokonaisluku, sekä linkin, joka on listan seuraava Literaali."""
    def __init__(self, arvo):
        self.arvo = arvo
        self.linkki = None
