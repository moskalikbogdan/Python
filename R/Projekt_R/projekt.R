#wczytanie danych
tab<-read.csv(file="CENY_2917_CTAB_20200124233110.csv",sep=";",dec=",",encoding = "UTF-8")
View(tab)
#nazwy danych
names(tab)
names(tab)[1:8]
#zmiany nazwy kolumn !!
#names(tab)[3:7]<-paste0("miesoWolZKosciazaKg",c("2015","2016","2017","2018","2019"))
#names(tab)[8:12]<-paste0("serDojrzewZaKg",c("2015","2016","2017","2018","2019"))
#names(tab)[13:17]<-paste0("jajKurze",c("2015","2016","2017","2018","2019"))
#names(tab)[18:22]<-paste0("Masło",c("2015","2016","2017","2018","2019"))
#names(tab)[23:27]<-paste0("jablkaZaKg",c("2015","2016","2017","2018","2019"))
#names(tab)[28:32]<-paste0("CzyszczenieGarnituru",c("2015","2016","2017","2018","2019"))
#names(tab)[33:37]<-paste0("PolbutyDamskie",c("2015","2016","2017","2018","2019"))
#names(tab)[38:42]<-paste0("BateriaZlewoz",c("2015","2016","2017","2018","2019"))
#names(tab)[43:47]<-paste0("WizytaULekarza",c("2015","2016","2017","2018","2019"))


#śmieci
#woj<-rep(c("Polska","dolnoslaskie","kujawsko-pomorskie","lubelskie","lubuskie","lodzkie","malopolskie",
#  "mazowieckie","opolskie","podkarpackie","podlaskie","pomorskie","slaskie","swietokrzyskie",
#  "warminsko-mazurskie","wielkopolskie","zachodniopomorskie"),12*45)
#mies<-rep(c("sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paz","lis","gru"),each=85)
#miesoWolZKosciazaKg<-c(tab[,3],tab[,4],tab[,5],tab[,6],tab[,7])

#head(mies,20)
#sum(mies=="sty")
#names(tab)[48:52]<-paste0("WizytaULekarza",c("2015","2016","2017","2018","2019"))

#nazy województw
tab[,2]
#zamiana z typu czynnikowego na znakowy
tab[,2]<-as.character(tab[,2])

# powtarzalność dla lat 2015-2019
woj<-rep(tab[,2],5)
# powtarzalność dla 12 miesięcy
woj1<-rep(woj,12) 
# długość wektora
length(woj1)
# oznaczenie roku w jednej zmiennej dla każdego województwa i dla Poski
rok<-rep(c("2015","2016","2017","2018","2019"),each=17)
#length(rok)
# powtarzalność dla 12 miesięcy
rok1<-rep(rok,12)
# długość wektora
length(rok1)

# oznaczenie miesięcy;
mon<-factor(mies, levels=c("sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paź","lis","gru"), ordered = TRUE)
mies<-rep(c("sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paź","lis","gru"),each=85)

#zebranie danych z tabeli do odpowiednich kolumn
j=0
miesoWolZKosciazaKg<-c(tab[,j+3],tab[,j+4],tab[,j+5],tab[,j+6],tab[,j+7])
serDojrzewZaKg<-c(tab[,j+8],tab[,j+9],tab[,j+10],tab[,j+11],tab[,j+12])
jajaKurze<-c(tab[,j+13],tab[,j+14],tab[,j+15],tab[,j+16],tab[,j+17])
Masło<-c(tab[,j+18],tab[,j+19],tab[,j+20],tab[,j+21],tab[,j+22])
jablkaZaKg<-c(tab[,j+23],tab[,j+24],tab[,j+25],tab[,j+26],tab[,j+27])
CzyszczenieGarnituru<-c(tab[,j+28],tab[,j+29],tab[,j+30],tab[,j+31],tab[,j+32])
PolbutyDamskie<-c(tab[,j+33],tab[,j+34],tab[,j+35],tab[,j+36],tab[,j+37])
BateriaZlewoz<-c(tab[,j+38],tab[,j+39],tab[,j+40],tab[,j+41],tab[,j+42])
WizytaULekarza<-c(tab[,j+43],tab[,j+44],tab[,j+45],tab[,j+46],tab[,j+47])

