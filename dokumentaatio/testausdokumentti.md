# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Testausdokumentti

#### Testikattavuusraportti

| Name                 | Stmts | Miss | Branch | BrPart | Cover | Missing |
|----------------------|-------|------|--------|--------|-------|---------|
| src/dpll.py | 163 | 77 | 74 | 3 | 54% | 14-20, 27, 32-70, 89->91, 104-108, 128-133, 152-159, 178-187, 191-201, 225 |
| src/rakenteet.py | 8 | 0 | 0 | 0 | 100% |
| src/syote_purku.py | 33 | 28 | 14 | 0 | 11% | 10-21, 27-32, 38-50 |
| TOTAL | 204 | 105 | 88 | 3 | 48% |

#### Testauskertomus

Ohjelman tässä vaiheessa (viikko 4) testaus on kokonaisuudessaan yksikkötestausta, jolla testataan dpll.py -tiedoston funktioita. Testien syötteinä käytetään pieniä, käsin kirjoitettuja, työssä toteutettuja tietorakenteita, sekä kokonaislukuja ja merkkijonoja. Testaus on toteutettu suurimmilta osin niille funktioille, jotka ovat poikkeuksetta suorituksen loppupäässä, toisin sanoen ei-rekursiivisille funktioille. dpll.py -tiedostoon on merkitty mitkä funktiot on testattu kattavasti, mitkä osittain, ja mitä ei ollenkaan.

Päästä päähän -testausta, tai mitään kokonaisvaltaisempaa algoritmin testausta, ei ole vielä toteutettu, mutta se on työn alla jo kurssin vaatimuksien vuoksi. Suorituskykytestausta on tehty pintapuolisesti eri kehitysvaiheissa lähinnä koesyötekokoa määrittäessä ja sitä tullaan tekemään syvemmin ja tilastoivasti, kun algoritmin vaaditut osat on toteutettu.

#### Testien suorittaminen

Testien suorittaminen vaatii poetryn riippuvuuksien latauksen,

```bash
poetry install
```

Poetry-kuoren käynnistämisen,

```bash
poetry shell
```

sekä testikomennon ajamisen Poetry-kuoressa.

```bash
pytest src
```

Testikattavuuden haarautumakattavuuksineen saa generoitua,

```bash
coverage run --branch -m pytest src
```

ja generoinnin jälkeen joko tulostettua terminaaliin

```bash
coverage report -m
```

tai visualisoitua html-tiedostoon.

```bash
coverage html
```