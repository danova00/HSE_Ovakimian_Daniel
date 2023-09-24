import json
from currencies_helper import ParserCBRF
import os




class Actions:

    def get_currency_value(self):

        curcode = input('Чтобы получить курс валюты, пожалуйста, введите код валюты:  ')
        while(str(type(curcode)) != "<class 'str'>"):
             curcode  = input('Пожалуйста, введите корректный код валюты: ')

        f = open('parsed_data/currencies.json')
        data = json.load(f)

        res = False
        for i in data:
            if i[1] == curcode:
                res = True
                break
        if res == True:
             print(i[3] + ' покупается по курсу ' + i[4])
        else:
             print('Введённой вами валюты нет в списке')


    def get_currency_info(self):

        curcode = input('Чтобы получить информацию о валюте, пожалуйста, введите код валюты:  ')
        while(str(type(curcode)) != "<class 'str'>"):
             curcode  = input('Пожалуйста, введите корректный код валюты: ')

        f = open('parsed_data/currencies.json')
        data = json.load(f)

        res = False
        for i in data:
            if i[1] == curcode:
                res = True
                break
        if res == True:
             print('Цифр. код: '+ i[0] +'; Букв. код: ' + i[1] + '; Единиц: ' + i[2] + '; Валюта: ' + i[3] + '; Курс: ' + i[4])
        else:
             print('Введённой вами валюты нет в списке')


    def clear_mess(self):
        os.remove("currencies.csv")
        os.remove("parsed_data/currenciesed.csv")
        os.remove("parsed_data/currencies.json")




par = ParserCBRF()
ac =Actions()

par.start()

par.serialize()
par.deserialize()
ac.get_currency_value()
ac.get_currency_info()

#ac.clear_mess()
