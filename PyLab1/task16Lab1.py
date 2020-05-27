#Напишите скрипт, который на основе списка
#из 16 названий футбольных команд случайным 
#образом формирует 4 группы по 4 команды,
#а также выводит на консоль календарь
#всех игр (игры должны проходить по средам,
#раз в 2 недели, начиная с 14 сентября текущего года).
#Даты игр необходимо выводить в формате «14/09/2016, 22:45».
#Используйте модули random и itertools. 

from random import shuffle  # смешивание комада
import itertools
from time import strftime
from datetime import timedelta, datetime

format = "%d/%m/%Y, %H:%M"
start = datetime.strptime("14/09/2020, 22:45", format)


football_teams=['Наполи','Арсенал','Зенит','Гамбург',
                'Барселона','Ювентус','Милан','Ливерпуль',
                'Марсель','Динамо','Спартак','Шахтёр',
                'Герта','Динамо','Рубин','Днепр']

shuffle(football_teams)
football_teams=[football_teams[i*4: i*4+4] for i in range(0,4)]
games=[]
for g in football_teams:
    games.append([j for j in itertools.combinations(g,2)])
for i in range(0,6):
   
    print("Игра: ", i+1)
    print(start.strftime(format))
    print(games[0][i])
    print(games[1][i])
    print(games[2][i])
    print(games[3][i])
    print('\n')
    start = start + timedelta(days=14)
print("Чемпионат закончен!")
print(start.strftime(format))
