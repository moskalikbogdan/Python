library(ggplot2)
# analiza względem województw z pieciu lat łącznie
dim(dane)
View(dane)

# średnie dla roku
#for(i in 4:12){
# print(tapply(dane[,i],dane[,1],mean))
#}


# średnie w poszczególnych województwach
Sr_miesoWolZKosciazaKg<-tapply(dane[,4],dane[,1],mean)
Sr_serDojrzewZaKg<-tapply(dane[,5],dane[,1],mean)
Sr_jajaKurze<-tapply(dane[,6],dane[,1],mean,na.rm=T)
Sr_masło<-tapply(dane[,7],dane[,1],mean)
Sr_jablkaZaKg<-tapply(dane[,8],dane[,1],mean)
Sr_czyszczenieGarnituru<-tapply(dane[,9],dane[,1],mean)
Sr_polbutyDamskie<-tapply(dane[,10],dane[,1],mean)
Sr_bateriaZlewoz<-tapply(dane[,11],dane[,1],mean)
Sr_wizytaULekarza<-tapply(dane[,12],dane[,1],mean)

# zestawienie średnich:
srednie<-data.frame(woj=as.factor(sort(tab[,2])),Sr_miesoWolZKosciazaKg=Sr_miesoWolZKosciazaKg,Sr_serDojrzewZaKg=Sr_serDojrzewZaKg,
                    Sr_jajaKurze=Sr_jajaKurze,Sr_masło=Sr_masło,Sr_jablkaZaKg=Sr_jablkaZaKg,
                    Sr_czyszczenieGarnituru=Sr_czyszczenieGarnituru,Sr_polbutyDamskie=Sr_polbutyDamskie,
                    Sr_bateriaZlewoz=Sr_bateriaZlewoz,Sr_wizytaULekarza)
#View(srednie)
# wykresy średnich
ggplot(data = srednie, 
       aes(x = woj, 
           y = Sr_miesoWolZKosciazaKg)) + 
  geom_point(color = 'red', 
             size = 1, 
             shape = 15) +
  ggtitle("Województwo v. cena Mięsa Wołowego z kością") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

ggplot(data = srednie, 
       aes(x = woj, 
           y = Sr_miesoWolZKosciazaKg)) +
  geom_bar(stat = 'identity', fill="lightblue", colour = "red") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


# odchylenia standardowe w poszczególnych województwach
Odch_miesoWolZKosciazaKg<-tapply(dane[,4],dane[,1],sd)
Odch_serDojrzewZaKg<-tapply(dane[,5],dane[,1],sd)
Odch_jajaKurze<-tapply(dane[,6],dane[,1],sd,na.rm=T)
Odch_masło<-tapply(dane[,7],dane[,1],sd)
Odch_jablkaZaKg<-tapply(dane[,8],dane[,1],sd)
Odch_czyszczenieGarnituru<-tapply(dane[,9],dane[,1],sd)
Odch_polbutyDamskie<-tapply(dane[,10],dane[,1],sd)
Odch_bateriaZlewoz<-tapply(dane[,11],dane[,1],sd)
Odch_wizytaULekarza<-tapply(dane[,12],dane[,1],sd)

# zestawienie odchyleń standardowych
odchylenia<-data.frame(srednie,Odch_miesoWolZKosciazaKg=Odch_miesoWolZKosciazaKg,Odch_serDojrzewZaKg=Odch_serDojrzewZaKg,
                    Odch_jajaKurze=Odch_jajaKurze,Odch_masło=Odch_masło,Odch_jablkaZaKg=Odch_jablkaZaKg,
                    Odch_czyszczenieGarnituru=Odch_czyszczenieGarnituru,Odch_polbutyDamskie=Odch_polbutyDamskie,
                    Odch_bateriaZlewoz=Odch_bateriaZlewoz,Odch_wizytaULekarza)

# uwzględnienie odchyleń standardowych na wykresach
ggplot(odchylenia, aes(x=woj, y=Sr_miesoWolZKosciazaKg)) + 
  geom_errorbar(aes(ymin=Sr_miesoWolZKosciazaKg-Odch_miesoWolZKosciazaKg, 
                    ymax=Sr_miesoWolZKosciazaKg+Odch_miesoWolZKosciazaKg), 
                width=.1,
                col="blue") +
  geom_point(color = 'red', 
             size = 1, 
             shape = 15) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


ggplot(data = odchylenia, 
       aes(x = woj, 
           y = Sr_miesoWolZKosciazaKg)) +
  geom_bar(stat = 'identity', fill="lightblue", colour = "red") +
  geom_errorbar(aes(ymin=Sr_miesoWolZKosciazaKg - Odch_miesoWolZKosciazaKg, ymax=Sr_miesoWolZKosciazaKg + Odch_miesoWolZKosciazaKg),
              width=.2,                    # Width of the error bars
              col="darkblue") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
