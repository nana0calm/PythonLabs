# Напишите программу, имитирующую работу банкомата.
# Выберите структуру данных для хранения купюр разного 
# достоинства в заданном количестве.
# При вводе пользователем запрашиваемой суммы денег,
# скрипт должен вывести на консоль количество купюр 
# подходящего достоинства.Если имеющихся денег не хватает, 
# то необходимо напечатать сообщение «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено «5*1000 + 3*100 + 1*50 + 2*10».

Cash_machine={1000:2, 500:8, 100:100, 50:20, 10:100}
amount_requested=input('Введите неободимую сумму! ')
Amount_Requested={}
totalAmount=0

def Totalamount(totalAmount):
    TotalAmount=[key*Cash_machine[key] for key in Cash_machine]
    for num in TotalAmount:
        totalAmount+=num
    print("Всего денег в банкомате: ",totalAmount)
    return totalAmount

def cashDispenser():
    totalAmount1=Totalamount(totalAmount)
    if(int(amount_requested)<int(totalAmount1)):
            thousand=int(int(amount_requested)//1000)
            hundreds=int(int(amount_requested)//100-thousand*10)
            dozens=int(int(amount_requested)//10-thousand*100-hundreds*10)
            Amount_Requested[1000]=thousand
            Amount_Requested[100]=hundreds
            Amount_Requested[10]=dozens
            print("Your money :"+ " {}*{}+".format(1000, Amount_Requested[1000])+" {}*{}+".format(100, Amount_Requested[100])+" {}*{}".format(10, Amount_Requested[10]) )
    else:
        print('Операция не может быть выполнена!')


cashDispenser()
    
    
    
    