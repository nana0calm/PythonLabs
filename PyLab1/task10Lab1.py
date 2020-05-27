#Напишите скрипт, позволяющий определить надежность
#вводимого пользователем пароля. Это задание является
#творческим:алгоритм определения надежности разработайте самостоятельно.

password=input("Введите пароль")
password_strength=0
flag=True
index1=password.find("-")
index2=password.find("_")
index3=password.find("/")
index4=password.find("@")
index5=password.find("!")
false=-1
#длина пароля
if len(password)>16:
    password_strength +=2
elif len(password)>8:
    password_strength +=1
else:
    password_strength -=1
    
# если все символы в пароле все маленькие\все цифры\все большие - понижение надежности пароля
if password.islower():
    password_strength -= 5
    flag = False
if password.isdigit():
    password_strength -= 5
    flag = False
if password.isupper():
   password_strength -= 5
   flag = False    

if(index1!=false and flag is not False):
   password_strength +=1
if(index2!=false and flag is not False):
   password_strength +=1
if(index3!=false and flag is not False):
   password_strength +=1
if(index4!=false and flag is not False):
   password_strength +=1
if(index5!=false and flag is not False):
   password_strength +=1
   
for i in range(len(password)):
    if password[i].isdigit() and flag is not False:
        password_strength +=2
    if password[i].isupper() and flag is not False:
        password_strength +=2
        
if password_strength > 10:
    print('Your password is strength! (' + str(password_strength) + ')')
#234_SECTor-@/52 надежность 23
elif 5 <= password_strength <= 10:
    print('Your password is so-so...(' + str(password_strength) + ')')
# 7Sr5!TT надежность 10
elif password_strength < 5:
    print('Your password is very bad, change it!(' + str(password_strength) + ')')
# 73_sector_73 надежность -4