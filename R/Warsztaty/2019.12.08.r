# 20191208
# Zad.1 
m <- matrix(1:10000, nrow = 100, ncol = 100)
# Zad.1.2
m <- ifelse(m > 5000, 2*m, m)
# zad.1.3
sum(m[5:6,60]+m[5:6,61]+m[5:6,62])

# zad. 2
# Wektor "names"
imiona <- c("Andrew", "Catherine", "Mathiew")
# Wektor "ages"
wiek <- c(18,24,28)
# Rama danych "osoby" z wektorem "names" oraz "ages"
osoby <- data.frame(imiona, wiek)
# zmienna ze œredni¹ wieku
average <- mean(wiek)

# zad. 3

# Pytanie o liczbe
nterms = as.integer(readline(prompt="Podaj liczbê dla której obliczê ci¹g Fibonnaciego? "))
n1 = 0
n2 = 1
count = 2
# Sprawdzenie
if(nterms <= 0) {
  print("proszê o podanie liczby dodatniej")
} else {
  if(nterms == 1) {
    print("Sekwencja Fibonacciego: ")
    print(n1)
  } else {
    print("Sekwencja Fibonacciego: ")
    print(n1)
    print(n2)
    while(count < nterms) {
      nth = n1 + n2
      print(nth)
      # Aktualizacja zmiennych
      n1 = n2
      n2 = nth
      count = count + 1
    }
  }
}

Zad.4 
# normy
niedowaga <- seq(16.00, 18.49, 0.01)
norma <- seq(18.50, 24.99, 0.01)
nadwaga <- seq(25.00, 30.00, 0.01)
print(niedowaga)
print(norma)
print(nadwaga)
#Pytanie
waga = as.integer(readline(prompt="Podaj wagê w kg: "))
wzrost = as.integer(readline(prompt="Podaj wysokoœæ w cm: "))
#BMI
bmi <- waga/wzrost**2 * 10000
bmi_round <-round(bmi, digits = 2)
print(bmi_round)
for(nied in niedowaga){
  if (bmi_round == nied) print("Niedowaga")
}
for (norm in norma){
  if (bmi_round == norm) print("w normie :)")
}
for (nad in nadwaga){
  if (bmi_round == norm) print("Nadwaga")
}
