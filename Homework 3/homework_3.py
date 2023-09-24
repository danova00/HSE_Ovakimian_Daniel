import itertools
import helpers

#1 Создайте ряд функций для проведения математических вычислений:

#a) функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
# Принимает в качестве аргумента число, возвращает его факториал;


def findFact(nm):
    i = 1
    snm = nm
    mp = []
    while(i < nm):
        snm *= i
        i+=1
        mp.append(snm)
    print("The factorial of "+str(nm)+" is "+str(mp[len(mp) - 1]))

#findFact(5)
#findFact(10)

#b) поиск наибольшего числа из трёх.
# Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них

def fndGret(a, b, c):
    myNmb= [a, b, c]
    for i in myNmb:
        if(i >=myNmb[0] and i >=myNmb[1] and i >=myNmb[2]):
            print("The biggest number is " +str(i))

#fndGret(5772, 33, 33)


#c) расчёт площади прямоугольного треугольника.
# Принимает в качестве аргумента размер двух катетов треугольника. Возвращает площадь треугольника.

def sSquare(a, b):
    s = (a*b)%2
    print("The square is equal "+str(a))

#sSquare(15, 7)



#2) Создайте функцию для генерации текста с адресом суда.
# Функция должна по шаблону генерировать шапку для процессуальных документов с реквизитами сторон для отправки.

p1 = helpers.courtsData()
repHead =  {'full_name': 'общество с ограниченной ответственностью " ПРОДСЕРВИС "', 'short_name': 'ООО " ПРОДСЕРВИС "',
     'inn': '2465081302', 'ogrn': '1042402640125', 'region': 'Красноярский край', 'category': 'Обычная организация',
     'category_code': 'SimpleOrganization', 'bankruptcy_id': '12182', 'case_number': 'А33-2794/2011',
     'address': '660020, КРАЙ КРАСНОЯРСКИЙ, Г. КРАСНОЯРСК, УЛ. 7-Й КМ ЕНИСЕЙСКОГО ТРАКТА, ТЕРРИТОРИЯ ЗАО "ТЗБ КРАЙПОТРЕБСОЮЗА"'}

def genHead(caseNumb, rCourts, resp):

    l=0
    # У  некоторых респондентов не было ключа "case_number", мне было лень перебирать вручную, поэтому я отсортировал их.

    while (l < len(rCourts)):
        if (rCourts[l]["court_code"] == caseNumb[0:3]):
            print(f'\nВ {rCourts[l]["court_name"]}:' +
                    f'\nАдрес: {rCourts[l]["court_address"]}:' +
                    f'\nИстец: Самохин Даниил Дмитриевич' +
                    f'\nИНН 1236182357 ОГРНИП 218431927812733' +
                    f'\nАдрес: 123534, г. Москва, ул. Водников, 13' +
                    f'\nОтветчик: {resp["short_name"]}' +
                    f'\nИНН {resp["inn"]} ОГРН {resp["ogrn"]}' +
                    f'\nАдрес: {resp["address"]}' +
                    "\n" +f'\nНомер дела {caseNumb}')
        l += 1




#Создайте ещё одну функцию, которая принимает в себя список словарей с данными ответчика.
# Используйте цикл for для генерации всех возможных вариантов этой шапки с вызовом первой функции внутри тела цикла for
# и выводом данных, которые она возвращает в консоль.

def genHeadMod(rParts, rCourts):
    l = 0
    key = "case_number"
    partn = []
    for c in rParts:
        if key in c:
            partn.append(c)

# У  некоторых респондентов не было ключа "case_number", мне было лень перебирать вручную, поэтому я отсортировал их.

    while(l < len(partn)):
      for i in rCourts:
         if(partn[l]["case_number"][0:3] == i["court_code"]):
            print(f'\nВ {i["court_name"]}:'+
                  f'\nАдрес: {i["court_address"]}:' +
                  f'\nИстец: Самохин Даниил Дмитриевич' +
                  f'\nИНН 1236182357 ОГРНИП 218431927812733' +
                  f'\nАдрес: 123534, г. Москва, ул. Водников, 13'+
                  f'\nОтветчик: {partn[l]["short_name"]}' +
                  f'\nИНН {partn[l]["inn"]} ОГРН {partn[l]["ogrn"]}' +
                  f'\nАдрес: {partn[l]["address"]}' +
                  "\n"+
                  f'\nНомер дела {partn[l]["case_number"]}')
      l += 1


#Создайте ещё одну функцию, которая принимает в себя список словарей с данными ответчика.
# Используйте цикл for для генерации всех возможных вариантов этой шапки с вызовом первой функции внутри тела цикла for
# и выводом данных, которые она возвращает в консоль. Решение 2
def genHeadMod2(rParts, rCourts):
    l = 0
    key = "case_number"
    partn = []
    for c in rParts:
        if key in c:
            partn.append(c)

    for i in partn:
        genHead(i["case_number"], rCourts, i)







#genHead("А13-2909/2021", p1.courts, repHead)
#genHeadMod(p1.repondents, p1.courts)
#genHeadMod2(p1.repondents, p1.courts)
