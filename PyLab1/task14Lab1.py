#Напишите декоратор non_empty, который дополнительно 
#проверяет списковый результат любой функции: 
#если в нем содержатся пустые строки или значение None, 
#то они удаляются. Пример кода: 
# 
#   @non_empty def get_pages():
#       return ['chapter1', '', 'contents', '', 'line1'] 

def non_empty(func):
    def decor():
        res = func()
        return list(filter(None, res))

    return decor


@non_empty  
def get_pages():
    return [None, 'chapter1', '', None, 'contents', '', 'line1', None]


print(get_pages())