j=45
miesoWolZKosciazaKg<-c(miesoWolZKosciazaKg,tab[,j+3],tab[,j+4],tab[,j+5],tab[,j+6],tab[,j+7])
serDojrzewZaKg<-c(serDojrzewZaKg,tab[,j+8],tab[,j+9],tab[,j+10],tab[,j+11],tab[,j+12])
jajaKurze<-c(jajaKurze,tab[,j+13],tab[,j+14],tab[,j+15],tab[,j+16],tab[,j+17])
Masło<-c(Masło,tab[,j+18],tab[,j+19],tab[,j+20],tab[,j+21],tab[,j+22])
jablkaZaKg<-c(jablkaZaKg,tab[,j+23],tab[,j+24],tab[,j+25],tab[,j+26],tab[,j+27])
CzyszczenieGarnituru<-c(CzyszczenieGarnituru,tab[,j+28],tab[,j+29],tab[,j+30],tab[,j+31],tab[,j+32])
PolbutyDamskie<-c(PolbutyDamskie,tab[,j+33],tab[,j+34],tab[,j+35],tab[,j+36],tab[,j+37])
BateriaZlewoz<-c(BateriaZlewoz,tab[,j+38],tab[,j+39],tab[,j+40],tab[,j+41],tab[,j+42])
WizytaULekarza<-c(WizytaULekarza,tab[,j+43],tab[,j+44],tab[,j+45],tab[,j+46],tab[,j+47])

j=11*45  # od 2 do 11
miesoWolZKosciazaKg<-c(miesoWolZKosciazaKg,tab[,j+3],tab[,j+4],tab[,j+5],tab[,j+6],tab[,j+7])
serDojrzewZaKg<-c(serDojrzewZaKg,tab[,j+8],tab[,j+9],tab[,j+10],tab[,j+11],tab[,j+12])
jajaKurze<-c(jajaKurze,tab[,j+13],tab[,j+14],tab[,j+15],tab[,j+16],tab[,j+17])
Masło<-c(Masło,tab[,j+18],tab[,j+19],tab[,j+20],tab[,j+21],tab[,j+22])
jablkaZaKg<-c(jablkaZaKg,tab[,j+23],tab[,j+24],tab[,j+25],tab[,j+26],tab[,j+27])
CzyszczenieGarnituru<-c(CzyszczenieGarnituru,tab[,j+28],tab[,j+29],tab[,j+30],tab[,j+31],tab[,j+32])
PolbutyDamskie<-c(PolbutyDamskie,tab[,j+33],tab[,j+34],tab[,j+35],tab[,j+36],tab[,j+37])
BateriaZlewoz<-c(BateriaZlewoz,tab[,j+38],tab[,j+39],tab[,j+40],tab[,j+41],tab[,j+42])
WizytaULekarza<-c(WizytaULekarza,tab[,j+43],tab[,j+44],tab[,j+45],tab[,j+46],tab[,j+47])

# tworzenie ramki danych z danymi
dane<-data.frame(woj=woj1, rok=rok1, mies=mies, mon=mon, miesoWolZKosciazaKg=miesoWolZKosciazaKg, serDojrzewZaKg=serDojrzewZaKg,
                 jajaKurze=jajaKurze, masło=Masło, jablkaZaKg=jablkaZaKg, czyszczenieGarnituru=CzyszczenieGarnituru,
                 polbutyDamskie=PolbutyDamskie, bateriaZlewoz=BateriaZlewoz, wizytaULekarza=WizytaULekarza)
dim(dane)

#Analiza danych w osobnym skrypcie

