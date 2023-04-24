# Zaokraglij do dwoch miejsc po przecinku
liczba_1 = 0.59
potega_1 = 2
liczba_2 = 10
potega_2 = 3
def oblicz_potega(liczba, potega):
    wynik = liczba ** potega
    wynik_zaokraglony=round(wynik, 2)
    return print(wynik_zaokraglony)

oblicz_potega(liczba_1, potega_1)
oblicz_potega(liczba_2, potega_2)