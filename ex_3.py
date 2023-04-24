# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci) -> [int, int]:
    k = 0  # liczba studentek
    m = 0  # liczba studentów
    
    for student in studenci:
        if student[-1] == 'a':
            k += 1
        else:
            m += 1
            
    return [k, m]
