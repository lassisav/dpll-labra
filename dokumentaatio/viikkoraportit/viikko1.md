# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Viikkoraportt, viikko 1

Ensimmäisellä viikolla luotiin harjoitustyölle määrittely, alustettiin repositorio, ja tutustuttiin aiheeseen, ja algoritmin eri toteutuksiin ja optimisaatiomahdollisuuksiin.

Ohjelman toteutus aloitetaan toisella viikolla.

Viikon työn koostuessa lähinnä materiaaleihin tutustumisesta, on tällä viikolla opittu toteutuvuusongelmasta ja DPLL-algoritmin toiminnasta perusteellisesti.

Suurimpana epäselvyytenä on ollut eri lähteiden erot algoritmin rakenteessa. Samoja optimisaatiotapoja on joissain lähteissä annettu DPLL:n osana, joissain potentiaalisena algoritmin optimisaationa, ja joissain potentiaalisina datan sievintämismenetelminä ennen varsinaisen algoritmin ajamista. Näiden eroavaisuuksien vuoksi, vaikka apua toteutukseen haetaan useista lähteistä, toteutetaan algortimi niin kuin se on Aalto-yliopiston Declarative Programming -kurssin materiaaleissa määritelty.

Toisen viikon kärkitavoite on datan muuttaminen DIMACS CNF -formaatista linkitetyillä listoilla käsiteltäväksi. Vaikka tämä ei periaatteessa ole harjoitustyön ydintä, on tämä huomattavasti vaivattomampi tapa tuottaa algoritmin testaukselle ja toimivuuden silmämääräiselle arvioinnille tarpeellinen data, kuin sen kovakoodaaminen konstruktorikutsuilla. Tämän jälkeen itse algoritmin toteutus voi alkaa tarkemman toimintasuunnitelman luomisella algoritmin toteuttamisesta. Tavoitteena on saada ainakin osia DPLL-algoritmista ensi viikolla toteutettua.

Tuntimäärä: 15