#Напишите скрипт, который обрабатывает список строк-адресов
#следующим образом: сначала определяет, начинается ли каждая
#строка в списке с префикса «www». Если условие выполняется,
#то скрипт должен вставить  в начало этой строки префикс «http://», 
#а затем проверить, что строка заканчивается на «.com». 
#Если у строки другое окончание, то скрипт должен вставить
#в конец подстроку «.com». В итоге скрипт должен вывести
#на консоль новый список с измененными адресами. 
#Используйте генераторы списков. 


Adresses=['wikipedia.org','vk.com','www.yandex.ru','www.google.com','www.youtube.com']
s1='http://'
s2='.com'

def App(str):
    if str.startswith('www.')==True:
        str=s1+str
    if str.endswith('.com')==False:
        str=str+s2
    return str

def pri():
    print("Строка с добавлением")
    print([App(i) for i in Adresses])


pri()