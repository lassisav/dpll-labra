# Algoritmit ja tekoäly -harjoitustyö, Helsingin yliopisto

## DPLL-algoritmi Pythonilla, fil. yo Lassi Savolainen

### Viikkoraportti, viikko 3

Kolmannella viikolla toteutettiin minimiversion algoritmista, joka toimii tarpeeksi pienillä syötteillä, ja josta puuttuu tehostamistoimet. Ensimmäisen version luonnin jälkeen työssä on keskitytty tämän version paranteluun, lähinnä poistamalla rekursioita jotka estävät suurempien syötteiden käsittelyn.

Ohjelmassa on nyt DFS-muotoinen puuhaku, eli ns. ytimen ydin on toteutettu. Tulee tosin huomioida, että algoritmin funktiot tarvitsevat vielä parantelua, että se toimii vaikeimmilla mahdollisilla syötteillä.

Tämä viikko oli opettavainen debuggauksen suhteen. Valittu algoritmin luomisen tapa tehdä purkkaratkaisu pohjalle jota parantaa oli luultavasti nopein ja parhaiten työn edistymistä havainnolistava tapa. Tämä kuitenkin johti siihen, että seuraavina askeleina oli tunnistaa koodin virheitä ja valuvikoja rekursiorajailmoitusten ja debuggaustulosteiden avulla.

Vaikeuksia jälleen kolmosviikolla tuotti henkilökohtaisen elämän asettamat aikataululliset haasteet, jotka kuitenkin ovat nyt laajuudessaan takanapäin, ja voin antaa harjoitustyölle sen ansaitseman huomion.

Nelosviikolla aloitetaan testaus- ja toteutusdokumenttien tekeminen, pilkottaan algoritmia yhä enemmän palasiksi niin testauksen kuin luettavuuden helpottamiseksi, sekä parannellaan algoritmin syötekestävyyttä siivoamalla rekursiivisia funktioita ja muita valuvikoja.

Tuntimäärä: 10