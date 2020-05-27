#Напишите скрипт, который разделяет введенный с клавиатуры текст на
#слова и выводит сначала те слова, длина которых превосходит 7
#символов, затем слова размером от 4 до 7 символов, затем – все
#остальные

text=list(input("Введите текст").split(' '))
for word1 in text:
    if len(word1)>=7:
        print(word1)
for word2 in text:
    if 4<=len(word2)<7:
        print(word2)
for word3 in text:
    if len(word3)<4:
        print(word3)
print('Hell0')
