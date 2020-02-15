# Zad.1

library(ggplot2) 


mpg <- read.csv("/Users/OCTO 00/Documents/GitHub/CDV/R/Warsztaty/mpg.csv") 
?mpg 
input_data <- mpg[,c("displ", "cyl", "cty", "hwy")] 

# macierz
row(mpg) 

library(caTools)

split_cty <- sample.split(input_data[,"cty"], SplitRatio = 0.75) 

split_hwy <- sample.split(input_data[,"hwy"], SplitRatio = 0.75) 


# Obraz macierz
split_cty
split_hwy
training_data <- subset(input_data, split == TRUE) 
test_data <- subset(input_data, split == FALSE) 
model_hwy <- lm(hwy ~ displ + cyl, data = training_data) 
model_cty <- lm(cty ~ displ + cyl, data = training_data) 

summary(model_cty) 
summary(model_hwy)
cty_pred <- predict(model_cty, test_data)
hwy_pred <- predict(model_hwy, test_data)

cty_pred
hwy_pred

# add column
test_data$cty_pred <- cty_pred
test_data$hwy_pred <- hwy_pred

# CTY
nrow(test_data)
ggplot(test_data) +
  geom_point(mapping = aes(x=c(1:59), y=cty),color="blue") +
  geom_point(mapping = aes(x=c(1:59),y=cty_pred),color="red")

# HWY
nrow(test_data)
ggplot(test_data) +
  geom_point(mapping = aes(x=c(1:59), y=hwy),color="blue") +
  geom_point(mapping = aes(x=c(1:59),y=hwy_pred),color="red")


# zad. 2
library(ggplot2)
library(forecast)
library(astsa)
library(forecast)

data <- nottem
plot(nottem)
str(data)
start(data)
end(data)
frequency(data)
class(nottem)
data_decomposed <- decompose(data, type = "multiplicative")
autoplot(data_decomposed)
plot(log(data))

data_diff <- diff(log(data))
plot(data_diff)

acf(diff(log(data)))
pacf(diff(log(data)))

model <- auto.arima(data, trace = T, stepwise = F, approximation = F)
summary(model)
autoplot(model)

model_predykcja <- predict(model, h= 240)
plot(forecast(model, h = 240), ylab = "œrednia miesiêczna temp. (F)", 
     bty = "l", xlab = "Time")
model_forecast <- forecast(model, h=240)
autoplot(model_forecast)

predykcja_new <- model_forecast$mean
data
predykcja_new
