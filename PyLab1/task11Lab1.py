# Напишите генератор frange как аналог range() с дробным шагом.
#Пример вызова:       
#for x in frange(1, 5, 0.1):  print(x) 
 # выводит     1    1.1    1.2    1.3    1.4   …   4.9 

def frange(start, end, step):
    while start<=end-0.2:
        start +=step
        yield start

for x in frange(1, 5, 0.1):
    print(round(x,1))
