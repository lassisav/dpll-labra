# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Testausdokumentti

#### Testikattavuusraportti

| Name                 | Stmts | Miss | Branch | BrPart | Cover | Missing |
|----------------------|-------|------|--------|--------|-------|---------|
| src/dpll.py | 215 | 126 | 98 | 3 | 42% | 14-20, 26-28, 34-55, 59-70, 75-92, 98-136, 155->157, 170-174, 194-199, 218-225, 244-253, 257-267, 291 |
| src/rakenteet.py | 8 | 0 | 0 | 0 | 100% |
| src/syote_purku.py | 33 | 28 | 14 | 0 | 11% | 10-21, 27-32, 38-50 |
| TOTAL | 204 | 105 | 88 | 3 | 48% |

#### Yksikkötestaus

Ohjelman automatisoitu testaus on kokonaisuudessaan yksikkötestausta, jolla testataan dpll.py -tiedoston funktioita. Testien syötteinä käytetään pieniä, käsin kirjoitettuja, työssä toteutettuja tietorakenteita, sekä kokonaislukuja ja merkkijonoja. Testaus on toteutettu suurimmilta osin niille funktioille, jotka ovat poikkeuksetta suorituksen alimmilla tasoilla, eli eivät suuremmin kutsu muita funktioita. dpll.py -tiedostoon on merkitty mitkä funktiot on testattu kattavasti, mitkä osittain, ja mitä ei ollenkaan.

#### Suorituskykytestaus

Ohjelman suorituskykyä on testattu eri syötteillä, joista osa on toteutuvia lauseita ja osa ei-toteutuvia. Testattavan tiedoston nimessä uf tarkoittaa toteutuvaa lausetta ja uuf ei-toteutuvaa. Tätä seuraava numero tarkoittaa lauseen muuttujien määrää, ja lopun numero on uniikki identifiointi. Testilauseina on käytetty Brittiläisen Kolumbian yliopiston luomaa [SATLIB - Benchmark Problems](https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html) -dataa. Testauksen tulokset löytyvät taulukosta tämän dokumentaation tiedostosta [Suorituskykytestaus](https://github.com/lassisav/dpll-labra/blob/main/dokumentaatio/suorituskykytestaus.md)

#### Testien suorittaminen ja testikattavuus

Testien suorittamisen ja testikattavuuden tarkastelun ohjeet löytyvät ohjelman [käyttöohjeesta](https://github.com/lassisav/dpll-labra/blob/main/dokumentaatio/kayttoohje.md)