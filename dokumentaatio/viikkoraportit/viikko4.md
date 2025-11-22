# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Viikkoraportti, viikko 4

Nelsoviikon alussa poistettiin suurempia syötteitä rajoittaneita rekursioita ohjelmasta. Näiden pohjalta saatiin ensimmäinen aidosti toimiva versio ohjelmasta, joka pystyi inhimillisesti siedettävässä ajassa käsittelemään 50 totuusmuuttujaa sisältäviä lauseita. Tämän jälkeen saatiin ohjelmaan myös yksikköpropagaatio, joka mahdollistaa jopa 100-muuttujaisten lauseiden käsittelyn. Tämän jälkeen keskityttiin koodin ulkoasun parantelemiseen (tässä työtä riittäisi) ja testikattavuuteen.

Ohjelman perustoiminnot ovat nyt lähes valmiit, ja määrittelyn mukaisesta algoritmista toteuttamatta on enää puhtaan literaalin poisto.

Viikon teemana (alkuviikon läpimurron jälkeen) on ollut siisteys. Vaikka olisi varmaankin hedelmällisempää oppia tekemään hyvää ja hyvin dokumentoitua koodia alusta asti, on viikko ollut hyvin opettavainen selkeän ja luettavan koodin ja dokumentaation luomisessa. On myös ollut helppoa huomata, että malliaikataulun lisäksi tuleva vertaisarviointi on ohjannut viikon prioriteettejä.

Ohjelmassa olisi ehkä jo puhtaan literaalin poistokin, mutta jäin pohtimaan sen toteutustapaa pitkäksi aikaa, joten lopulta päätin siirtää sen ensi viikolle ja keskittyä muihin asioihin. Tämän viimeisen määrittelytoiminnalisuuden toteuttamiseen kuluva aika on vielä täysi mysteeri; ehkä se käy yllättävän nopeasti ja lyhyesti kuten yksikköpropagaatio, tai ehkä edessä on suuri taistelu.

Näin ollen ensi viikolla työ pyörii viimeisen toiminnallisuuden ympärillä. Lisäksi kärkitavoitteena on testaamisen tuominen malliaikataulun mukaiselle tasolle.

Tuntimäärä: 17