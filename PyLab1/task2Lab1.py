#Написать скрипт, который выводит на экран «True», если элементы
#программно задаваемого списка представляют собой возрастающую
#последовательность, иначе – «False».

    
numbers=[1,3,5, 16, 11, 15]
res = True
for i in range(1,len(numbers)):
    if (numbers[i-1]>numbers[i]):
        res = False
        break
print(res)