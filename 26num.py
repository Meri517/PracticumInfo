'''
#12933
f = open('26_12933.txt')
n, k = [int(x) for x in f.readline().split()]
a = []
for i in range(1, n + 1):
    ts, to = [int(x) for x in f.readline().split()]
    a.append((ts, i, 's'))
    a.append((to, i, 'o'))
a.sort()
#print(n, k)
#print(a)
lenta = [0] * (n + 1)
ks = 0
spo = set()
start, end = 1, n
for t, num, op in a:
    if num not in spo:
        spo.add(num)
        if op == 's':
            lenta[start] = num
            start += 1
            ks += 1
        else:
            lenta[end] = num
            end -= 1
print(ks)
print(lenta[k])

'''








# КЕГЭ №12933
'''
f = open('26_12933.txt')
n, k = [int(x) for x in f.readline().split()] # прочитали и разредали, получили 2 строчки состоящие из цифр
a = []
for i in range(1, n + 1): # n - кол-во иттераций; перебором захватываем всё
    ts, to = [int(x) for x in f.readline().split()] # ts - время шлифовки, to - время окрашивания
    a.append((ts, i, 's')) # делаем картежи s - шлифовка, o - окрашивание
    a.append((to, i, 'o'))
a.sort() # время по возврастанию
lenta = [0] * (n + 1) # метод для выведения по номеру места, создание ленты
ks = 0 # кол-во отшлифованных деталей
spo = set() # создаём множество окрашнных деталей
start, end = 1, n # start - первое место на ленте, end - последнее место на ленте
for t, id, op in a: # t - время , id - айди, op - операция
    if id not in spo: # проверили есть ли деталь
        spo.add(id) # добавляет окрашенные детали
        if op == 's': # если деталь для шлифовки
            lenta[start] = id # ставим этот элемент в начало ленты
            start += 1
            ks += 1
        else: # если деталь для окрашивания
            lenta[end] = id # ставим этот элемент в конец ленты
            end -= 1 # -= потому что идём с конца
print(ks, lenta[k])
'''







# КЕГЭ №13101

'''
f = open('26_13101.txt')
n = int(f.readline())
a = []
for i in f:
    st, t, o =  [int(x) for x in i.split()] # st - начало время обслуживания, t - время обслуживания, o - окно
    a.append((st, t, o)) # создаём картеж
a.sort()
okno1 = [] # первая очередь
okno2 = [] # вторая очередь
kn = 0 # счёчтик обслуживаемых
k2 = 0 # счётчик второго окна
for st, t, o in a:
    okno1 = [x for x in okno1 if x > st]
    okno2 = [x for x in okno2 if x > st]
    if o == 1 or (o == 0 and len(okno1) <= len(okno2)):
        if len(okno1) >= 14:
            kn += 1
            continue
        if len(okno1) == 0:
            okno1 += [st + t]
        else:
            okno1 +=[max(okno1) + t]

    else:
        if len(okno2) >= 14:
            kn += 1
            continue
        k2 += 1
        if len(okno2) == 0:
            okno2 += [st + t]
        else:
            okno2 += [max(okno2) + t]
print(k2, kn)

'''






#КЕГЭ №12478

f = open('26_12478.txt')
n = (f.readline())
a = []
start_ege = 1000
end_ege = 18000
for i in f:
    start, end= [int(x) for x in i.split()] # st - время начала работы, t - время окончания работы
    a.append((start, end)) # создаём картеж
a.sort()

tvr = [] # время всей работы 1 чела

for start, end in a:
    tvr += [end - start + 1]

Uje_rabotayut = []




    okno1 = [x for x in okno1 if x > st]
    okno2 = [x for x in okno2 if x > st]
    if o == 1 or (o == 0 and len(okno1) <= len(okno2)):
        if len(okno1) >= 14:
            kn += 1
            continue
        if len(okno1) == 0:
            okno1 += [st + t]
        else:
            okno1 +=[max(okno1) + t]



print(a[0])
print(tvr)