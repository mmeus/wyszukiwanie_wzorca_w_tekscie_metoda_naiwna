dane = [w.strip() for w in open('slowa1.txt').readlines()]

wakacje = 'wakacje'
licznik = 0

for s in dane:
    i = 0
    licznik = 0
    for z in s:
        if z == wakacje[i]:
            i += 1
        if i == len(wakacje):
            i = 0
            licznik += 1
    print(len(s) - licznik * len(wakacje))