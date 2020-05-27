# =============================================================================
# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен.
# =============================================================================

import os
from glob import glob
import os.path

path=r'F:\2Kurs\PyLab2\task3Files'
os.chdir(path)

musicFiles=glob('*.mp3')

nameFiles=list(filter(None, [text.replace('\n', '') if text is not 'music.txt' else None for text in open('music.txt', 'r', encoding='utf8')]))

count_music=0
Done=False

for i in range(len(musicFiles)):
    try:
        os.rename(musicFiles[i], nameFiles[i])
        if count_music==len(musicFiles)-1:
            Done=True
        count_music +=1
    except Exception as e:
        print('Error file ' + str(count_music) + ': ', e.args)
        
if Done:
    print('All files renamed')
else:
    print('Error')