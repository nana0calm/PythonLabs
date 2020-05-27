# =============================================================================
# Напишите скрипт, позволяющий искать в заданной директории и в ее
# подпапках файлы-дубликаты на основе сравнения контрольных сумм
# (MD5). Файлы могут иметь одинаковое содержимое, но отличаться
# именами. Скрипт должен вывести группы имен обнаруженных файловдубликатов. 
# =============================================================================

import os
import hashlib

path = r'F:\2Kurs\PyLab2\task2Files'
files = os.listdir(path)
files_count = []
for file in files:
    with open(path + '\\' + file, 'rb') as g:
        data = g.read()
        files_count.append(hashlib.md5(data).hexdigest())

for i in range(len(files) - 1):
    for j in range(i + 1, len(files)):
        if files_count[i] == files_count[j]:
            print(files[i], ' дубликат ', files[j])