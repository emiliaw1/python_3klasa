lista = []
dzialanie = True
def avg(lista=[]):
    sum = 0

    for item in lista:
        sum += item["wiek"]
    avg = sum / len(lista)
    return avg


while(dzialanie):
    wybor = int(input("Wybierz opcję: \n"
                      "[1] Dodaj nową osobę \n"
                      "[2] Policz średnią wieku \n"
                      "[3] Wyświetl dane osób \n"
                      "[4] Wyjdź z programu \n"
                      "[5] Zapisz listę do pliku \n"
                      "[6] Wczytaj listę z pliku \n"))
    if wybor == 1:
         imie = input("Podaj imię: ")
         wiek = int(input("Podaj wiek: "))
         osoba = {"imie": imie, "wiek": wiek}
         lista.append(osoba)
         print(lista)
    if wybor == 2:
        print(avg(lista))
    if wybor == 3:
        for item in lista:
            print(item["imie"], item["wiek"])
    if wybor == 4:
        dzialanie = 0

# json i csv
