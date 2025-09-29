def wyszukaj(s, n ,w, m):
    I = []
    ind = 0
    for i in range(n - m + 1):
        czy_wzorzec = True
        for j in range(m):
            if s[i + j] != w[j]:
                czy_wzorzec = False
                break
        if czy_wzorzec:
            I.append(i)
            ind += 1
    return I

s = 'banan'
n = len(s)
w = 'an'
m = len(w)

print(wyszukaj(s, n, w, m))