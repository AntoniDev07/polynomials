n = int(input())
a = []
a = list(map(int, input().split()))
a0 = a[-1]
an = a[0]


def calkowite(a0):
    dzielniki_cal = []
    for i in range(1, abs(a0) + 1):
        if a0 % i == 0:
            dzielniki_cal.append(i)
            dzielniki_cal.append(-i)
    return dzielniki_cal


def wymierne(a0, an):
    dzielniki_a0 = calkowite(a0)
    dzielniki_an = calkowite(an)
    kandydaci = []
    for i in dzielniki_a0:
        for j in dzielniki_an:
            kandydaci.append(i / j)
    return kandydaci


def wartosc(a, x):
    wynik = 0

    for i in range(len(a)):
        wynik += a[i] * (x ** (n - i))
    return wynik


kandydaci_wymierne = wymierne(a0, an)
pierwiastki = set()

for kandydat in kandydaci_wymierne:
    if abs(wartosc(a, kandydat)) < 1e-9:
        pierwiastki.add(kandydat)


print(calkowite(a0))
print(wymierne(a0, an))
print(pierwiastki)
