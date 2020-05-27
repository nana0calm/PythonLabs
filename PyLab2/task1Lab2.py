
# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.



filename="rus.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
    file.close()
vocabulary = {letter.lower(): text.count(letter) for letter in text if letter.isalpha()}
for value in sorted(vocabulary.keys(), key=vocabulary.get, reverse=True):
    print(value, '- ', vocabulary[value])