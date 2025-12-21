# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Käyttö-ohje

#### Asennus

Kloonaa repositorio omalle laitteellesi.

Asenna riippuvuudet komennolla ``` poetry install ```.

#### Syötteiden lisääminen

Algoritmin syötteinä käytetään [DIMACS CNF](https://users.aalto.fi/~tjunttil/2021-DP-AUT/notes-sat/solving.html#the-dimacs-cnf-file-format) -muotoisia .cnf-tiedostoja. Tiedostoja on repositoriossa muutamia, ja niitä voi sekä etsiä että generoida erinäisten verkkosivujen avulla. Tiedostoille voi luoda oman hakemistonsa, tai niitä voi lisätä repositorioon kuuluvaan esimerkkidata-hakemistoon. Ohjelman käytön kannalta on helpointa, että syötteenä käytettävät tiedostot ovat dpll-labra -hakemistossa tai sen alaisissa hakemistoissa.

#### Ohjelman suoritus

Navigoi terminaalissa hakemistoon dpll-labra, eli kloonaamasi repositorion hakemistoon.

Käynnistä ohjelma komennolla ``` poetry run invoke kaynnista ```.

Aloitusdialogin jälkeen syötä käsiteltävän tiedoston polku hakemistosta katsoen, esimerkiksi esimerkkidata/esim1.cnf.

Ohjelma suorittaa algoritmin, ja tulostaa jonkin annetun lauseen toteuttavan totuusjakauman. Jos lause ei ole toteutuva, tulostaa ohjelma tiiviisti tekstin ``` Tyhjä ```.

Ohjelman suoritus päätyy, kun algoritmi on suoritettu.

#### Testien suorittaminen

Testit suoritetaan dpll-labra -hakemistossa komennolla ``` poetry run invoke testit```.

Testikattavuusraportti luodaan komennolla ``` poetry run invoke kattavuus```. Tämä komento luo kattavuusraportin, tulostaa sen terminaaliin, sekä luo siitä html-tiedoston hakemistoon htmlcov.