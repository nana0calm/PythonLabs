#Напишите собственную версию генератора enumerate
#под названием extra_enumerate. Пример вызова: 
# 
#for i, elem, cum, frac in extra_enumerate(x):
#    print(elem, cum, frac) 
#
#В переменной cum хранится накопленная сумма 
#на момент текущей итерации, в переменной F
#frac – доля накопленной суммы от общей суммы
#на момент текущей итерации. 
#Например, для списка x=[1,3,4,2] вывод будет таким: 
# 
#  (1, 1, 0.1)    (3, 4, 0.4)    (4, 8, 0.8)    (2, 10, 1)

def extra_enumerate(x):
    cum=0
    frac=0
    amount=0
    for step in x:
        amount +=step
    for j in range(len(x)):
        elem=x[j]
        cum+=x[j]
        frac= round(cum/amount,1)
        yield j, elem, cum, frac
    
x=[x for x in range(5)]
print(x)
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
    