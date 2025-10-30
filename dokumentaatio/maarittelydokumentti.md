# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Määrittelydokumentti

#### Harjoitustyön ydin

Harjoitustyössä toteutetaan [propositiologiikan toteutuvuusongelman](https://fi.wikipedia.org/wiki/Lauselogiikan_toteutuvuusongelma) ratkaiseva Davis-Putnam-Logemann-Loveland -algoritmi, eli [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm). Algoritmille annetaan propositiolause [konjunktiivisessa normaalimuodossa](https://fi.wikipedia.org/wiki/Konjunktiivinen_normaalimuoto), [DIMACS CNF](https://users.aalto.fi/~tjunttil/2021-DP-AUT/notes-sat/solving.html#the-dimacs-cnf-file-format) -formaatissa. Algoritmi palauttaa lauseen toteuttavan totuusjakauman, joka on tyhjä lauseen ollessa ristiriita.

#### Tietorakenteet ja algoritmit

Konjunktiivisessa normaalimuodossa oleva propositiolause on käytännössä kokonaislukulistojen lista. Lauseen konjunktio yhdistää klausuuleja, klausuulin disjunktio yhdistää literaaleja, literaalin itseisarvo kertoo mistä totuusjakauman symbolista on kyse ja literaalin etumerkki vastaa totuusarvoa. Harjoitustyössä lausetta käsitellään klausuuleista koostuvana yhteen suuntaan linkitettynä listana. Klausuulia käsitellään literaaleista koostuvana yhteen suuntaan linkitettynä listana. Palautettavaa totuusjakaumaa käsitellään klausuulina, ja se tulostetaan järjestettynä merkkijonona DIMACS CNF -formaatissa.

DPLL:n pohjana toimii [backtracking](https://en.wikipedia.org/wiki/Backtracking), jota voi ajatella mahdollisten totuusjakaumien puun syvyyshakuna. Algoritmia tehostavana toistettavana ominaisuutena toteutetaan [yksikköpropagaatio](https://en.wikipedia.org/wiki/Unit_propagation). Lisäksi vähintään algoritmin alkuvaiheessa toteutetaan [puhtaan literaalin poisto](https://users.aalto.fi/~tjunttil/2020-DP-AUT/notes-sat/preprocessing.html#pure-literal-elimination).

DIMACS CNF -formaattisen syötteen muuntamiseen kokonaislukulistojen listaksi luodaan oma algoritminsa.

#### Tila- ja aikavaativuus

DPLL:n huonoimman tapauksen aikavaativuus on O(n²), ja tilavaativuus O(n). ([Freiburgin Yliopisto](https://cca.informatik.uni-freiburg.de/sat/ss23/03))

#### Ohjelmointikielet

Harjoitustyö toteutetaan kokonaisuudessaan Pythonilla.

#### Toteutuksessa käytettävät lähteet

Algoritmin pääasiallisena lähteenä toimii Aalto-yliopiston perustieteiden korkeakoulun tietotekniikan laitoksen kurssin Declarative Programming [kurssimateriaalin](https://users.aalto.fi/~tjunttil/2020-DP-AUT/notes-sat/index.html) toteutuvuusongelmaa koskevat osat. Täydentävänä lähteenä käytetään englanninkielisen Wikipedian soveltuvia artikkeleita (linkkejä ylempänä), sekä vapaasti verkosta löytyvää yliopistojen kurssimateriaalia (mm. [New Hampshiren yliopisto](https://www.youtube.com/watch?v=ENHKXZg-a4c), [Pennsylvanian yliopisto](https://www.cis.upenn.edu/~cis1890/files/Lecture3.pdf), [Oxfordin yliopisto](https://www.cs.ox.ac.uk/people/james.worrell/lecture06.pdf))

#### Hallinnolliset tiedot

- Harjoitustyön dokumentaatio toteutetaan suomen kielellä.
- Kurssi suoritetaan osana Helsingin yliopiston matemaattis-luonnontieteellisen tiedekunnan tietojenkäsittelytieteen kandiohjelmaa.
- Vertaisarvioitavaksi voidaan antaa Pythonia, Javaa ja Haskellia, sekä tilanteen sattuessa JavaScriptiä tai R:ää käyttäviä harjoitustöitä.