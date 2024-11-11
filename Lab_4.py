#Zdanie 1

moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(moja_lista)
moja_lista.append(100)
print(moja_lista)

#Zdanie 2
#a)
imiona = ["Ola", "Jula", "Bartek", "Janusz"]
imiona.sort()
print("Po sortowaniu:", imiona)

imiona.append("Ewa")
imiona.append("Filip")
print("Dodane osoby:",imiona)
usunienta_osoba = imiona.pop()
print("Usunienta osoba - ", usunienta_osoba)

imiona.insert(2, 'Bart')
print("Po dodaniu osoby na index 2:", imiona)

imiona.reverse()
print("Odwrócona kolejność:", imiona)

#Zdanie 3

imie = input("Podaj swoje imię:")
print("Witaj", imie)

wiek = input("Podaj swój wiek:")
print("Twój wiek", wiek)

imię = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko:" )
inicjaly = imię[0].upper()+ "." + nazwisko[0].upper()+"."
print("Twoje inicjaly",inicjaly)

lancuch = input("Wpisz tekst:")
print(lancuch * 5)

lancuch1 = input("Wpisz tekst:")
lancuch2 = input("Wpisz tekst:")
print(lancuch1 +" "+ lancuch2)

#Zad 4
zdanie = input("Podaj zdanie: ")
alfabet = 'a, ą, b, c, ć, d, e, ę, f, g, h, i, j, k, l, ł, m, n, o, ó, p, q, r, s, ś, t, u, v, w, x, y, z, ź, ż'
litery_w_zdaniu = [char.lower() for char in zdanie if char.isalpha()]
litery_posortowane = sorted(litery_w_zdaniu)

print("Posortowane litery w zdaniu:")
print("".join(litery_posortowane))

unikalne_litery = set(litery_posortowane)
brakujace_litery = [litera for litera in alfabet if litera not in unikalne_litery]

print("Brakujące litery alfabetu:")
print("".join(brakujace_litery))


#Zad 5
dni_tygodnia = ["poniedziałek.", "Wtorek", "środa", "czwartek","piątek","sobota","niedziela"]
print(dni_tygodnia)

#Zad 6
owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan','malina')
count_banan = owoce.count("banan")
print('zliczenia wystąpień elementu banan wkrotce:', count_banan )

#Zad7

moja_krotka= (10, 2, 6, 6, 9, 13, 0,1)
moja_krotka = list(moja_krotka)
moja_krotka.sort()
sorted_krotka = tuple(moja_krotka)
print("Posortowana krotka:", sorted_krotka)

#Zad8
stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

ilość_stopnii= len(stopnie) 
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie

print(ilość_stopnii)
print(Major_index)
print(Pułkownik_wstepowanie)

#Zdanie 9

lista_zakupow = {
    "Chleb": 3.50,
    "Mleko": 2.30,
    "Jabłka": 4.00,
    "Masło": 4.60,
    "Kowbaski": 9.20
}
print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(artykul,kwota, "PLN")

wydatki = sum(lista_zakupow.values())

print("\nPodsumowanie wydatków:", wydatki, "PLN")
