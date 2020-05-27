# =============================================================================
# Напишите скрипт, который позволяет ввести с клавиатуры имя
# текстового файла, найти в нем с помощью регулярных выражений все
# подстроки определенного вида, в соответствии с вариантом:
# Вариант 3: найдите все IPv4-адреса – подстроки вида «192.168.5.48».
# =============================================================================

import re

pattern=re.compile("\d{3}.\d{3}.\d+.\d{2}")
content=''
matches=[]
count_str=[1,2,3,4,5]
posit=0
i=0
j=1
path=input('Введите название вашего файла')
try:
    file = open('F:\\2Kurs\\PyLab2\\'+ path, 'r', encoding='UTF-8')
    content = file.read()
    file.close()
except FileNotFoundError as e:
    print('File does not exist. ', e.args)
result=pattern.findall(content)

while j<len(result):
    for i in result:
        posit=pattern.search(content)
        info="Строка {0}, позиция {1} : найдено {2}".format(j, posit.start(), i)
        j+=1
        print(info)
