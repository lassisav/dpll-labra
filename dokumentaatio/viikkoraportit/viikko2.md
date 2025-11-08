# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Viikkoraportti, viikko 2

Toisella viikolla tehtiin ohjelmalle runko, sekä toteutettiin algoritmin toteutukselle ja testaukselle keskeisiä funktioita. Nyt ohjelmaan on toteutettu sen vaatimat tietorakenteet (linkitetyt listat), sekä DIMACS CNF -formaattisen datan muuntaminen näihin tietorakenteisiin. Lisäksi on toteutettu tulostusta, jolla algoritmin toimintaa on mielekästä tutkia niin testeillä kuin silmämääräisesti. Ohjelma on nyt myöskin kiedottu alkeelliseen terminaalikäyttöliittymään, mikä mahdollistaa syötteiden monipuolisen valikoinnin.

Ydintehtävä, eli itse DPLL, on vielä lapsenkengissä, mutta on saanut runkonsa ja mm. päättymistarkastuksen. Haaran epäsuotuisuuden toteava funktio on myöskin saanut testauksen.

Viikon työ on ollut opettavaista kertausta monista perusasioista, kuten tiedoston luvusta ja tekstikäyttöliittymästä. Uutena opittuna asiana voidaan mainita, että oletin pääseväni toteuttamaan itse DPLL:ää paljon aikaisemmassa vaiheessa. Tähän mennessä ohjelmaa on kuitenkin ollut mielekkäintä lähestyä algoritmin toteutusta edeltävistä, ja osin seuraavista, osista.

Tämän viikon suurimpana haasteena on ollut aika, jota on kurssin ulkopuolisista syistä ollut riittämättömän vähän. Sama haaste on olemassa myöskin ensi viikolla, minkä jälkeen pystyn antamaan kurssille ns. kaikkeni. Tämä vaikeuttaa työn suoritttamista ja lisää siitä koituvaa stressiä, mutta hopeareunuksena on mahdollistanut suuremman "pureskelun" aiheesta kehityksen alkuvaiheessa.

Ensi viikon alussa tuodaan testaus harjoitustyön ohjeiden mukaiselle tasolla. Tulkintana tästä toimii, että toteutetut funktiot jotka eivät ole runkofunktioita (kuten karsinta) tai kehittäjälle suunnattuja apufunktioita (kuten tulosta_klausuulilista), yksikkötestataa perusteellisesti. Tämän jälkeen toteutetaan algortimin ydin, eli puumainen totuusjakauman haku. Ajan salliessa olemassa olevaa koodia refaktoroidaan uusiin tiedostoihin, ja mahdollisesti aloitetaan yksikköpropagaation toteuttaminen. Algoritmin ydintä toteutetaan alusta asti erillisissä funktioissa testauksen mahdollistamiseksi.

Tuntimäärä: 11
