# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"

studenci_1 = ["Anna", "Jakub", "Piotr", "Jan"]
studenci_2 = ["Anna Patera", "Anna Piątek", "Piotr Kawa", "Jan Mały", "Barbara Wrzesień"]
studenci_3 = [17, "Anna Patera", "Anna Piątek", 0, "Piotr Kawa", "Jan Mały", "Barbara Wrzesień"]
studenci_4 = [17, "Anna Patera", "Anna Piątek", 0, "Piotr Kawa", "Katarzyna", "Bartosz"]

def policz_studentow_plec(studenci):
    k = 0
    m = 0
    
    for student in studenci:
        if isinstance(student,str):
            if student[-1] == 'a':
                k += 1
            else:
                m += 1
            
    return [k, m]

policz_studentow_plec(studenci_1)
policz_studentow_plec(studenci_2)
policz_studentow_plec(studenci_3)
policz_studentow_plec(studenci_4)



