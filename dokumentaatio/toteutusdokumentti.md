# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Toteutusdokumentti

#### Ohjelman yleisrakenne

Ohjelman päätoiminnot ovat dpll.py -tiedostossa. Tietorakenteina on toteutettu kaksi linkitettyä listaa rakenteet.py:ssä. DIMACS CNF -muotoisten tiedostojen lukeminen ja muuntaminen toteutettuihin tietorakenteisiin tapahtuu syote_purku.py:ssä olevilla funktioilla.

#### Aika- ja tilavaativuudet

DPLL:n huonoimman tapauksen aikavaativuus on O(n²), ja tilavaativuus O(n), missä n on lauseessa olevien totuusmuuttujien määrä. ([Freiburgin Yliopisto](https://cca.informatik.uni-freiburg.de/sat/ss23/03))

#### Työn puutteet ja parannusehdotukset

Työstä puuttuu tässä vaiheessa (viikko 4) puhtaan literaalin poisto. Lisäksi algoritmista tarpeettoman suuri osa tapahtuu vielä karsinta-funktion sisällä.

#### Laajojen kielimallien käyttö

Työn toteutuksessa ei ole käytetty laajoja kielimalleja.

#### Työn toteutuksessa käytetyt lähteet

Algoritmin pääasiallinen lähde: [Aalto-yliopisto](https://users.aalto.fi/~tjunttil/2020-DP-AUT/notes-sat/index.html)

Algoritmin ymmärtämisen tukilähde: [Englanninkielinen Wikipedia](https://en.wikipedia.org/wiki/DPLL_algorithm)

Havainnollistava video: [New Hampshiren yliopisto, YouTube](https://www.youtube.com/watch?v=ENHKXZg-a4c)