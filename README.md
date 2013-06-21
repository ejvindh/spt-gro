Siden Athas-crew'et i sin tid lavede den første udgave af dette program til at læse Gyldendals ordbøger på Linux, har Gyldendal udvidet sortimentet, således at man nu kan få ordbøger til engelsk, tysk, fransk, spansk, italiensk, svensk, norsk, engelsk (fag/teknik), stor dansk-engelsk, stor engelsk-dansk, retskrivning, fremmedord, synonymer, Dansk (http://download.ordbog.gyldendal.dk/). Nogle af disse kunne uden store ændringer indlemmes i det gamle script, men ikke alle.

Denne nye version er en opdatering af gui-versionen af det oprindelige program (jeg har ikke rørt ved ordbog.py). Programmet forudsætter python installeret sammen med pygtk (http://pygtk.org/).

For at køre programmet, skal du

(1) Sikre dig, at du har Python og pygtk installeret.

(2) Kopiere ordbogsfilerne over i /data/-mappen. For at finde disse filer, er du nødt til at have installeret den pågældende ordbog på en windows-computer. Herefter kan du finde dem i mappen %Program Files%Gyldendal/Røde Ordbøger/data -- det drejer sig om to filer for hver ordbog, og de har fil-endelserne *.dat og *.gdd.

(3) Åbne filen main.py med en tekst-editor, og i toppen af filen, skal du fjerne #-tegnene ud for de ordbøger, som du har rådighed over. Det drejer sig om 6 #-tegn for hver ordbog -- hvis du har den tyske ordbog, ser første linie således ud:
'de': {

...sidste linie således:
},

(4) Så er du klar til at køre programmet. Det startes med kommandoen:
python main.py

God arbejdslyst. Ligesom Athas vil jeg også gerne understrege, at det er strengt ulovligt at piratkopiere ordbogen. Hvis du kan lide sproget, så køb det! Dette program er udelukkende tænkt til at hjælpe folk til at kunne migrere til Linux -- uden at skulle miste adgangen til deres legalt erhvervede software.

//ejvindh
