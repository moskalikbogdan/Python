library(ggplot2)
library(zoo)

# analiza poszczególnych województw po latach województw z pieciu lat łącznie
dim(dane)
View(dane)

malopolska <- dane[dane$woj == "MAŁOPOLSKIE",]
dim(malopolska)
View(malopolska2015)
str(malopolska)

malopolska$data <- as.yearmon(paste(malopolska$mies, malopolska$rok)) 
malopolska<-malopolska[order(malopolska$my),]

malopolska2015<-malopolska[malopolska$rok==2015,]
malopolska2016<-malopolska[malopolska$rok==2016,]
malopolska2017<-malopolska[malopolska$rok==2017,]
malopolska2018<-malopolska[malopolska$rok==2018,]
malopolska2019<-malopolska[malopolska$rok==2019,]

# dane w jednym roku
ggplot(data = malopolska2015, 
       aes(x = data, 
           y = miesoWolZKosciazaKg)) + 
  geom_point(color = 'red', 
             size = 5, 
             shape = 15) +
  ggtitle("Miesiąc v. cena Mięsa Wołowego z kością dla małopolski") +
  scale_x_yearmon() +
  theme(axis.text.x = element_text(angle = 90, hjust = .5))

ggplot(data = malopolska2016, 
       aes(x = data, 
           y = miesoWolZKosciazaKg,)) + 
  geom_point(color = 'red', 
             size = 5, 
             shape = 15) +
  ggtitle("Miesiąc v. cena Mięsa Wołowego z kością dla małopolski") +
  scale_x_yearmon() +
  theme(axis.text.x = element_text(angle = 90, hjust = .5))

# zmiany w czasie
ggplot(data = malopolska, 
       aes(x = data, 
           y = miesoWolZKosciazaKg,
           color =rok)) + 
  geom_point(size = 5, 
             shape = 15) +
  ggtitle("Miesiąc v. cena Mięsa Wołowego z kością dla małopolski") +
  scale_x_yearmon() +
  theme(axis.text.x = element_text(angle = 90, hjust = .5))

# porównanie po latach
ggplot(data = malopolska, 
       aes(x = mon, 
           y = miesoWolZKosciazaKg,
           color =rok,
           group=rok)) + 
  geom_point(size = 5, 
             shape = 15) +
  ggtitle("Miesiąc v. cena Mięsa Wołowego z kością dla małopolski") +
  scale_x_discrete( labels = c("sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paź","lis","gru")) +
  theme(axis.text.x = element_text(angle = 90, hjust = .5))

ggplot(malopolska, aes(x=mon, y=miesoWolZKosciazaKg, fill=mies)) + 
  geom_boxplot(alpha=0.6)
  
  
