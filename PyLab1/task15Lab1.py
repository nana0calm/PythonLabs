#Напишите параметризированный декоратор pre_process,
#который осуществляет предварительную обработку
#(цифровую фильтрацию) списка по алгоритму:
#     s[i] = s[i]–a∙s[i–1]. 
#Параметр а можно задать в коде (по умолчанию равен 0.97). 
# Пример кода: 
# 
#@pre_process(a=0.93) 
#def plot_signal(s):   
#    for sample in s:    
#        print(sample) 


def pre_process(a=0.93):
    def decorator(func):
        def wrap(*args):
            s=args[0]
            for i in range(1, len(s)):
                s[i]=s[i]-a*s[i-1]
            print('a= ', a)
            func(s)
           
        return wrap
      
    return decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)
        

array=[i for i in range(20)]
plot_signal(array)
        