vvod = input("Введите список:")
a = eval(vvod)
v = []
b = []
for i in range(len(a)):
    b.clear()
    for j in range(len(a)):
        if i != j:
            c = abs(a[i] - a[j])  
            b.append((c, a[j]))
    mindist = min(b)[0]
    candidat = [value for dist, value in b if dist == mindist]
    near = min(candidat) if len(candidat) > 1 else candidat[0]
    v.append(near)
print(v) if v else print('Нет нужных элементов')