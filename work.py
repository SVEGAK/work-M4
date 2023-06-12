# # import random 


# # comp_num = random.randint(1, 1000)
# # user_num = int(input(' угадай число от 1 до 1000   '))
# # diff = user_num - comp_num
# # for i in range(3): 
# #     user_num = int(input(' угадай число от 1 до 1000   '))
# #     diff = user_num - comp_num

# # if user_num == comp_num:
# #     print("молодец угадал победа победа!!!!!!!!!!")
# # elif diff  == 1 or diff == -1 :
# #     print('почти угадал могешь')
# # else: 
# #     print('ты не угадал')



# # temp =  int(input('введите температуру '))

# # if temp > 25 and temp <= 30:
# #     print('На улице очень жарко ')
# # elif temp  == temp >20 and temp <=25:
# #     print('На улице  жарко ')
# # elif temp  == temp >15 and temp <=20:
# #     print( 'На улице тепло')
# # elif temp  == temp >10 and temp <=15:
# #     print('На улице прохладно ')
# # elif temp == temp > 0 and temp <=10:
# #     print('На улице холодно ')
# # elif temp == temp > -25 and temp <0:
# #     print('На улице очень холодно ')
# # else:
# #     print('упс, вы ввели некорректную температуру!')






# # import random 
# # user_choice = str(input('user,выберите орла или решку!  '))
# # first = ['Орел', 'решка' ]
# # comp_choice = random.choice(first)
# # if comp_choice.lower() == user_choice.lower():
# #     print('User, вы угадали', "это была   "  + str(comp_choice ))
# # else:
# #     print('Упс! неудача, ничего в следующий раз повезет', "компьютер загадал: " + str(comp_choice))




# # N = [-1, 14, 27, 36, 42,23214, 0,2, -500, 543, 0,24, 968, 762, 123, -5, -8, -242]
# # lone = len(N) 
# # for i in range(1, lone): 
# #     for k in range(lone - 1, i - 1, -1): 
# #          if N[k - 1] > N[k]: 
# #             N[k - 1], N[k] = N[k], N[k - 1] 
# # print(*N)



# # -----------------------------------------------------------------------------------------------------------------------------------------
# # 18.11.22



# # english_dict = {
# #     'яблоко':'apple',
# #     'молоко': 'milk',
# #     'кот': 'cat'
# # }
# # # print(english_dict['кот'])
# # # или
# # word = input('введите слово на русском: ').lower()
# # if word in english_dict:
# #     print(f'{word} на английском языке будет {english_dict.get(word)}')
# # else:
# #     print('Такого слова нет в словаре')


# # films_dict = {
# #     'Начало':'Леонардо ди каприо',
# #     'пираты карибского моря':'джони депп',
# #     'Миссия не выполнима':'Том круз'
# # }
# # favorite_actor = 'Леонардо ди каприо'
# # film = input('Какой фильм вы собираетесь посмотреть ')
# # actor = films_dict.get(film)
# # if actor == favorite_actor:
# #     print('Этот фильм стоит посмотреть')
# # else:
# #     print('фильм фу')



# # films_dict = {
# #     'Начало':'Леонардо ди каприо',
# #     'пираты карибского моря':'джони депп',
# #     'Миссия не выполнима':'Том круз'
# # }
# # favorite_actor = 'Леонардо ди каприо'
# # film = input('Какой фильм вы собираетесь посмотреть ')
# # if film in films_dict:
# #     print('Етот фильм стоит посмотреть')
# # else:
# #     print('Такого фильма нет')


# # questions = [
# #     {'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
# #     'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
# #     'right_answer': 4},

# #     {'question': 'Как звучит полное имя младшего брата Тора?',
# #     'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
# #     'right_answer': 3},

# #     {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
# #     'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
# #     'right_answer': 1}
# # ]

# # points= 0

# # for question in questions:
# #     print(question.get('question'))
# #     answer_number = 1
# #     for answer in question.get('answers'):
# #         print(answer_number, ' - ', answer)
# #         answer_number += 1
    
# #     user_answer = int(input('Ваш ответ: '))
    
# #     if user_answer == question.get('right_answer'):
# #         print('Верно')
# #         points += 1
# #     else:
# #         print('Не верно')
    
# #     print('-'*40)
# # if points == 3:
# #     print('Ты победил!')   
# # else:
# #     print('Ты проиграл!') 
  




# # --------------------------------------------------------------------------------------------------------------------------------------------
# # 19.11.22

# # songs = {
# #     'World in My Eyes': 4.86,
# #     'Sweetest Perfection': 4.43,
# #     'Personal Jesus': 3.45,
# #     'Halo': 4.9,
# #     'Waiting for the night': 6.07,
# #     'Enjoy the silence':4.20,
# #     'Policy of thuth': 4.76,
# #     'Blue Dress': 4.76,
# #     'Clean': 5.83
# # }
# # summ = 0
# # user_request = int(input('Сколько песен выбрать?  '))
# # for i in range(user_request):
# #     song = input('Название  ' + str(i+1)+'  песни: ')
# #     time = songs[song]
# #     summ = summ +time
# # print('Общее время звучания песен: ', summ,'минут')



# # goods = {
# #     'Лампа':'21321',
# #     'стол':'2342',
# #     'диван': '24242',
# #     'стул': '999'
# # }

# # store = {
# #     '21321': [
# #         {'quantity': 27, 'price': 42},
# #     ],
# #     '2342': [
# #         {'quantity': 22, 'price': 510},
# #         {'quantity': 32, 'price': 520},
# #     ],
# #     '24242': [
# #         {'quantity': 2, 'price': 1200},
# #         {'quantity': 1, 'price': 1150},
# #     ],
# #     '999': [
# #         {'quantity': 50, 'price': 100},
# #         {'quantity': 12, 'price': 95},
# #         {'quantity': 43, 'price': 97},
# #     ],
# # }


# # for name, product_key in goods.items():
# #     item_all_quantity = 0
# #     item_all_cost = 0 
# #     for product in store[product_key]:
# #         item_quantity = product['quantity']
# #         item_cost = product['price']
# #         item_all_cost += item_quantity * item_cost
# #         item_all_quantity += item_quantity
# #     print(name , item_quantity , 'шт', 'общая стоимость' , item_all_cost ,  'рублей'.format(name, item_all_quantity , item_all_cost)) 


# # 21.11.22
# # Начнем с открытия,файл открыть можно в нескольких режимах:
# # r - чтение read
# # w - запись write
# # а - append добавление
# # r+ - чтение и запись
# # file = open('название файла или путь до этого файла', 'режим')

# # file = open('result.txt', 'w')
# # file = open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'a')
# # file.write('топ 10 пранков от VS code')
# # file.close()

# # with open как цикл нужен для закрытия файла без file.close, отступ 4 строчки
# # with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'a') as file:
# #     file.write(' Амогус!')

# # /n добавляет перенос на следующую строчку!!!!!

# # with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'r') as file:
# #      text = file.read()
# #      print(text)


# # with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'r') as file:
# #      for line in file.readlines():
# #         print(line)


# # with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'а') as file:
# #     file.write(f'Игрок {name} набрал(а) очков: {count_points}\n')

# # with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'r') as file:
# #      text = file.read()
# #      print(text)

# # def add(x, y):
# #     print(x + y)
# #     return x + y

# # summ = add(7, 7)
# # print(summ)
# # print(add(5, 7))


# # def calcuclator(num1, num2, znak):
# #     num = 0
# #     if znak == '+':
# #         num = num1 + num2

# #     elif znak == '-':
# #        num =  num1 - num2
# #     else:
# #         num =  ' не смогли почситать'
# #         print('Такого знака нету в калькуляторе!!')
# #     with open('C:\\Users\\Роман\OneDrive\\Рабочий стол\\lesspython.txt', 'a') as file:
# #      file.write(num)



# # num = calcuclator(5, 7, '-')
# # print(num)

# # def summa_n(n):
# #     summa = 0
# #     for num in range(n):
# #         summa += num + 1 
# #         print(f' Я знаю, что сумма чисел от 1 до {n} равна {summa}')

# # end = int(input('введите число: '))
# # summa_n(end)



# # def greeting():
# #     for i in range(5):
# #         a = input('Зайдёте? Да/Нет: ')
# #         if a == 'Да':
# #             print('Привет!')
# #             print('Добро пожаловать!')
# #             print('Следующий.\n')
# #         else:
# #             print('Следующий.\n')
 
 
# # greeting()

# # def calcuclator(num1, num2, znak):
# #     global num 
# #     num = 0
# #     if znak == '+':
# #         num = num1 + num2
# #         print(num)
       

# #     elif znak == '-':
# #        num =  num1 - num2
# #        print(num)
    
# #     elif znak == '*':
# #         num = num1 * num2
# #         print(num)
        
# #     elif znak == '/':
# #         num = num1 / num2
# #         print(num)
       
# #     else:
# #         num =  ' не смогли почситать'
# #         print('Такого знака нету в калькуляторе!!')



# # num1 = int(input('Введите число '))
# # num2 = int(input('Введите число '))
# # znak = input('Введите действие ')
# # calcuclator(num1, num2, znak )

# # file = open('C:\\Users\\Роман\\OneDrive\\Рабочий стол\\lesspython.txt', 'a')
# # file.write(f' Результат работы калькулятора: {num}')

# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #    25.11.22 
 

# # from tkinter import *
# # window = Tk()


# # window.geometry('700x500')
# # window.title('very hard test')
# # label_title = Label(text='Тест по вселенной Marvel!!!', font=('arial', 30),  fg='green', bg='black')
# # label_title.place(x=0, y=0, width=700, height=50)
# # facts = [
# #     {'text': ' Человеческое имя Халка - Брюс Беннет', 'right': 1},
# #     {'text': 'Уолт дисней является создателем вселенной marvel', 'right': 0},
# #     {'text': 'До появления костюма супергероя, человек муравей занимался воровством', 'right': 1},
# #     {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
# # ]
# # cur_f = 0 
# # points = 0

# # fact = Message(text=facts[cur_f]['text'], font=('Arial', 14), width= 650)
# # fact.configure(justify=CENTER)
# # fact.place(x=15, y=75)

# # var =  IntVar()
# # true = Radiobutton(text=' Правда ', variable = var, value=1)
# # true.place(x=15, y= 200)

# # def check():
# #     global cur_f, points
# #     answer = var.get()
# #     if answer == facts[cur_f]['right']:
# #         points +=1
# #     if cur_f < len(facts) -1:
# #         cur_f += 1 
# #         fact['text'] = facts[cur_f]['text']
# #     else: 
# #         points_label = Label(text=f'Вы набрали {points} очков .', font=('arial', 35),  fg='blue', bg='black')
# #         points_label.place(x=0, y=0, width=700, height=500)


# # false = Radiobutton(text=' Неправда ', variable = var, value=0)
# # false.place(x=15, y= 120)
# # b = Button(text='Ответить', font=('Arial',24), fg= 'red', command=check)
# # b.place(x=200, y=130)





# # window.mainloop()





# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #    26.11.22 


# # from tkinter import *
# # import random
# # import time 

# # window = Tk()
# # window.geometry('700x500')
# # window.title('Кликер')

# # points = 0
# # points2 = 0
# # def check():
# #     global points
# #     global b
# #     global points2
# #     global c
    
# #     b.place(x=random.randint(1,550),y=random.randint(1,350))
# #     c.place(x=random.randint(1,550),y=random.randint(1,350))
# #     points +=1
# #     points2 +=1
# #     point_label['text'] = points
# #     points2_label['text']= points2
# #     if points >=10 and points2 ==0: 
# #         c['text']='Ну пожалуйста :('
# #     else:
# #         pass


# # def check2():
# #     global points
# #     global b
# #     global points2
# #     global c
# #     c.place(x=random.randint(1,550),y=random.randint(1,350))
# #     points2 +=1
# #     points2_label['text']= points2
# #     if points ==0 and points2 >=10:
# #         b['text']='Ну пожайлуста :('
# #     else:
# #         pass
        


    
       



# # b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# # b.place(x=200,y=130)

# # c = Button(text='НАЖМИ НА МЕНЯ ', font=('Arial', 20), fg='black', command=check2)
# # c.place(x=150,y=150)

# # points2_label = Label(text= points2  , font=('Arial',15), fg='red')
# # points2_label.place(x=25,y=10)
# # point_label = Label(text = points, font=('Arial',15), fg='black')
# # point_label.place(x=10,y=10)

# # window.mainloop()



# # ------------------------------------------------------------------------------------------------------------
# # 27.11.22
# # from tkinter import*
# # # import os

# # window = Tk()
# # window.geometry('900x500')
# # window.title('СМЭРТЬ')
# # def on_close():
# #     if int(count_text['text']) > 0:
# #         count_text['text'] = int(count_text['text']) - 1
# #         count_text.place(x=250, y=25, width=400, height=100)
# #         window.after(1000, on_close)
# #         # shutdown_command="shutdown /s /t 00"
# #         # os.system(shutdown_command)
# #     else:
# #         screen_width = window.winfo_screenwidth()
# #         screen_height = window.winfo_screenheight()
# #         window.geometry(str(screen_width) + 'x' + str(screen_height))

# #         photo = PhotoImage(file='skelet.png')
# #         photo_lable = Label(image=photo, bg='black')
# #         photo_lable.image = photo
# #         photo_lable.place(width=screen_width, height=screen_height, x=0, y=0)
# #         pass
# # window.config(bg='red')
# # window.resizable(width=False, height= False)

# # text = Label(text='СМЭРТЬ', fg= 'black', bg='red',font=('Courier New', 50))
# # text.place(x=300, y=150, width=450, height=100)
# # window.protocol('WM_DELETE_WINDOW', on_close)

# # count_text = Label(text='6', fg= 'black', bg='red',font=('Courier New', 50))
# # text.place(x=300, y=150, width=450, height=100)

# # window.mainloop()
# # # -------------------------------------------------------------------------------------------------------------------------------------------------------
# # 28.11.22


# # from tkinter import*
# # import os

# # window = Tk()
# # window.geometry('1500x900')
# # window.title('не ЛОХОТРОН')
# # def value():
# #     if b.
# #       pass
        
# # window.config(bg='blue')
# # window.resizable(width=False, height= False)

# # text = Label(text='ВЫ ВЫИГРАЛИ В ЛОТЕРЕЕ!', fg= 'red', bg='blue',font=('Courier New', 24))
# # text.place(x=300, y=150, width=450, height=100)
# # window.protocol('WM_DELETE_WINDOW')

# # b= Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', font=('Arial', 20), fg='red', command=value)
# # b.place(x=200,y=130)


# # window.mainloop()



# # ///////////
# # ///WEB////
# # /////////




# # import requests
# # from bs4 import BeautifulSoup
# # import random
# # def get_interesting_fact():
# #     response = requests.get('https://i-fakt.ru')
# #     site_content = response.content
# #     html_code = BeautifulSoup(site_content, 'lxml')
# #     # html_code.find_all(class_ = 'p-2 clearfix')

# #     fact = random.choice(html_code.find_all(class_ = 'p-2 clearfix'))
# #     print(fact.text)
# #     # запринтить текст
# #     print(fact.a)
# #     print(fact.a.attrs['href'])
# #     # запринтить ссылку


# # import requests
# # from bs4 import BeautifulSoup
# # import random
# # def fest():
# #     response = requests.get('https://kudago.com/msk/festival/')
# #     site_content = response.content
# #     html_code = BeautifulSoup(site_content, 'lxml')
# #     fest = random.choice(html_code.find_all(class_ = 'post-title'))
# #     print(fest.text)   
    
# #     print(fest.a.attrs['href'])
# # fest()


# # points= []
# # n = int(input('Количество собак: '))

# # for doge in range(n):

# #     point = int(input(f'Количество очков за сезон для {doge + 1} собаки: '))
# #     points.append(point)

# # print(f'Список с багом  - {points}')
# # max = points[0]
# # min = points[0]
# # for point in points:
# #     if point < min:
# #         min = point
# # for point in points:
# #     if point > max:
# #         max = point
# # for dog in range(n):
# #     if points[dog] == min:
# #         points[dog] = max
# #     elif points[dog] == max:
# #         points = min

# # print(f'список без бага {points}')




# # # -------------------------------------------------------------------------------------------------------------------------------------------------------
# # 01.12.22


# # import requests
# # from lxml import html

# # response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets').text
# # h3 = html.fromstring(response).xpath('//h3')
# # for element in h3:
# #     print(element.text)






# # import requests
# # from bs4 import BeautifulSoup
# # import random
# # import lxml
# # def fest():

# #     response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
# #     site_content = response.content
# #     html_code = BeautifulSoup(site_content, 'lxml')
# #     fest = random.choice(html_code.find_all(class_ = 'col-sm-4 col-lg-4 col-md-4'))
# #     print(fest.text)   
# # fest()



# # import requests
# # from bs4 import BeautifulSoup

# # sp = []
# # sp1 = []

# # link = 'https://store.steampowered.com/tag/browse/#global_492'
# # responce = requests.get(link)
# # site_content = responce.content

# # html_code = BeautifulSoup(site_content, 'lxml')

# # fact = html_code.find_all(class_ ='tag_browse_tag')
# # for i in range(len(fact)):
# #     sp.append(str(fact[i]))
# # a = 0
# # for i in range(len(sp)):
# #     for j in range(len(sp[i])):
# #         if sp[i][j] == '<':
# #             a = j
# #     b = sp[i].index('>')
# #     c = sp[i][b + 1:a]
# #     sp1.append(c)
# # print(sp1)
# # user_genre = input('Скопируйте и вставьте ваш любимый жанр из предложенных выше(на английском с большой буквы): ')
# # if user_genre == 'Indie':
# #         print('Вам следует поиграть в TABS')
# # elif user_genre == 'Combat':
# #         print('вам следует поиграть в cs:go')
# # elif user_genre == 'Horror':
# #         print('Вам следует поиграть в Phasmophobia')
# # elif user_genre == 'Sandbox':
# #         print('Вам следует поиграть в Factorio')
# # elif user_genre == 'Online Co-Op':
# #         print('Вам следует поиграть в Rainbow Six Siedge')
# # elif user_genre == 'Survival':
# #         print('Вам следует поиграть в Rust')
# # else:
# #         print('Вы ввели неверное имя жанра, пожайлуста следуйте инструкции выше!!')
# # pass

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 03.12.22
# # ЦИКЛ WHILE с условием
# # выводим числа которые меньше или равны num
# # num = 10
# # while num > 0:
# #     print(num)
# #     num -=1 #тоже самое что и num = num -1 


# # from random import*

# # num =int(input('Введите число: '))
# # cur_num = 1
# # while cur_num <= num:
# #     print(cur_num)
# #     cur_num += 1




# # import random 

# # films  = ['Форсаж', 'Терминатор', 'Аватар', 'Оно 2', 'Железный человек', 'Джон Уик', 'Мандалорец',  'Звездные войны ', 'Мстители', 'Матрица ', 'Очень странные дела']
# # print('Привет сейчас покажу тебе случайный фильм!')
# # # Создаем бесконечный цикл
# # while True :
# #     print(random.choice(films))
# #     answer = input('Нужно еще ? Y/N: ')
# #     while answer != 'Y' and answer != 'N':
# #         answer = input('Пожайлуста, введите ответ в формате Y/N: ')
# #     if answer =='N':
# #         break



# # print('Приятного просмотра!')


# # from fpdf import FPDF
# # pdf_file = FPDF('P', 'cm',(10,15)) #'P' Портретная ориентиация и размеры страницы
# # pdf_file.add_page()

# # # шрифт текста в файле
# # pdf_file.set_font('arial', size=16)
# # # задаем цвет текста
# # pdf_file.set_text_color(120,78,235)
# # # задаем цвет заднего фона
# # pdf_file.set_fill_color(0,0,255)
# # # задаем цвет рисования 
# # pdf_file.set_draw_color(0,120,0)
# # # создаем ячейку с текстом
# # pdf_file.cell(10,5,'Amogus',align='c',border=10,fill=True)
# # pdf_file.image('pic.jpg',h=0, w=10,x=0, y=5)

# # # создаем заданный пдф файл в текущей папке
# # pdf_file.output('My_pdf.pdf') #в самом конце сохраняет файл


# # number = int(input('Введите число: '))
# # summ = 0
# # while number != 0:

# #  summ += number

# #  number = int(input('Введите  еще одно число: '))

# # print(summ)


# # //////////////////  |
# # /////HomeWORK////  | |
# # ////////////////   /\



# # password = int(input('Введите пароль: '))
# # while password != 235:
# #     print('Пароль не верен! ')
# #     password = int(input('Введите пароль еще раз: '))
# # print('Пароль верный! Добро пожаловать.')






# # https://habr.com/ru/post/232291/



# # import xlrd, xlwt
# # #открываем файл
# # rb = xlrd.open_workbook('D:\\python',formatting_info=True)
# # #выбираем активный лист
# # sheet = rb.sheet_by_index(0)
# # #получаем значение первой ячейки A1
# # val = sheet.row_values(0)[0]
# # #получаем список значений из всех записей
# # vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
# # wb = xlwt.Workbook()
# # ws = wb.add_sheet('Test')
# # #в A1 записываем значение из ячейки A1 прошлого файла
# # ws.write(0, 0, val[0])
# # #в столбец B запишем нашу последовательность из столбца A исходного файла
# # i = 0
# # for rec in vals:
# #     ws.write(i,1,rec[0])
# #     i =+ i
# # #сохраняем рабочую книгу
# # wb.save('D:\\python')





# # import openpyxl
# # wb = openpyxl.load_workbook(filename = '../ArticleScripts/ExcelPython/openpyxl.xlsx')
# # sheet = wb['test']
# # #считываем значение определенной ячейки
# # val = sheet['A1'].value
# # #считываем заданный диапазон
# # vals = [v[0].value for v in sheet.range('A1:A2')]
# # #записываем значение в определенную ячейку
# # sheet['B1'] = val
# # #записываем последовательность
# # i = 0
# # for rec in vals:
# #     sheet.cell(row=i, column=2).value = rec
# #     i =+ 1
# # # сохраняем данные
# # wb.save('../ArticleScripts/ExcelPython/openpyxl.xlsx')



# # Работа с com-объектом

# # import win32com.client
# # Excel = win32com.client.Dispatch("Excel.Application")
# # wb = Excel.Workbooks.Open(u'D:\\Scripts\\DataScience\\ArticleScripts\\ExcelPython\\xl.xls')
# # sheet = wb.ActiveSheet
# # #получаем значение первой ячейки
# # val = sheet.Cells(1,1).value
# # #получаем значения цепочки A1:A2
# # vals = [r[0].value for r in sheet.Range("A1:A2")]
# # #записываем значение в определенную ячейку
# # sheet.Cells(1,2).value = val
# # #записываем последовательность
# # i = 1
# # for rec in vals:
# #     sheet.Cells(i,3).value = rec
# #     i = i + 1
# # #сохраняем рабочую книгу
# # wb.Save()
# # #закрываем ее
# # wb.Close()
# # #закрываем COM объект
# # Excel.Quit()




# # Вызываем функции Python из MS Excel
# # def get_unique(lists):
# #     sm = 0
# #     for i in lists:
# #         sm = sm + int(i.pop()) 
# #     return sm
# # Function sr(lists As Range)
# #     On Error GoTo do_error
# #         Set plugin = PyModule("plugin", AddPath:=ThisWorkbook.Path)
# #         Set result = PyCall(plugin, "get_unique", PyTuple(lists.Value2))
# #         sr = WorksheetFunction.Transpose(PyVar(result))
# #         Exit Function
# # do_error:
# #         sr = Err.Description
# # End Function



# # import xlrd, xlwt
# # rb = xlrd.open_workbook('D:\\python',formatting_info=True)
# # sheet = rb.sheet_by_index(0)
# # val = sheet.row_values(0)[0]
# # vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
# # wb = xlwt.Workbook()
# # ws = wb.add_sheet('Test')
# # ws.write(0, 0, val[0])
# # i = 0
# # for rec in vals:
# #     ws.write(i,1,rec[0])
# #     i =+ i
# # wb.save('D:\\python')


# # import openpyxl
# # wb = openpyxl.load_workbook(filename = 'D:\\python')
# # sheet = wb['test']
# # val = sheet['A1'].value
# # vals = [v[0].value for v in sheet.range('A1:A2')]
# # sheet['B1'] = val
# # i = 0
# # for rec in vals:
# #     sheet.cell(row=i, column=2).value = rec
# #     i =+ 1
# # wb.save('D:\\python')


# # import win32com.client
# # Excel = win32com.client.Dispatch("Excel.Application")
# # wb = Excel.Workbooks.Open(u'D:\\Scripts\\DataScience\\ArticleScripts\\ExcelPython\\xl.xls')
# # sheet = wb.ActiveSheet
# # val = sheet.Cells(1,1).value
# # vals = [r[0].value for r in sheet.Range("A1:A2")]
# # sheet.Cells(1,2).value = val
# # i = 1
# # for rec in vals:
# #     sheet.Cells(i,3).value = rec
# #     i = i + 1
# # wb.Save()
# # wb.Close()
# # Excel.Quit()


# # def get_unique(lists):
# #     sm = 0
# #     for i in lists:
# #         sm = sm + int(i.pop()) 
# #     return sm

    
# # Function sr(lists As Range)
# #     On Error GoTo do_error
# #         Set plugin = PyModule("plugin", AddPath:=ThisWorkbook.Path)
# #         Set result = PyCall(plugin, "get_unique", PyTuple(lists.Value2))
# #         sr = WorksheetFunction.Transpose(PyVar(result))
# #         Exit Function
# # do_error:
# #         sr = Err.Description
# # End Function

# # ------------------------------------------------------------------------------------------------------------------------------------------------------
# # 04.12.22

# # from fpdf import FPDF
# # from datetime import datetime
# # pdf = FPDF('P', 'mm', 'A4')
# # pdf.add_page()
# # pdf.image('HB.jpg', h=297, w=210, x=0, y=0)
# # pdf.add_font('comic','','C:\WINDOWS\FONTS\COMIC.ttf',uni=True) #uni это кодировка которая может читать русский язык
# # pdf.set_font('comic', size=37)
# # pdf.set_text_color(50, 205, 50)
# # friend_name = input('Кому отправим? - ')
# # pdf.cell(0, 95, ln= 1)
# # pdf.cell(0,20, txt=f'Дорогой {friend_name}!', align='C', ln=1)
# # message = input('Введите текст поздравления: ')
# # pdf.set_font('comic',size=24)
# # pdf.set_text_color(10, 100, 25)
# # pdf.set_left_margin(50)
# # pdf.set_right_margin(50)
# # pdf.multi_cell(0, 20,txt=message, align='C')
# # author_name = input('Введите ваше имя: ')
# # today = datetime.today().strftime('%d.%m.%Y')
# # pdf.set_font('comic', size=18)
# # pdf.set_text_color(60,89,147)
# # pdf.cell(0,10,txt= author_name, align='R',ln=1)
# # pdf.cell(0,10,txt=today, align='R',ln=1)
# # pdf.output('card.pdf')



# # :::::::::::
# # :ПРОЕКТ!!!:
# # :::::::::::

# # from tkinter import *
# # def find_fact():
# #     clear()
# #     draw_home_button()

# # def surprise():
# #     clear()
# #     draw_home_button()
# # window = Tk()
# # window.geometry('700x600')
# # def draw_menu():
# #     clear()
# #     label_title  = Label(text='Что бы вы хотели сделать? ', font=('Arial',30), fg='white', bg='Blue' )
# #     label_title.place(width=700, height=50,x=0,y=0)

# #     b1= Button(text='Узнать что-то новое', font=('Arial',25), fg='yellow', bg='Blue',command=find_fact)
# #     b1.place(x=25,y=75, width=300)

# #     b2= Button(text='Сюрприз?', font=('Arial',25), fg='yellow', bg='Blue',command=surprise)
# #     b2.place(x=375,y=75, width=300)

# # def clear():
# #     all_widjets = window.place_slaves()
# #     for wid in all_widjets:
# #         wid.destroy()
# # def draw_home_button():
# #     b_home = Button(text='Назад', font=('Arial',25), fg='yellow', bg='Blue',command=draw_menu)
# #     b_home.place(x=25,y=500,width = 150)





# # draw_menu()
# # window.mainloop()

# # i = 1

# # while i <= 10:

# #     print(i)

# #     i += 1

# # else:

# #     print('Цикл окончен, i =', i)





























# # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 05.12.22
# # Telegram bot
# # import random 
# # from bs4 import BeautifulSoup
# # import requests
# # import telebot
# # token = '5568397319:AAHFQs-MEme68V4m-bC7NRAfGOUppYgq8OY'

# # bot = telebot.TeleBot(token)
# # @bot.message_handler(commands=['start', 'help'])
# # def send_message(message):
# #     welcome_txt = 'Привет я рассказываю стихи, знаю много интересных фактов и могу показать котиков)'
# #     bot.send_message(message.chat.id, welcome_txt)

# # @bot.message_handler(commands=['poem'])
# # def send_poem(message):
# #     poem_txt = 'Амогус?'
# #     bot.send_message(message.chat.id, poem_txt)
# # @bot.message_handler(commands=['fact'])
# # def send_fact(message): 
# #     response = requests.get('https://i-fakt.ru') 
# #     html = BeautifulSoup(response.text) 
# #     fact = random.choice(html.find_all(class_='p-2 clearfix'))  
# #     bot.send_message(message.chat.id, fact.text) 
# #     link_fact = fact.a.attrs['href'] 
# #     bot.send_message(message.chat.id, link_fact) 
# # @bot.message_handler(commands=['cat'])
# # def send_cat(message):
# #         cat_number = str(random.randint(1,3))
# #         cat_img = open('D:\\PYTHON\\' + cat_number +'.jpg', 'rb')
# #         bot.send_photo(message.chat.id, cat_img)
# # @bot.message_handler(commands=['music'])
# # def send_music(message):
# #         song = open('1.mp3', 'rb')
# #         bot.send_audio(message.chat.id, song)
    
# # bot.polling()













# # --------------------------------------------------------------------------------------------------------------------------------------------------------
# # 12.12.22


# ## INT и FLOAT
# # first_var = 22 # тип данных int
# # second_var = 3.5 # тип данных float

# # print(first_var + second_var)
# # print(first_var - second_var)
# # print(first_var / second_var)
# # print(first_var * second_var)

# # print(type(first_var), type(second_var))

# # res_var = first_var + second_var

# # print(type(res_var))

# ## СТРОКИ 
# # str_var = 'Привет, мир' # тип даннных str
# # print(str_var)

# # sub_string_hello = str_var[:6]
# # sub_string_world = str_var[8:]
# # print(sub_string_hello)
# # print(sub_string_world)


# # # IF ELIF ELSE (try, except)

# # # try:
# # #     # Код который мы хотим выполнить и который может вызвать ошибку
# # # except тип ошибки:
# # #     # Действия программы если ошибка возникла
# # # else:
# # #     # Действия программы если ошибки не возникло

# # try:
# #     input_num_1 = int(input('Введите первое число: '))
# #     input_num_2 = int(input('Введите второе число: '))
# # except ValueError:
# #     print('Вы ввели неправильное значение!!!')
# # else:
# #     if input_num_1 > input_num_2:
# #         print(f'{input_num_1} больше чем {input_num_2}.')
# #         # print(str(input_num_1) + ' больше чем ' + str(input_num_2))
# #         # print(input_num_1,'больше чем', input_num_2)


# #     elif input_num_1 < input_num_2:
# #         print(f'{input_num_1} меньше чем {input_num_2}.')
# #     else:
# #         print(f'{input_num_1} равно {input_num_2}.')


# # # СПИСКИ

# # home_list = ['кухня', 'комната', 'зал']
# # home_list.append('спальная')
# # print(home_list)
# # home_list[1] = 'детская'
# # print(home_list)

# # print(len(home_list))

# # for h in home_list:
# #     print(h)


# ## ЦИКЛЫ

# # for i in range(6):
# #     print(i)

# # for i in range(5, 10):
# #     print(i)

# # for i in range(10, 0, -1):
# #     print(i)


# ## ФУНКЦИЯ

# # def add1(x, y):
# #     return x + y

# # def add2(x, y):
# #     print(x + y)

# # summ = add1(5, 5)
# # print(summ)

# # def hello():
# #     name = input('Как тебя зовут: ')
# #     print(f'Приятно познакомиться {name}')
# #     hello()

# # hello()

# # def calculate():
# #     try:
# #         num1 = int(input("Введите первое число: "))
# #         num2 = int(input("Введите второе число: "))
# #     except ValueError:
# #         print('Вы ввели неправильное значение')
# #     else:
# #         print('Укажите интересующую вас операцию: ')
# #         print('* - умножение')
# #         print('/ - деление')
# #         print('+ - сложение')
# #         print('- - вычитаение')

# #         operation = input()

# #         res = None
# #         if operation == '*':
# #             res = int(num1) * int(num2)
# #             print(res)
# #         elif operation == '/':
# #             res = int(num1) / int(num2)
# #             print(res)
# #         elif operation == '+':
# #             res = int(num1) + int(num2)
# #             print(res)
# #         elif operation == '-':
# #             res = int(num1) - int(num2)
# #             print(res)
# #         else:
# #             print('Операция неизвестна, повторите ввод')
# #             print(res)      
# # calculate()

# # def calculate():
# #     import math
# #     choice = int(input('Выберите, что вам нужно решить:   1.Обычные дейсвия с числами; 2.Квадратное уравнение через D; 3.Высчитать корень числа.  '))
# #     global a
# #     global b 
# #     global C
# #     global res0
# #     global x1
# #     global x2
# #     if choice == 1:
# #         try:
# #             num1 = int(input("Введите первое число: "))
# #             num2 = int(input("Введите второе число: "))
# #         except ValueError:
# #             print('Вы ввели неправильное значение')
# #         else:
# #             print('Укажите интересующую вас операцию: ')
# #             print('* - умножение')
# #             print('/ - деление')
# #             print('+ - сложение')
# #             print('- - вычитаение')

# #             operation = input()

# #             res = None
# #             if operation == '*':
# #                 res = int(num1) * int(num2)
# #                 print(res)
# #             elif operation == '/':
# #                 res = int(num1) / int(num2)
# #                 print(res)
# #             elif operation == '+':
# #                 res = int(num1) + int(num2)
# #                 print(res)
# #             elif operation == '-':
# #                 res = int(num1) - int(num2)
# #                 print(res)
# #             else:
# #                 print('Операция неизвестна, повторите ввод')
# #                 print(res)
# #     elif choice == 2:
# #         try:
# #             a = float(input('Введите значение а: '))
# #             b = float(input('Введите значение b: '))
# #             C = float(input('Введите значение с: '))
# #         except ValueError:
# #             print('Неверное значение  попробуйте еще раз!')
# #         else:
# #             res0 = b*b - 4 * a  * C
# #             print("Дискриминант D = %.2f" % res0)
           
# #             if res0 > 0:
# #                 x1 = (-b + math.sqrt(res0)) / (2 * a)
# #                 x2 = (-b - math.sqrt(res0)) / (2 * a)
# #                 print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# #             elif res0 == 0:
# #                 x = -b / (2 * a)
# #                 print("x = %.2f" % x)
# #             else:
# #                 print('Корней нет!') 
# #     elif choice ==3:
# #         global num
# #         global sqrt
# #         num = int(input('Введите число под корнем:  '))
# #         if num > 0:
# #             sqrt = math.sqrt(num)
# #             print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))
# #         elif num == 0:
# #             print('Квадратный корень из 0 = 0')
# #         else:
# #             print('Отрицательное число не может быть под корнем!')
# # calculate()
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 19.12.22
# # telebot
# import random 
# from bs4 import BeautifulSoup
# import requests
# import telebot
# from collections import defaultdict
# token = '5568397319:AAHFQs-MEme68V4m-bC7NRAfGOUppYgq8OY'
# text2 =  'Во что поиграть на пк?'
# bot = telebot.TeleBot(token)
# # user_by_messages = defaultdict(list)
# # messages = []

# @bot.message_handler(commands=['start','help'])
# def send_welcome(message):
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,one_time_keyboard=False)
#     button_poem = telebot.types.KeyboardButton('Стихотворение')
#     button_fact = telebot.types.KeyboardButton('Факт')
#     button_cat = telebot.types.KeyboardButton('Кот')
#     button_music = telebot.types.KeyboardButton('music')
#     button_game = telebot.types.KeyboardButton(text2)
#     keyboard.add(button_poem, button_fact, button_cat, button_music, button_game)
#     welcome_text = 'Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых шлеп'
#     bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


# @bot.message_handler(commands=['poem'])
# def send_poem(message):
#     poem_txt = 'Амогус?'
#     bot.send_message(message.chat.id, poem_txt)
#     keybord = telebot.types.InlineKeyboardMarkup(row_width=1)
#     button_url = telebot.types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
#     keybord.add(button_url)
#     bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keybord)



# @bot.message_handler(commands=['fact'])
# def send_fact(message): 
#     response = requests.get('https://i-fakt.ru') 
#     html = BeautifulSoup(response.text) 
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))  
#     bot.send_message(message.chat.id, fact.text) 
#     link_fact = fact.a.attrs['href'] 
#     bot.send_message(message.chat.id, link_fact) 
# @bot.message_handler(commands=['cat'])
# def send_cat(message):
#         cat_number = str(random.randint(1,3))
#         cat_img = open('F:\\PYTHON\\' + cat_number +'.jpg', 'rb')
#         bot.send_photo(message.chat.id, cat_img)
# # /music
# @bot.message_handler(commands=['music'])
# def send_music(message):
#         song = open('amogus.mp3', 'rb')
#         bot.send_audio(message.chat.id ,song)

# # /sticker
# @bot.message_handler(commands=['sticker'])
# def send_sticker(message):
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGyAFjlcn6NwXCN0gfFcJfQ-iv-usiUAAC1CIAAvhtsEgTy0IAAWSuHYgrBA')
# user_by_messages = defaultdict(list)
# messages = []

# @bot.message_handler(commands=[text2])

# def send_game(message): 
#     list_of_genres = 'Выживание, Шутер, Песочница, Симулятор, Разрушения, Хардкор, СБЭУ, Экшен, Инди, Стратегия, Котики, Королевская битва, Приключения'
#     bot.send_message(message.chat.id, 'Напишите ваш любимый жанр(с заглавной буквы) из представленных ниже🠗🠗🠗.')
#     bot.send_message(message.chat.id, list_of_genres)

#     bot.register_next_step_handler(message, bot_answers)
    


# def bot_answers(message):
#     game = { '1' or '2' or '3' : 'Rust' , '3'  or '5' or '4': 'Teardown' ,

#      '6' or '1' or '2' or '7' : 'Escape from Tarkov', '5' : 'War Thunder', 

#     '8' or '9' or '11' : 'Mount & Blade II: Bannerlord',  '2' or '1' : 'Deadside', '8': 'Watch_Dogs 2', '12' : 'Stray',

#     '2'or '13' : 'PUBG' , '5 ' or '3': 'TABS' , '10' or '1' or '8' : ' Sea of thieves'}

#     text = message.text
#     if  text == 'Выживание':
#         try:
#             game_random = []
#             game_random.append(game['1'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {game_random}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')
#     elif text == 'Шутер':
#         try:
#             game_random = []
#             game_random.append(game['2'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random.text)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Песочница':
#         try:
#             game_random = []
#             game_random.append(game['3'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Разрушения':
#         try:
#             game_random = []
#             game_random.append(game['4'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Симулятор':
#         try:
#             game_random = []
#             game_random.append(game['5'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')
#     elif text == 'Хардкор':
#         try:
#             game_random = []
#             game_random.append(game['6'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'СБЭУ':
#         try:
#             game_random = []
#             game_random.append(game['7'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Экшен':
#         try:
#             game_random = []
#             game_random.append(game['8'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')
    
#     elif text == 'Инди':
#         try:
#             game_random = []
#             game_random.append(game['9'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Приключения':
#         try:
#             game_random = []
#             game_random.append(game['10'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')
    
#     elif text == 'Стратегия':
#         try:
#             game_random = []
#             game_random.append(game['11'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Котики':
#         try:
#             game_random = []
#             game_random.append(game['12'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')

#     elif text == 'Королевская битва':
#         try:
#             game_random = []
#             game_random.append(game['13'])
            
#             bot.send_message(message.chat.id, f'Вам следует поиграть в {str(game_random)}.')
            
#         except:
#             bot.send_message(message.chat.id, 'Чтото пошло не так, попробуйте еще раз...')
    
#     else: 
#         bot.send_message(message, 'Вы неправильно ввели название жанра или такого жанра нет в боте!Попробуйте еще раз.')
    
    





# @bot.message_handler(content_types=['text', 'audio',"photo"]) #перед bot.polling
# def answer (message):
#     if message.text.strip() == 'Стихотворение':
#         send_poem(message)
#     elif message.text.strip() == 'Факт':
#         send_fact(message)
#     elif message.text.strip() == 'Кот':
#         send_cat(message)
#     elif message.text.strip() =='music':
#         send_music(message)
#     elif message.text.strip() =='Во что поиграть на пк?':
#         send_game(message)
#     else:
#         bot.send_message(message.chat.id, 'Пока')




# bot.polling()
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 26.12.22
# from tkinter import*
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# # canvas.create_rectangle(120,120,140, 140, fill='yellow', outline='')
# # canvas.create_rectangle(150,150,190, 190, fill='blue', outline='')
# # canvas.create_rectangle(200,200,260, 260, fill='red', outline='')
# # canvas.create_polygon(10,180,60,110 ,100,120 ,fill='yellow', outline='')
# canvas.create_rectangle(20,260,100,320, fill='brown', outline='')
# canvas.create_polygon(10,260,60,200,110,260 ,fill='yellow', outline='')
# canvas.create_rectangle(50,280,70,300, fill='SkyBlue1', outline='black')

# # ---------------------------------------------------------------
# from tkinter import*
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# class House:
#     def __init__(self,  roof_color, wall_color ):
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.width = 130
#         self.height = 100
#         self.roof = None
#         self.wall = None

#     def build_house(self, x, y):
#         h = self.height
#         w = self.width
#         self.roof = canvas.create_polygon(x,y,x + w,y,x +w/2,y - h/2, fill=self.roof_color)
#         self.wall = canvas.create_rectangle(x+20,y,x + w -20, y + h, fill=self.wall_color)
#     def print_info(self):
#         print(f'Цвет дома {self.wall_color}')
#         print(f'Цвет крыши {self.roof_color}')
#         print(f'Шарина дома {self.width}')
#         print(f'Высода дома {self.height}')




# house_1 = House('red', 'green')
# house_2 = House('black', 'blue')
# house_1.print_info()
# house_2.print_info()

# from tkinter import*
# class Paint(Frame):
#     def __init__(self):  
#         Frame.__init__(self) 
#         self.pack(fill = BOTH, expand = True)  
#         c = Canvas(self)
#         c.create_polygon(10,10,100,100,150,50, fill="yellow", width=3, outline='orange')
#         c.create_polygon(250,110,350,150,280,200,fill="orange", width=3, outline='yellow')
#         c.create_polygon(50,0,0,50,150,100,fill="red", width=3, outline='')
#         c.create_rectangle(30,210,90,260,fill="red", width=3, outline='black')
#         c.create_rectangle(250,210,300,260,fill="black", width=3, outline='red')  
#         c.pack(fill = BOTH, expand = True) 
       
# f = Paint()
# f.mainloop()

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 14.01.23
# from tkinter import *
# import random
# window = Tk()
# window.title("Чтобы ударить нажмите W!!!")
# w = 600
# h = 600
# window.geometry(str(w) + 'x' + str(h))
# canvas = Canvas(window, width=w, height=h)
# canvas.pack()
# bg_photo = PhotoImage(file='bg.png')
# class warrior_1:
#     def __init__(self,health = 100):

#         self.x = 70
#         self.y = h / 2
#         self.photo = PhotoImage(file='ninja_1.png')
#         self.h = health
# def hit(event):
#     current_attacker  = random.randint(1,2)
#     if current_attacker == 1:
#         ninja_1.h -= 20
#         print(f'ninja_1.h {ninja_1.h}')
#     elif current_attacker == 2:
#         ninja_2.h -= 20
#         print(f'ninja_2.h {ninja_2.h}')
#     else:
#         print('Робит')  
# ninja_1 = warrior_1()
# ninja_2 = warrior_1()
# def ninja_die():
#     if ninja_2.h  == 0:
#         canvas.delete('all')
#         canvas.create_image(w//2, h//2, image = bg_photo)
#         canvas.create_text(w//2, h//2, text="Первый ninja победил!", font="Verdana 42", fill='blue')
#     elif ninja_2.h == 0:
#         canvas.delete('all')
#         canvas.create_image(w//2, h//2, image = bg_photo)
#         canvas.create_text(w//2, h//2, text="Второй ninja победил!", font="Verdana 42", fill='red')
#     else:
#         window.after(20, game)
# def game():
#     canvas.delete('all')
#     canvas.create_image(w//2, h//2, image = bg_photo)
#     canvas.create_image(ninja_1.x, ninja_1.y, image = ninja_1.photo)
#     canvas.create_image(ninja_2.x + 200, ninja_2.y, image = ninja_2.photo)
#     ninja_die()
# game()
# window.bind('w',hit)
# window.mainloop()





# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 09.01.23

# from tkinter import *
# import random
# window = Tk()

# w = 600
# h = 600

# window.geometry(str(w) + 'x' + str(h))

# canvas = Canvas(window, width=w, height=h)
# canvas.pack()

# bg_photo = PhotoImage(file='bg_2.png')

# # Класс рыцарь
# class Knight:
#     def __init__(self):
#         self.x = 70
#         self.y = h / 2
#         self.v = 0
#         self.v -= self.x
#         self.v += self.x
#         self.photo = PhotoImage(file='knight.png')
#     def up(self, event):
#         self.v = -3
#         y_cord =self.y
#         print(y_cord)
#         if y_cord <= 55:
#             self.v = +15
#         else: 
#             self.v = -3
#     def down(self, event):
#         self.v = 3
#         y_cord =self.y
#         print(y_cord)
#         if y_cord >= 545:
#             self.v = -15
#         else: 
#             self.v = 3
#     def stop(self, event):
#         self.v = 0
#         y_cord =self.y
#         print(y_cord)
#     def left(self,event):
#         self.x -= 4
#         print(self.x)
#     def right(self,event):
#         self.x += 4
#         print(self.x)
# knight_obj = Knight()
# class Dragon:
#     def __init__(self):
#         self.x = w + 150
#         self.y = random.randint(100, h - 100)
#         self.v = random.randint(1,3)
#         self.photo = PhotoImage(file='dragon.png')

# dragons_list = []
# for i in range(3):
#     dragons_list.append(Dragon())

# def game():
#     canvas.delete('all')
#     canvas.create_image(w//2, h//2, image = bg_photo)
#     canvas.create_image(knight_obj.x, knight_obj.y, image = knight_obj.photo)
#     knight_obj.y += knight_obj.v
    

#     current_dragon = 0
#     dragon_to_kill = -1

#     for dragon in dragons_list:
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x, dragon.y, image = dragon.photo)
#         if ((dragon.x-knight_obj.x)**2) + ((dragon.y - knight_obj.y)**2) <= (96)**2:
#             dragon_to_kill = current_dragon
        
#         current_dragon += 1
#         #Поражение
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w//2, h//2, text="You lose!", font="Verdana 42", fill='green')
#             break


#     if dragon_to_kill >= 0:
#         del dragons_list[dragon_to_kill]

#     # Победа
#     if len(dragons_list) == 0:
#         canvas.delete('all')
#         canvas.create_text(w//2, h//2, text="You win!", font="Verdana 42", fill='red')
#     else:
#         window.after(20, game)


# game()

# window.bind('w', knight_obj.up )
# window.bind('s', knight_obj.down)
# window.bind('<KeyRelease>', knight_obj.stop)
# window.bind('a', knight_obj.left)
# window.bind('d', knight_obj.right)
# window.mainloop()

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 16.01.23
# import requests
# url = 'https://swapi.dev/api'
# response = requests.get(url).json()

# # people_api = response.get('people')
# starships_api = response.get('starships')
# def check_people(url):
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()    #https://swapi.dev/api/people +/ + i(1 - 5)
#         print(response['name']+ '-'+ response['height'])
# planets_api = response.get('planets')
# def check_planets(url):
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()    #https://swapi.dev/api/planets +/ + i(1 - 5)
#         print(response['name'])

# def check_planets_diameter(url):
#     diameters_list = []
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()  # https://swapi.dev/api/people + / + i(1 - 5)
#         diameters_list.append({response.get('name'): response.get('diameter')})
        
#     print(diameters_list)


# check_people(people_api)
# check_planets(planets_api)
# check_planets_diameter(planets_api)
# def check_starships_max_speed(url):
#     for i in range(1, 6):
#         max_atmosphering_speed_LIST = []
#         response = requests.get(f'{url}/{i}').json()  # https://swapi.dev/api/people + / + i(1 - 5)
#         max_atmosphering_speed_LIST.append({response.get('name'): response.get('max_atmosphering_speed')})
#         print(max_atmosphering_speed_LIST)
# check_starships_max_speed(starships_api)

# # var_1 = True
# # var_2 = False
# # var_3 = 6 > 4
# # # print(var_3)
# # hour = 13
# # #hour = 18   True(1)  *    False(0)
# # if hour > 12 and hour <= 16:
# #     print('День')
# # elif hour > 16 and  hour <= 23:
# #     print('Вечер')
# # elif hour > 23 or hour <= 3:
# #     print('Ночь')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# import requests
# url = 'https://swapi.dev/api'

# response = requests.get(url).json()

# starships_api = response.get('starships')

# def check_starships_max_speed(url):

#         for i in range(1,6):
#             max_speed_LIST = []
#             response = requests.get(f'{url}/{i}').json()  
#             max_speed_LIST.append(response.get('max_atmosphering_speed'))
#             print(max_speed_LIST)
        
#         # del max_speed_LIST[]
#         # print(max_speed_LIST)

#         # print(max_speed_LIST[0], ' -  Наибольшая скорость из всех кораблей')
        
# check_starships_max_speed(starships_api)



# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 23.01.23

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# today = datetime.today()

# today = today.strftime('%d/%m%Y')

# print(f'Курс на  {today}.')

# payload = {'date_req=':today}

# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

# date = 'date_req=23/01/2023'
# responce = requests.get(url , date)

# xml = BeautifulSoup(responce.content, 'html.parser')
# def getCourse(id):
#     return xml.find('valute', {'id': id}).value.text

# print(f'{getCourse("R01235")} рублей за 1 доллар\n')
# print(f'{getCourse("R01239")} рублей за 1 евро\n')
# print(f'{getCourse("R01375")} рублей за 1 юань\n')
# print(f'{getCourse("R01035")} рублей за 1 Фунт стерлингов\n')
# print(f'{getCourse("R01230")} рублей за 1 Дирхам ОАЭ\n')
# with open('file.txt', 'a') as file:
#     file.write(f'Курс на  {today}:\n')
#     file.write(f'{getCourse("R01235")} рублей за 1 доллар\n\n')
#     file.write(f'{getCourse("R01239")} рублей за 1 евро\n\n')
#     file.write(f'{getCourse("R01375")} рублей за 1 юань\n\n')
#     file.write(f'{getCourse("R01035")} рублей за 1 Фунт стерлингов\n')
#     file.write(f'{getCourse("R01230")} рублей за 1 Дирхам ОАЭ\n')
# . . . . . . . . . . . . . . .  . .  .. . . .  .  . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . .
# Создайте программу, которая будет конвертировать валюту.
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import math
# import locale
# today = datetime.today()
# today = today.strftime('%d/%m%Y')
# payload = {'date_req=':today}
# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# date = 'date_req=23/01/2023'
# responce = requests.get(url , date)
# xml = BeautifulSoup(responce.content, 'html.parser')
# def getCourse (id):
# 	return xml.find("valute",  {'id': id}).value.text
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8' )
# #  . . . . . . .. . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . .
# # Char code конвертируемой  валюты пользователя
# valute_from = str(input('Введите конвертируемую валюту(код RUR, USD, EUR, CNY): '))

# if valute_from == 'RUR':
# 	valute_from = float('1')

# elif valute_from == 'USD':
# 	valute_from = getCourse("R01235")
# 	valute_from = float(valute_from.replace(',', '.'))
# elif valute_from == 'EUR':
# 	valute_from = getCourse("R01239")
# 	valute_from = float(valute_from.replace(',', '.'))
# elif valute_from == 'CNY':
# 	valute_from = getCourse("R01375")
# 	valute_from = float(valute_from.replace(',', '.'))
# else:
# 	print('Вы неверно ввели Char code или введенная валюта нет в  программе.')
# #  . . . . . . .. . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . .
# # Char code  валюты пользователя
# valute_to = str(input('Введите валюту в которую конвертировать(код RUR, USD, EUR и тд):'))

# if valute_to == 'RUR':
# 	valute_to = float('1')

# elif valute_to == 'USD':
# 	valute_to = getCourse("R01235")
# 	valute_to = float(valute_to.replace(',', '.'))
# elif valute_to == 'EUR':
# 	valute_to = getCourse("R01239")
# 	valute_to = float(valute_to.replace(',', '.'))
# elif valute_to == 'CNY':
# 	valute_to = getCourse("R01375")
# 	valute_to = float(valute_to.replace(',', '.'))
# else:
# 	print('Вы неверно ввели Char code или введенная валюта нет в  программе.')
# #  . . . . . . .. . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . .
# # количество валюты:
# amount = int(input('Введите кол-во валюты для конвертации:  '))
# #  . . . . . . .. . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . .
# # функция конвертирования:
# RUR = 1
# def course (valute_from, valute_to, amount):
# 	print(f'{valute_from} -Ваша валюта  {valute_to} -Курс валюты для конвертации {amount} -количество валюты ')
	
# 	if valute_from == 1.0:
# 		user_valute_first = valute_to * amount
# 		user_valute_last = math.floor(user_valute_first)
# 	elif valute_from > RUR and valute_to == 1.0:
# 			user_valute_first = valute_from* amount
# 			user_valute_last = math.floor(user_valute_first)
# 	elif  valute_from > RUR:
# 		valute_from_course = valute_from
# 		valute_to_course = valute_to
# 		user_valute = amount * valute_from_course
# 		user_valute_first = user_valute / valute_to_course
# 		user_valute_last = math.floor(user_valute_first)
# 	else:
# 		print('что-то пошло не так...')
# 	print(user_valute_last)
    
	

# course(valute_from, valute_to, amount)


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 30.01.23
# import os
# from gtts import gTTS
# from playsound import playsound
# with open('file.txt', 'r', encoding='utf-8') as my_file:
#     my_string = my_file.read()
# mp3_name = 'ru.mp3'
# tts = gTTS(text=my_string, lang='ru')
# tts.save(mp3_name)
# playsound(mp3_name)
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import pyaudio
# import speech_recognition as sr
# import random
# while True:
#     r = sr.Recognizer()
#     with sr.Microphone(device_index=1) as source:
#         print('Скажи что нибудь...')
#         print('Скажи что нибудь...')
#         print('Скажи что нибудь...')
#         print('Скажи что нибудь...')
#         print('Скажи что нибудь...')
#         print('Скажи что нибудь...')
#         audio = r.listen(source)

#     speech = r.recognize_google(audio, language='ru_RU').lower()
#     print(speech)
#     answers_list = ['Здарова','Привет','Здраствуйте', 'Приветствую', 'Здраствуй путник']
#     films_list = ['Чебурашка', 'Ярость', '28 панфиловцев','Ведьмак', 'Аватар: Путь воды', 'Аватар', 'Люди в черном', 'Брат', 'Брат-2','9 Рота']
#     if 'привет' in speech:
#         answer = random.choice(answers_list)
#         print(answer)
#     elif 'пока' in speech:
#         print('Пока')
#     else:
#         print('Слова не распознаны')
    
#     if 'фильм' in speech:
#         film = random.choice(films_list)
#         print(film)
#     else:
#         print('Слова не распознаны')
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 06.02.23
# from tkinter import *
# window = Tk()
# count = 0
# def change_label():
#     global count
#     count += 1
#     label_1['text'] = count
# window.title('Far cry 5')
# window.geometry('1500x1500')
# label_1 = Label(window,text='?'*1000, font='16')
# label_1.place(x=100,y=100)
# Label['text'] = '?!' *1000
# btn = Button(text='Баттон', bg='#16c751', fg='black', font='20',command=change_label)
# btn.place(x=200, y=200)








# window.mainloop()


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 07.02.23
# from tkinter import *
# import requests                 # pip install requests
# from bs4 import BeautifulSoup   # pip install bs4
# from datetime import datetime 
# window = Tk()
# window.geometry('400x350+300+300')
# window.title('Курс валют')
# window.resizable(width=False, height= False)
# img = PhotoImage(file='logo.png')
# logo = Label(window, image=img)
# logo.place(x=0, y=0)
# img2 = PhotoImage(file='usd.png')
# usd_pic = Label(window, image=img2)
# usd_pic.place(y=190, x=40)
# img3 = PhotoImage(file='eu.png')
# eu_pic = Label(window, image=img3)
# eu_pic.place(y=250, x=40)
# img4 = PhotoImage(file='chinf.png')
# china_pic = Label(window, image=img4)
# china_pic.place(y=300, x=40)
# tablo = Label(window, text='Курс валют', font=('Arial', 22))
# tablo.place(x=150, y=25)
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
# payload = {"date_req" : today}
# responce = requests.get(url, params=payload)
# xml = BeautifulSoup(responce.content, "html.parser")
# def getCourse(id):
# 	return xml.find("valute",  {'id': id}).value.text
# course_date = Label(window, text=f'Курс валют на {today.replace("/", ".")}', font=('Arial', 18))
# course_date.place(y=150, x=90)
# usd_course = Label(window, text=f'$ {getCourse("R01235")} руб.', font=('Arial', 18))
# usd_course.place(y=190, x=100)
# eur_course = Label(window, text=f'€ {getCourse("R01239")} руб.', font=('Arial', 18))
# eur_course.place(y=250, x=100)
# yuan_course = Label(window, text=f'¥ {getCourse("R01375")} руб.', font=('Arial', 18))
# yuan_course.place(y=300, x=100)
# window.mainloop()

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 13.02.23

# def func(a, b , c = 3, d= 2):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(d)
# func(c=5, d=5)
# # a - позиционный аргумент
# # с - именной аргумент
# # сначала а потом с 

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def func(a,b, *args, **kwargs): #можно передавать через args и kwargs любое количество аргументов
# 	print(a)
# 	print(b)
# 	print(args) #работает как список с [], (args[4]) - индекс чтобы вызвать чтото 
# 	print(kwargs) #передает любое количество ИМЕННОВАННЫХ аргументов, kwargs.get('two') - как словарь


# func(1,2, 3, 4 , 5 , 6, one= 1, two = 2)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Тернарный if


# #  обычный if:
# age = 18

# if age >= 18:
# 	is_allow = True
# else:
# 	is_allow = False

# print(is_allow)
# ---------------------
# # Тернарный if
# is_allow = True if age >= 18 else False
# print(is_allow)

# # ---------------------------

# val = None

# if val is None:
# 	res = []
# else:
# 	res = val

# # Тернарный if
# val = None
# res = [] if val is None else val

# val = None
# res = val or []
# print(res)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Генерация списков и словарей 



# div_5_list = []

# for x in range(100):
# 	if x  % 5 == 0 :   # 5 % 2 = 1   5%10= 5   4%2 = 0
# 		div_5_list.append(x)

# print(div_5_list)


# div_5_list = [x for x in range(100) if x % 5== 0] 


# 			#    |        3   		| 1      			|   2       |
# div_5_list = [x**3 if x > 50 else x for x in range(100) if x % 5==0] 


# print(div_5_list)

# # -----------------------------------------------------------

# a = {x:len(x) for x in ['orange', 'red', 'blue', 'green']}
# print(a)


# самостоятельное задание

# div_5_list = [x for x in range(0, 250) if x % 30== 0 or x % 31 ==0] 
# print(div_5_list)



# # -----------------------------------------------------------

# Кортежи - списки неизменяемая структура данных
#  Один из способов оптимизации ткк хавает меньше памяти
# пишется через () или tuple()

# СПИСОК
# listt1 = []
# listt2 = list()

# # КОРТЕЖ
# tuple1 = ()
# tuple2 = tuple()

# some_dict= {
# 	(1,2,3) : 'Hello'
# }
# a = some_dict.get((1,2,3))
# print(a)

# some_list = [1,2,3]
# some_tuple = list(some_list) #кортеж стал списком

# some_tuple = (1,2,3)
# some_list = tuple(some_tuple) #список стал кортежем





# # -----------------------------------------------------------
# 19.02.23
# 1
# def func_div(*args):
#     return [list(filter(lambda x: x % 2 == i, args)) for i in range(2)]

# print(func_div(1,2,3,4,5,6,7,8,9,10))
# 2
# \\
# \\
# \\
# a = (5, 3, 2, 1, 4)
# b = list(a)
# list.sort(b)
# а = tuple(b)
# print(а)


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 20.02.23
# ООП

# class Human:
#     def __init__(self, name, color_hair,weight,height):
#         self.name = name
#         self.color_hair = color_hair
#         self.height = height
#         self.weight = weight
#     def breathe(name):
#         print(f'{name} дышит')

# human1 = Human('Aнтон', 'black', 190, 80)
# human2 = Human('Василий', 'brown', 180, 90)


# import random
# class Tank:
#     """Template of tanks"""
    
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         self.model = model
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
#         self.health = health

#     def print_info(self):
#         print(f'{self.model} имеет лобовую броню {self.armor}мм. при {self.health} здоровье и урон {self.damage}')

#     def health_down(self, enemy_damage):
#         self.health -= enemy_damage - (self.armor / 10)
#         print(f"\n{self.model}:")
#         if self.health <= 0:
#             self.health = 0
#         print(f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")

#     def shot(self, enemy):
#         enemy.health_down(self.damage)
#         if enemy.health > 0:
#             print(f"\n{self.model}:")
#             print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
#         else:
#             print(f'Экипаж танка {enemy.model} уничтожен')


# class SuperTnk(Tank):
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         super().__init__(model, armor, min_damage, max_damage, health)
#         self.forceArmor = True
    
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage / 2)



# tank_1 = Tank('ИС-3', 90, 20, 30, 100)
# tank_2 = Tank('Tiger', 90, 10, 40, 100)

# tank_1.print_info()
# tank_2.print_info()

# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)


# tank_1 = Tank('ИС-3', 90, 20, 30, 100)
# tank_super = SuperTnk('MAUS', 90, 10, 40, 100)

# tank_1.print_info()
# tank_super.print_info()

# tank_1.shot(tank_super)
# tank_1.shot(tank_super)
# tank_1.shot(tank_super)
# tank_1.shot(tank_super)







# НАСЛЕДОВАНИЕ
# class A:
#     def one(self):
#         print(1)
#     def two(self):
#         print(2)
# class B(A):
#     def three(self):
#         print(3)
# a = A()
# b = B()

# a.one()
# a.two()

# b.one()
# b.two()

# b.three()


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 25.02.23


# class User:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#     def health_down(self, damage, enemy):
#         self.health -= damage
#         print(self.health)
#         if self.health <= 0:
#             self.health = 0
       
#     def atack(name,damage, health):
#         name.health_down(damage)
#         if health > 0:
#             print(f'{name} еще жив.')
#             print(f'У него {health}')
#         else: 
#             health = 0
#             print(f'{name} помер.')

# class User:
#     def __init__(self, name,damage, health):
        
#         self.name = name
#         self.damage = damage
#         self.health = health

#     def health_down(self, enemy_damage):
#         self.health -= enemy_damage
#         if self.health <= 0:
#             self.health = 0
#         print(f"Атаковали {self.name}, у него осталось {self.health} очков здоровья")

#     def attack(self, enemy):
#         enemy.health_down(self.damage)
#         if enemy.health > 0:
#             print(f"{enemy.name} осталось {enemy.health} единиц здоровья")
#         else:
#             print(f'{enemy.name} убит')

# class Warrior(User):
#     def __init__(self, name,damage, health):
#         super().__init__(name, damage, health)
#         self.name = name
#         damage = damage *2
#         health = health + 50
#         self.damage = damage 
#         self.health = health 
        
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage / 2)

# class Mag(User):
#     def __init__(self, name, damage, health):
#         super().__init__(name, damage, health)
#         self.damage = damage
#         self.health = health
#         self.name = name
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage)
# class Archer(User):
#     def __init__(self, name,damage, health):
#         super().__init__(name, damage, health)
#         self.name = name
#         damage = damage * 1.5
#         self.damage = damage  
#         self.health = health 
        
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage)

# User_1 = Warrior('Воин', 20,100)
# User_2 = Mag('Маг',20, 100)
# User_3 = Archer('Лучник',20,100)
# User_2.attack(User_3)
# User_1.attack(User_2)
# User_1.attack(User_2)
# User_2.attack(User_3)
# User_2.attack(User_3)
# User_2.attack(User_3)
# User_2.attack(User_3)




# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 27.02.23

# print(id(1), type(1))
# print(id(id), type(id))
# print(id(id), type(type))


# # ----------------------------------------------------------------------------

# class A:
#     def public(self):
#         return 42
#     def _private(self):
#         return 'test'
#     def __protect(self):
#         return True
#     def wrapper_protect(self):
#         return self.__protect
# a = A()
# print(a.public())
# print(a._private())
# print(a._A__protect())


# # ----------------------------------------------------------------------------
# паттерны проектирования
# Singleton
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton,cls ).__new__(cls)
#         return cls.instance
    

# s = Singleton()
# print(s, id(s))
# s1 = Singleton()
# print(s1, id(s1))
        

# # ----------------------------------------------------------------------------
# декораторы

# def f():
#     return 2+2

# q = f
# print(q())



# def repair_deco(func):  # тут постоянный аргемент это func
#     def wrapper(a,b):   #тут аргументы которые получает функция
#         # return func(a,b) - 1
#         return ' hello vietnam'
#     return(wrapper)

# @repair_deco #оборачиваем функцию в декоратор с помощью @
# def wrong_func(a,b):
#     return a+b+1
# print(f'2 + 2 = {wrong_func(2,2)}')
# print(f'2 + 2 = {wrong_func(5,5)}')



# from datetime import datetime
# def timeit(func):
#     def wrapper(val):
#         start = datetime.now()
#         res = func(val)
#         end = datetime.now()
#         print(f'time:{end - start}')
#         return res
#     return wrapper



# @timeit
# def get_list_1(val):
#     return[x for x in range(val) if x % 2]

# @timeit
# def get_list_2(val):
#     new_list = []
#     for x in range (val):
#             if x % 2:
#                 new_list.append(x)

#     return new_list

# val = 10000

# a = get_list_1(val)
# b= get_list_2(val)


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.03.23
#Проект Kelvin
# import signal
# import time 
# from tkinter import*
# import pyaudio
# import speech_recognition as sr
# import random
# from datetime import datetime
# from tkinter import ttk
# w = 500 
# h = 500
# window = Tk()
# window.geometry('520x250')
# window.title('Kelvin voice helper')
# window['bg'] = 'White'
# label1 = PhotoImage(file='label.png')
# label2 = PhotoImage(file='label2.png')
# window_logo = Label(window, image=label1)
# window_logo.place(x=0, y=0)
# window_logo = Label(window, image=label2)
# window_logo.place(x=10, y=50)
# photo = PhotoImage(file = "mic.png")
# label_3 = Label(window,text='Кельвин вас слушает...',bg='#63f',fg='white')
# def mic_func1():
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=1) as source:
#             print('Скажи что нибудь...')
#             audio = r.listen(source)
#         speech = r.recognize_google(audio, language='ru_RU').lower()
#         # print(speech)
#         answers_list = ['Здарова','Привет','Здраствуйте', 'Приветствую', 'Здраствуй путник']
#         if 'привет' in speech:
#             answer = random.choice(answers_list)
#             print(answer)
#         elif 'пока' in speech:
#             print('Пока')
#         else:
#             print('Слова не распознаны')
# def run_progress():
#  my_progress= Label(window,text='Kelvin вас слушает, говорите..')
#  my_progress.place(x=w//2, y= 200 )
#  my_progress.pack(pady=40)

# def mic_func2():
#     run_progress()
#     mic_func1()
#     time.sleep(15)

# mic_button = Button(window,image=photo ,fg='#63f',compound=RIGHT,command=mic_func2)
# mic_button.place(x=w//2, y=100, width=54, height=54)
# window.mainloop()

# import time
# import tkinter as tk
# import datetime
# import time
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.button = tk.Button(self, command=self.start_action,
#                                 text="подождите 10 секунд")
#         self.button.place(padx=50, pady=20)
#         self.w = 500 
#         self.h = 500
#         self.window = Tk()
#         self.window.geometry('520x250')
#         self.window.title('Kelvin voice helper')
#         self.window['bg'] = 'White'
#         self.label1 = PhotoImage(file='label.png')
#         self.label2 = PhotoImage(file='label2.png')
#         self.window_logo = Label(window, image=label1)
#         self.window_logo.place(x=0, y=0)
#         self.window_logo = Label(window, image=label2)
#         self.window_logo.place(x=10, y=50)
#         self.photo = PhotoImage(file = "mic.png")
#         self.label_3 = Label(window,text='Кельвин вас слушает...',bg='#63f',fg='white')
#     def start_action(self):
#         self.button.config(state=tk.DISABLED)
#         time.sleep(10)
#         self.button.config(state=tk.NORMAL)
#     def mic_func1():
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=1) as source:
#             print('Скажи что нибудь...')
#             audio = r.listen(source)
#         speech = r.recognize_google(audio, language='ru_RU').lower()
#         # print(speech)
#         answers_list = ['Здарова','Привет','Здраствуйте', 'Приветствую', 'Здраствуй путник']
#         if 'привет' in speech:
#             answer = random.choice(answers_list)
#             print(answer)
#         elif 'пока' in speech:
#             print('Пока')
#         else:
#             print('Слова не распознаны')
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



######

# import time
# import tkinter as tk
# import random
# import speech_recognition as sr
# from tkinter import *
# import requests                 
# from bs4 import BeautifulSoup   
# from datetime import datetime 
# class Ball():
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1  # чтобы мяч двигался вверх
#         self.touch_bottom = False
#         self.points = 0
        
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -2.5
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= self.platform.pos[0] and self.pos[0] <= platform_pos[2]:
#             if self.pos[3] >=self.platform.pos[1] and self.pos[3] <= platform_pos[3]:
#                 self.points +=1
#                 return True 
#         return False
# class Platform():
#     def __init__(self,canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2
#     def right(self, event):
#         if self.pos[2] <= 500:
#             self.x = 2
#     def stop(self, event):
#             self.x = 0
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#         if self.pos[2] >= 500:
#             self.x = 0
# def game():
#     window = Tk()
#     window.title("Аркада")
#     window.resizable(0, 0)
#     window.wm_attributes('-topmost', 1)
#     canvas = Canvas(window, width=500, height=400)
#     canvas.pack()
#     platform = Platform(canvas, 'green')
#     ball = Ball(canvas, platform, 'red')
#     points_label = Label(text=ball.points,font="Arial 15", fg='blue', bg='white')
#     points_label.place(x=10, y = 100)
        
#     while True:
#         if ball.touch_bottom:
#             window.destroy()
#             points_label.destroy()
#             break
#         else:
#             platform.draw()
#             ball.draw()
#             points_label.config(text=f"Очки: {ball.points}")
#         window.update()
#         time.sleep(0.01)
#     window.mainloop()
# def kurse(): 
#     window = Toplevel()
#     window.geometry('400x350+300+300')
#     window.title('Курс валют')
#     window.resizable(width=False, height= False)
#     img = PhotoImage(file='logo.png')
#     logo = Label(window, image=img)
#     logo.place(x=0, y=0)
#     img2 = PhotoImage(file='usd.png')
#     usd_pic = Label(window, image=img2)
#     usd_pic.place(y=190, x=40)
#     img3 = PhotoImage(file='eu.png')
#     eu_pic = Label(window, image=img3)
#     eu_pic.place(y=250, x=40)
#     img4 = PhotoImage(file='chinf.png')
#     china_pic = Label(window, image=img4)
#     china_pic.place(y=300, x=40)
#     tablo = Label(window, text='Курс валют', font=('Arial', 22))
#     tablo.place(x=150, y=25)
#     url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#     today = datetime.today()
#     today = today.strftime("%d/%m/%Y")
#     payload = {"date_req" : today}
#     responce = requests.get(url, params=payload)
#     xml = BeautifulSoup(responce.content, "html.parser")
#     def getCourse(id):
#         return xml.find("valute",  {'id': id}).value.text
#     course_date = Label(window, text=f'Курс валют на {today.replace("/", ".")}', font=('Arial', 18))
#     course_date.place(y=150, x=90)
#     usd_course = Label(window, text=f'$ {getCourse("R01235")} руб.', font=('Arial', 18))
#     usd_course.place(y=190, x=100)
#     eur_course = Label(window, text=f'€ {getCourse("R01239")} руб.', font=('Arial', 18))
#     eur_course.place(y=250, x=100)
#     yuan_course = Label(window, text=f'¥ {getCourse("R01375")} руб.', font=('Arial', 18))
#     yuan_course.place(y=300, x=100)
#     window.mainloop()
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.w = 907
#         self.h = 300
#         self.geometry('907x300')
#         self.title('Kelvin voice helper')
#         self.configure(bg='white')
#         self.label1 = PhotoImage(file='label.png')
#         self.label2 = PhotoImage(file='label2.png')
#         self.window_logo = Label(self, image=self.label1)
#         self.window_logo.place(x=0, y=0)
#         self.window_logo2 = Label(self, image=self.label2)
#         self.window_logo2.place(x=10, y=50)
#         self.photo = PhotoImage(file = "mic.png")
#         mic_button = Button(self,image=self.photo ,fg='#63f',compound=RIGHT,command=self.kelvin)
#         mic_button.place(x=self.w//2, y=100, width=54, height=54)
#         self.label = Label(self,text='Кельвин ожидает...',bg='#63f',fg='white')
#         self.label.place(x=100, y=134)
#         self.tips = Label(text='Подсказки:'+'\nЧтобы включить аркадную игру'+
#                           '\n скажите "аркада" или\n "включи игру"'+
#                           '(также "игра" и др).'+
#                           '\n Чтобы узнать курс валют,скажите\n"курс рубля'+' или "какой сегодня курс".'+
#                           '\nTакже с ботом можно здороваться и прощаться.',
#                             font=('Arial', 12),bg='white', fg='#63f')
#         self.tips.place(x=520, y=90)
#     def kelvin(self):
#         self.kelvin_status()
#         window.update()
#         self.mic_func1()
#     def kelvin_status(self):
#         self.label.config(text="Кельвин вас слушает...")
#     def mic_func1(self):
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=1) as source:
#             print('...')
#             audio = r.listen(source,timeout=3)
#         speech = r.recognize_google(audio, language='ru_RU').lower()
#         # print(speech)
#         greatings_list = ['здарова','приветствую', 'здраствуй путник',"привет", "здравствуйте", "добрый день",
#                          "доброе утро", "добрый вечер", "пдорово", "приветствую", "здравствуй", "здравия желаю", 
#                          "рад видеть тебя", "рад приветствовать тебя", "салют", "приветики", "привет друг", "приветствую тебя"]
#         poka_list = ["пока", "до свидания", "до скорого", "до встречи", "счастливо", "удачи", "всего хорошего", "прощай", "бывай"]
#         stop_words = ['остановись', 'стоп', 'прекрати','закончи' ,'останови', 'забудь']
#         play_word_list = ['включи игру','врубай игру', 'давай поиграем', 'хочу играть', 'игра', "хочу поиграть", "играть", "врубай игрулю",
#                            "запускай игру","аркаду включи", "включи аркаду", "аркаду", 'аркада', 'Аркада']
#         greatings_list_kelvin = ['здарова кельвин', 'приветствую кельвин', 'здраствуй путник кельвин',"привет кельвин",
#                            "здравствуйте кельвин", "добрый день кельвин", "доброе утро кельвин", "добрый вечер кельвин", 
#                            "пдорово кельвин", "приветствую кельвин", "здравствуй кельвин", "здравия желаю кельвин", "рад видеть тебя кельвин",
#                              "рад приветствовать тебя кельвин", "салют кельвин", "приветики кельвин", "привет друг кельвин", "приветствую тебя кельвин"]
        
#         poka_list_kelvin = ["пока кельвин", "до свидания кельвин", "до скорого кельвин", 
#                      "до встречи кельвин", "счастливо кельвин", "удачи кельвин", "всего хорошего кельвин", 
#                      "прощай кельвин", "бывай кельвин"]
#         play_word_list_kelvin = ['включи игру кельвин','врубай игру кельвин', 'давай поиграем кельвин', 'хочу играть кельвин', 'игра кельвин', "хочу поиграть кельвин", "играть кельвин",
#                            "врубай игрулю кельвин", "запускай игру кельвин","аркаду включи кельвин", "включи аркаду кельвин", "аркаду кельвин"]
#         stop_words_kelvin = ['остановись кельвин', 'стоп кельвин', 'прекрати кельвин','закончи кельвин' ,'останови кельвин', 'забудь кельвин']
#         kelvin_greatings_list = ['кельвин здарова', 'кельвин приветствую', 'кельвин здраствуй путник', 'кельвин привет', 'кельвин здравствуйте', 
#                                  'кельвин добрый день', 'кельвин доброе утро', 'кельвин добрый вечер', 
#                                  'кельвин здорово', 'кельвин приветствую', 'кельвин здравствуй', 
#                                 'кельвин здравия желаю', 'кельвин рад видеть тебя', 'кельвин рад приветствовать тебя', 'кельвин салют', 
#                                 'кельвин приветики', 'кельвин привет друг', 'кельвин приветствую тебя']
#         kelvin_poka_list = ['кельвин пока', 'кельвин до свидания', 'кельвин до скорого', 
#                             'кельвин до встречи', 'кельвин счастливо', 'кельвин удачи', 'кельвин всего хорошего', 'кельвин прощай', 'кельвин бывай']
#         kelvin_stop_words = ['кельвин остановись', 'кельвин стоп', 'кельвин прекрати', 'кельвин закончи', 'кельвин останови', 'кельвин забудь']
#         kelvin_play_word_list = ['кельвин включи игру', 'кельвин врубай игру', 'кельвин давай поиграем', 'кельвин хочу играть', 'кельвин игра', 
#                                  'кельвин хочу поиграть', 'кельвин играть', 'кельвин врубай игрулю', 'кельвин запускай игру', 'кельвин аркаду включи', 'кельвин включи аркаду', 
#                                  'кельвин аркаду']
#         kurse_word_list = ['какой сегодня курс', 'курс валют на сегодня', 'курс валют', 'курс доллара', 'курс евро','курс юаня', 'курс рубля','покажи курс на сегодня',
#                             'покажи курс валют','курс на сегодня']
#         stat_kelvin = self.label.config(text="Кельвин ожидает...")
#         if speech in greatings_list:
#             answer = random.choice(greatings_list)
#             print(answer +'!')
#             stat_kelvin
#         elif speech in poka_list:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer+'!')
#             stat_kelvin
#         elif speech in greatings_list_kelvin:
#             answer = random.choice(greatings_list)
#             print(answer+'!')
#             stat_kelvin
#         elif speech in poka_list_kelvin:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer+'!')
#             stat_kelvin
#         elif speech in kelvin_greatings_list:
#             answer = random.choice(greatings_list)
#             print(answer+'!')
#             stat_kelvin
#         elif speech in kelvin_poka_list:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer+'!')
#             stat_kelvin
#         else:
#             None
#             stat_kelvin
#         if speech in stop_words:
#             stat_kelvin
#             print('Остановка...')
#             return
#         elif speech in stop_words_kelvin:
#             stat_kelvin
#             print('Остановка...')
#             return
#         elif speech in kelvin_stop_words:
#             stat_kelvin
#             print('Остановка...')
#             return
#         else:
#             None
#             self.mic_func1  
#             stat_kelvin
#         if speech in play_word_list:
#             print('Запускаю игру...')
#             game()
#         elif speech in play_word_list_kelvin:
#             print('Запускаю игру...')
#             game()
#         elif speech in kelvin_play_word_list:
#             print('Запускаю игру...')
#             game()
#         else:
#             None
#             stat_kelvin
#         if speech in kurse_word_list:
#             print('Открываю приложение с курсом валют...')
#             kurse()
#         else:
#             None
# if __name__ == "__main__":
#     window = App()
#     window.mainloop()

# window.mainloop()
# # Изменения:

# # 1. Убраны закомченные строки.

# # 2. Объект `window` инициализируется в `__init__`.

# # 3. Кнопка `mic_button` располагается относительно `self`, а не в новом окне.

# # 4. `mic_button` вызывает `mic_func1` при нажатии, а не `mic_func2`.

# # 5. В `mic_func1` добавлен вызов `window.mainloop()`, чтобы окно продолжало работать после распознания речи.



########


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6.03.23
# from tkinter import *
# import time
# import random

# class Ball():

#     def __init__(self, canvas,platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1  # чтобы мяч двигался вверх
#         self.touch_bottom = False
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -2.5
            
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= platform.pos[0] and self.pos[0] <= platform_pos[2]:
#             if self.pos[3] >= platform.pos[1] and self.pos[3] <= platform_pos[3]:
#                 return True
#         return False

# class Platform():

#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill = color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2

#     def right(self, event):
#         if self.pos[2] <=500:
#             self.x = 2
    
#     def stop(self, event):
#             self.x = 0

#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#         if self.pos[2] >=500:
#             self.x = 0
        
# window = Tk()
# window.title("Аркада")
# window.resizable(0, 0)
# window.wm_attributes('-topmost', 1)

# canvas = Canvas(window, width=500, height=400)
# canvas.pack()

# platform = Platform(canvas, 'green')
# ball = Ball(canvas,platform, 'red')

# while True:
#     if ball.touch_bottom:
#         break
#     else:
#         platform.draw()
#         ball.draw()
#     window.update()
#     time.sleep(0.01)
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 0.03.23




# Вы можете запечатать этот код в функцию с именем "game", следующим образом:

# from tkinter import *
# import time
# import random
# class Ball():
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1  # чтобы мяч двигался вверх
#         self.touch_bottom = False
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -2.5
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= self.platform.pos[0] and self.pos[0] <= platform_pos[2]:
#             if self.pos[3] >=self.platform.pos[1] and self.pos[3] <= platform_pos[3]:
#                 return True
#         return False
# class Platform():
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2
#     def right(self, event):
#         if self.pos[2] <= 500:
#             self.x = 2
#     def stop(self, event):
#             self.x = 0
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#         if self.pos[2] >= 500:
#             self.x = 0
# def game():
#     window = Tk()
#     window.title("Аркада")
#     window.resizable(0, 0)
#     window.wm_attributes('-topmost', 1)

#     canvas = Canvas(window, width=500, height=400)
#     canvas.pack()

#     platform = Platform(canvas, 'green')
#     ball = Ball(canvas, platform, 'red')

#     while True:
#         if ball.touch_bottom:
#             break
#         else:
#             platform.draw()
#             ball.draw()
#         window.update()
#         time.sleep(0.01)
#     window.mainloop()
# game()



# import time
# import tkinter as tk
# import datetime
# import random
# import speech_recognition as sr
# from tkinter import *

# class Ball():
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1  # чтобы мяч двигался вверх
#         self.touch_bottom = False
#         self.points = 0
#     def draw(self):
#         self.points_label = Label(text=self.points,font="Arial 15", fg='blue', bg='white')
#         self.points_label.place(x=10, y = 10)
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -2.5
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= self.platform.pos[0] and self.pos[0] <= platform_pos[2]:
#             if self.pos[3] >=self.platform.pos[1] and self.pos[3] <= platform_pos[3]:
#                 self.points += 1
#                 return True 
#         return False
# class Platform():
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2
#     def right(self, event):
#         if self.pos[2] <= 500:
#             self.x = 2
#     def stop(self, event):
#             self.x = 0
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#         if self.pos[2] >= 500:
#             self.x = 0
# def game():
#     window = Tk()
#     window.title("Аркада")
#     window.resizable(0, 0)
#     window.wm_attributes('-topmost', 1)
#     canvas = Canvas(window, width=500, height=400)
#     canvas.pack()
#     platform = Platform(canvas, 'green')
#     ball = Ball(canvas, platform, 'red')
#     while True:
#         if ball.touch_bottom:
#             window.destroy()
#             break
#         else:
#             platform.draw()
#             ball.draw()
#         window.update()
#         time.sleep(0.01)
#     window.mainloop()
# game()





# import time
# import tkinter as tk
# import random
# import speech_recognition as sr
# from tkinter import *
# import requests                 
# from bs4 import BeautifulSoup   
# from datetime import datetime 
# import wikipedia
# import textwrap

# class Ball():
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1  # чтобы мяч двигался вверх
#         self.touch_bottom = False
#         self.points = 0
        
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -2.5
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= self.platform.pos[0] and self.pos[0] <= platform_pos[2]:
#             if self.pos[3] >=self.platform.pos[1] and self.pos[3] <= platform_pos[3]:
#                 self.points +=1
#                 return True 
#         return False
# class Platform():
#     def __init__(self,canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2
#     def right(self, event):
#         if self.pos[2] <= 500:
#             self.x = 2
#     def stop(self, event):
#             self.x = 0
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#         if self.pos[2] >= 500:
#             self.x = 0
# def game():
#     window = Tk()
#     window.title("Аркада")
#     window.resizable(0, 0)
#     window.wm_attributes('-topmost', 1)
#     canvas = Canvas(window, width=500, height=400)
#     canvas.pack()
#     platform = Platform(canvas, 'green')
#     ball = Ball(canvas, platform, 'red')
#     points_label = Label(text=ball.points,font="Arial 15", fg='blue', bg='white')
#     points_label.place(x=10, y = 100)
        
#     while True:
#         if ball.touch_bottom:
#             window.destroy()
#             points_label.destroy()
#             break
#         else:
#             platform.draw()
#             ball.draw()
#             points_label.config(text=f"Очки: {ball.points}")
#         window.update()
#         time.sleep(0.01)
#     window.mainloop()
# def kurse(): 
#     window = Tk()
#     window.geometry('400x350+300+300')
#     window.title('Курс валют')
#     window.resizable(width=False, height= False)
#     img = PhotoImage(file='logo.png')
#     logo = Label(window, image=img)
#     logo.place(x=0, y=0)
#     img2 = PhotoImage(file='usd.png')
#     usd_pic = Label(window, image=img2)
#     usd_pic.place(y=190, x=40)
#     img3 = PhotoImage(file='eu.png')
#     eu_pic = Label(window, image=img3)
#     eu_pic.place(y=250, x=40)
#     img4 = PhotoImage(file='chinf.png')
#     china_pic = Label(window, image=img4)
#     china_pic.place(y=300, x=40)
#     tablo = Label(window, text='Курс валют', font=('Arial', 22))
#     tablo.place(x=150, y=25)
#     url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#     today = datetime.today()
#     today = today.strftime("%d/%m/%Y")
#     payload = {"date_req" : today}
#     responce = requests.get(url, params=payload)
#     xml = BeautifulSoup(responce.content, "html.parser")
#     def getCourse(id):
#         return xml.find("valute",  {'id': id}).value.text
#     course_date = Label(window, text=f'Курс валют на {today.replace("/", ".")}', font=('Arial', 18))
#     course_date.place(y=150, x=90)
#     usd_course = Label(window, text=f'$ {getCourse("R01235")} руб.', font=('Arial', 18))
#     usd_course.place(y=190, x=100)
#     eur_course = Label(window, text=f'€ {getCourse("R01239")} руб.', font=('Arial', 18))
#     eur_course.place(y=250, x=100)
#     yuan_course = Label(window, text=f'¥ {getCourse("R01375")} руб.', font=('Arial', 18))
#     yuan_course.place(y=300, x=100)
#     window.mainloop()
# class App(tk.Tk):

#     def __init__(self):
#         super().__init__()
#         size_of_window = "907x450"
#         self.w = 907
#         self.h = 450
#         self.geometry(size_of_window)
#         self.title('Kelvin voice helper')
#         self.configure(bg='white')
#         self.label1 = PhotoImage(file='label.png')
#         self.label2 = PhotoImage(file='label2.png')
#         self.window_logo = Label(self, image=self.label1)
#         self.window_logo.place(x=0, y=0)
#         self.window_logo2 = Label(self, image=self.label2)
#         self.window_logo2.place(x=10, y=50)
#         self.photo = PhotoImage(file = "mic.png")
#         mic_button = Button(self,image=self.photo ,fg='#63f',compound=RIGHT,command=self.kelvin)
#         mic_button.place(x=self.w//2, y=100, width=54, height=54)
#         self.label = Label(self,text='Кельвин ожидает...',bg='#63f',fg='white')
#         self.label.place(x=100, y=134)
#     def kelvin(self):
#         self.kelvin_status()
#         window.update()
#         self.mic_func1()
#     def kelvin_status(self):
#         self.label.config(text="Кельвин вас слушает...")
#     def mic_func1(self):
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=1) as source:
#             print('...')
#             audio = r.listen(source)
#         speech = r.recognize_google(audio, language='ru_RU').lower()
#         # print(speech)
#         greatings_list = ['здарова','приветствую', 'здраствуй путник',"привет", "здравствуйте", "добрый день",
#                          "доброе утро", "добрый вечер", "пдорово", "приветствую", "здравствуй", "здравия желаю", 
#                          "рад видеть тебя", "рад приветствовать тебя", "салют", "приветики", "привет друг", "приветствую тебя"]
#         poka_list = ["пока", "до свидания", "до скорого", "до встречи", "счастливо", "удачи", "всего хорошего", "прощай", "бывай"]
#         stop_words = ['остановись', 'стоп', 'прекрати','закончи' ,'останови', 'забудь']
#         play_word_list = ['включи игру','врубай игру', 'давай поиграем', 'хочу играть', 'игра', "хочу поиграть", "играть", "врубай игрулю",
#                            "запускай игру","аркаду включи", "включи аркаду", "аркаду"]
#         greatings_list_kelvin = ['здарова кельвин', 'приветствую кельвин', 'здраствуй путник кельвин',"привет кельвин",
#                            "здравствуйте кельвин", "добрый день кельвин", "доброе утро кельвин", "добрый вечер кельвин", 
#                            "пдорово кельвин", "приветствую кельвин", "здравствуй кельвин", "здравия желаю кельвин", "рад видеть тебя кельвин",
#                              "рад приветствовать тебя кельвин", "салют кельвин", "приветики кельвин", "привет друг кельвин", "приветствую тебя кельвин"]
        
#         poka_list_kelvin = ["пока кельвин", "до свидания кельвин", "до скорого кельвин", 
#                      "до встречи кельвин", "счастливо кельвин", "удачи кельвин", "всего хорошего кельвин", 
#                      "прощай кельвин", "бывай кельвин"]
#         play_word_list_kelvin = ['включи игру кельвин','врубай игру кельвин', 'давай поиграем кельвин', 'хочу играть кельвин', 'игра кельвин', "хочу поиграть кельвин", "играть кельвин",
#                            "врубай игрулю кельвин", "запускай игру кельвин","аркаду включи кельвин", "включи аркаду кельвин", "аркаду кельвин"]
#         stop_words_kelvin = ['остановись кельвин', 'стоп кельвин', 'прекрати кельвин','закончи кельвин' ,'останови кельвин', 'забудь кельвин']
#         kelvin_greatings_list = ['кельвин здарова', 'кельвин приветствую', 'кельвин здраствуй путник', 'кельвин привет', 'кельвин здравствуйте', 
#                                  'кельвин добрый день', 'кельвин доброе утро', 'кельвин добрый вечер', 
#                                  'кельвин здорово', 'кельвин приветствую', 'кельвин здравствуй', 
#                                 'кельвин здравия желаю', 'кельвин рад видеть тебя', 'кельвин рад приветствовать тебя', 'кельвин салют', 
#                                 'кельвин приветики', 'кельвин привет друг', 'кельвин приветствую тебя']
#         kelvin_poka_list = ['кельвин пока', 'кельвин до свидания', 'кельвин до скорого', 
#                             'кельвин до встречи', 'кельвин счастливо', 'кельвин удачи', 'кельвин всего хорошего', 'кельвин прощай', 'кельвин бывай']
#         kelvin_stop_words = ['кельвин остановись', 'кельвин стоп', 'кельвин прекрати', 'кельвин закончи', 'кельвин останови', 'кельвин забудь']
#         kelvin_play_word_list = ['кельвин включи игру', 'кельвин врубай игру', 'кельвин давай поиграем', 'кельвин хочу играть', 'кельвин игра', 
#                                  'кельвин хочу поиграть', 'кельвин играть', 'кельвин врубай игрулю', 'кельвин запускай игру', 'кельвин аркаду включи', 'кельвин включи аркаду', 
#                                  'кельвин аркаду']
#         kurse_word_list = ['какой сегодня курс', 'курс валют на сегодня', 'курс валют', 'курс доллара', 'курс евро','курс юаня', 'курс рубля','покажи курс на сегодня',
#                             'покажи курс валют','курс на сегодня']
#         stat_kelvin = self.label.config(text="Кельвин ожидает...")
#         if speech in greatings_list:
#             answer = random.choice(greatings_list)
#             print(answer)
#             stat_kelvin
#         elif speech in poka_list:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer)
#             stat_kelvin
#         elif speech in greatings_list_kelvin:
#             answer = random.choice(greatings_list)
#             print(answer)
#             stat_kelvin
#         elif speech in poka_list_kelvin:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer)
#             stat_kelvin
#         elif speech in kelvin_greatings_list:
#             answer = random.choice(greatings_list)
#             print(answer)
#             stat_kelvin
#         elif speech in kelvin_poka_list:
#             bye_anwer = random.choice(poka_list)
#             print(bye_anwer)
#             stat_kelvin
#         else:
#             None
#             stat_kelvin
#         if speech in stop_words:
#             stat_kelvin
#             return
#         elif speech in stop_words_kelvin:
#             stat_kelvin
#             return
#         elif speech in kelvin_stop_words:
#             stat_kelvin
#             return
#         else:
#             None
#             self.mic_func1  
#             stat_kelvin
#         if speech in play_word_list:
#             game()
#         elif speech in play_word_list_kelvin:
#             game()
#         elif speech in kelvin_play_word_list:
#             game()
#         else:
#             None
#             stat_kelvin
#         if speech in kurse_word_list:
#             kurse()
#         else:
#             None
# if __name__ == "__main__":
#     window = App()
#     window.mainloop()

# window.mainloop()


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 20.03.23

# name = input('Введите имя сотрудника:')
# salary = int(input('Введите зарплату сотрудника:'))
# print(f'У  {name}а(ы)  зарплата в год состовляет  {salary*12}  руб.')

# employee = {
#     'name': 'Даниил',
#     'salary': 200,
    
# }
# print(f'У  {employee["name"]}а(ы)  зарплата в год состовляет  {employee["salary"]* 12}  руб.')
# print(f'У  {employee.get( "name")}а(ы)  зарплата в год состовляет  {employee.get("salary")* 12}  руб.')
# employee['age']= 20
# employee['salary'] = 200000
# print(f'У  {employee.get( "name")}а(ы)  зарплата в год состовляет  {employee.get("salary")* 12}  руб.' + 
#       f' Eму {employee.get("age")} лет.')


# Если сотрудников много:
# employees_list = [
#     {
#     'name': 'Даниил',
#     'salary': 20000,
    
# },
#     {
#     'name': 'Кит',
#     'salary': 45000,
    
# },
#     {
#     'name': '???',
#     'salary': 65000,
    
# }
# ]
# print(employees_list[0])
# print(employees_list[-1])
# print(employees_list[-2])

# через цикл:

# employees_list = [
#     {
#     'name': 'Даниил',
#     'salary': 20000,
    
# },
#     {
#     'name': 'Кит',
#     'salary': 45000,
    
# },
#     {
#     'name': '???',
#     'salary': 65000,
    
# }
# ]
# for employee in employees_list:
#     if employee.get('name') == '???':
#         employees_list.remove(employee)
#         break
# new_employee = {
#     'name' : 'Тор',
#     'salary': 50000
# }
# employees_list.append(new_employee)   
# i=0
# for employee  in employees_list:
#     i += 1 
#     print(f'Итерация {i}')
#     print(f'У  {employee.get("name")}а(ы)  зарплата в год состовляет  {employee.get("salary")* 12}  руб.')

# print(f'В нашей компании работает следующее количество сотрудников: {len(employees_list)}')

#  ООП Исполнение

# class Employee():
#     def __init__(self,name, salary, age, on_vacation,is_good_employee):
#         self.salary = salary
#         self.name = name
#         self.on_vacation = on_vacation
#         self.age = age
#         self.is_good_employee = is_good_employee
#     def print_info(self):
#         print(f'У  {self.name}а(ы)  зарплата в год состовляет  {self.salary* 12}  руб. '+ f'Отпуск {self.on_vacation}')
# employees_list = [
#     Employee('Даниил', 200000, 25,True,True),
#     Employee('Иван', 322200, 32,False,True),
#     Employee('Андрей', 141680,28,False,True),
#     Employee('Эдуард', 425780, 35,False,True),
#     Employee('Максим',224000,29,True,False)
# ]
        
# for employee  in employees_list:
#     employee.print_info()
# for employee in employees_list:
#     if employee.is_good_employee == False:
#         employees_list.remove(employee)
# for employee  in employees_list:
#     print('Обновленный список сотрудников \n')
#     employee.print_info()
    
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 27.03.23
# Vk BOT
# import vk_api           # pip install vk_api (Выбор версии интерпретатора Python: ctr + shift + p -> Python: Select Interpreter)
# from course import *
# from planets import *    # нужно чтобы файл course.py находился в той же папке что и этот код
# import time
# from ships import*
# my_token = 'vk1.a.dwMNavUlGsmKAp6nKZOiMR_zqTMGUiUZcYUtKzPGeqHc4wu4aL82a7Cs8TsaAGXc2aQddLd4ENmbTM_Ncs8xf3DNgLCt50ouBhH5JwIEjaPCxohkXLSjk2aJrQZ9S7W5Bvyg772VgHQXDTOpuIcYGBNaU1KiZ9kzSwRrEyjMkjZFQ_eGVBjjMLBK8zGF4W3kISBGOQVYZ110FMkFOfW6yQ'
# vk = vk_api.VkApi(token=my_token)
# vk._auth_token()
# # Если возникает ошибка: vk_api.exceptions.ApiError: [901] Can't send messages for users without permission
# # тогда нужно что-то написать именно в чат сообщества
# while True:

#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:

#         user_id = messages['items'][0]['last_message']['from_id']   # id пользователя который пишет
#         message_id = messages['items'][0]['last_message']['id']     # id сообщения
#         message_text = messages['items'][0]['last_message']['text'] # текст сообщения

#         print(f'Id юзера:{user_id}, Id сообщения юзера: {message_id}, Текст сообщения юзера: {message_text}')

#         if message_text.lower() == 'сколько рублей за 1 доллар':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01235")} руб.'})

#         elif message_text.lower() == 'сколько рублей за 1 евро':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01239")} руб.'})
   
#         elif message_text.lower() == 'сколько рублей за 1 юань':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01375")} руб.'})
#         elif message_text.lower() == 'привет':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': 'Привет'})
#         elif message_text.lower() == 'планеты':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': check_planets_diameter()})
#         elif message_text.lower() == 'корабли':
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': check_starships_max_speed()})
#         else:
#             time.sleep(2)
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': 'Неизвестная команда :/'})


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 03.04.23
# Vk BOT
# import vk_api
# from course import *
# from vk_api.longpoll import VkLongPoll, VkEventType
# from wiki import get_wiki_article
# my_token = 'vk1.a.dwMNavUlGsmKAp6nKZOiMR_zqTMGUiUZcYUtKzPGeqHc4wu4aL82a7Cs8TsaAGXc2aQddLd4ENmbTM_Ncs8xf3DNgLCt50ouBhH5JwIEjaPCxohkXLSjk2aJrQZ9S7W5Bvyg772VgHQXDTOpuIcYGBNaU1KiZ9kzSwRrEyjMkjZFQ_eGVBjjMLBK8zGF4W3kISBGOQVYZ110FMkFOfW6yQ'
# vk_session = vk_api.VkApi(token=my_token)
# vk_session._auth_token()
# longpoll = VkLongPoll(vk_session)
# vk = vk_session.get_api()

# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         user_id =  event.user_id
#         message_id =  event.message_id
#         text = event.text.lower()
#         print(f'Id юзера:{user_id}, Id сообщения юзера: {message_id}, Текст сообщения юзера: {text}')
#         if text.startswith('-к'):
#             if text[0:6] == '-к usd':    
#                 response = f'{get_course("R01235")} рублей за 1 доллар'
#             elif text[0:6] == '-к eur':
#                 response = f'{get_course("R01239")} рублей за 1 евро'
#             elif text[0:6] == '-к gbp':
#                 response = f'{get_course("R01035") } рублей за 1 фунт'
#             elif text[0:6] == '-к cny':
#                 response = f'{get_course("R01375")} рублей за 1 юань' 
#         elif text == 'привет':
#             response = 'Привет!'
#         elif  text == 'дарова':
#             response = 'Дарова!'
#         # elif text[0:2] == '-в':
#         elif text.startswith('-в'):
#             article = text[3:]
#             response = get_wiki_article(article)
#             if len(response) >= 4000:
#                 response = response[0:4000]
            
#         else:
#             response = 'Неизвестная команда, чтобы узнать курс рубля напшите "-к",чтобы сделать запрос в википедию напишите "-в "ваш запрос""".'
        
#         vk.messages.send(user_id=user_id, random_id=message_id, message=response)



# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10.04.23
# ЛЕНИВЫЕ ВЫЧИСЛЕНИЯ
# import time

# my_list = [time.sleep(x) for x in range(1,3)]
# print(my_list)

# my_lazy_list = (time.sleep(x) for x in range(1,3))
# for elem in my_lazy_list:
#     print(elem)

# print(my_lazy_list)

# my_range = range(1,10)
# print(my_range)
# print(list(my_range))


# def my_lazy_fan():
#     for i in range(1,11):
#         print(f'До {i}')
#         yield i 
#         print(f'После {i}')

# for i in my_lazy_fan():
#     print(i)


# my_list = list(my_lazy_fan())
# print(my_list)

# print(my_lazy_fan())




# def my_lazy_fan(items):
#     yield from items
# items = ['Яблоко', 'Банан', 'Апельсин']

# for i in my_lazy_fan(items):
#     print(i)

# import contextlib

# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Входим в контекстный менеджер: ')
#     yield my_str[::-1]
#     print('Выходим из контекстного менеджера: ')
# with str_reverse('Hello, world!') as reversed_str:
#     print(f'Выполняется код: {reversed_str}')

# @contextlib.contextmanager
# def exception_handler(exception):
#     try:
#         yield True
#     except exception:
#         print('Произошло исключение')
# with exception_handler(IndexError):
#     my_list = [1, 2]
#     print(my_list[5])
#     print(my_list[0])


# ПЕРЕД ТЕМ КАК ДЕЛАТЬ ДЗ ЧЕКНУТЬ ВИДЕО В ТГ ИЗБРАННОЕ

# my_list = [x^2 for x in range(1,1000000)]
# print(my_list)

# def my_lazy_fan():
#     for i in range(1,1000000):
#         yield i^2
       
# my_lazy_fan()


# def my_lazy_fan():
#     for i in range(0,1000000):
#         yield i^2 
# for i in my_lazy_fan():
#     my_list = []
#     my_list.append(i)
# print(my_list)



# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# url = "http://www.cbr.ru/scripts/XML_daily.asp"
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
# payload = {"date_req": today}
# response = requests.get(url, params=payload)
# xml = BeautifulSoup(response.content, 'xml')
# def get_course(currency):
#     try:
#         currency_info = xml.find("Valute", {'ID': currency})
#         currency_name = currency_info.find('Name').text
#         currency_value = currency_info.find('Value').text
#         currency_nominal = currency_info.find('Nominal').text
#         return f'({currency_nominal}шт.) {currency_name} стоит(ят) {currency_value} рублей.'
#     except AttributeError:
#         return f'Валюта не найдена.'
    
# print(get_course("R01235"))

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 17.04.23
# import time 
# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
        
#     def __enter__(self):
#         self.start = time.time()
#         return self
#     def __exit__(self,exc_type, exc_val, exc_tb):
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb)
#         t = time.time() - self.start
#         print(f'Время работы кода: {t}')
#         if exc_type == TypeError:
#             return True
#         if exc_type == IndexError:
#             return True
# with RunningCodeJudge() as t1:
#     my_list = [x for x in range(1, 10000000)]
#     my_list[122321321] -= 's'
#     print(t1)



# my_list = [1,2,3,4,5]
# list_iterator = iter(my_list)
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# print('-')
# for i in list_iterator:
#     print(i)
# import random
# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#     def __iter__(self):
#         self.limit = self.__reload
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit -= 1
#         return random.randint(0,100)
# rand_iter = RandomIter(3)
# for rand_int in rand_iter:
#     print(rand_int)
# print('-'* 20)
# for rand_int in rand_iter:
#     print(rand_int)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 24.04.23


# class MyFile:
#     def __init__(self,name, mode, encoding="utf-8"):
#         self.name = name
#         self.mode = mode
#         self.encoding = encoding
#     def __enter__(self):
#         self.my_file = open(self.name,self.mode,encoding = self.encoding)
#         return self.my_file
#     def __exit__(self,name,mode,encoding):
#         self.my_file.close()
#         return self.my_file

# with MyFile(name='test.text',mode='w') as my_file:
#     my_file.write('Hello, world!')
# import random
# class InfinityIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#     def __iter__(self):
#         self.limit = self.__reload
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit += 1
#         return random.randint(0,1000)
# rand_iter = InfinityIter(1)
# for rand_int in rand_iter:
#     print(rand_int)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 24.04.23
# web
# class Year:
#     def __init__(self, days,season):
#         self.__days = days
#         self.__season = season
#     def get_days(self):
#         return self.__days
#     def get_season(self):
#         return self.__season
#     def set_days(self, days):
#         if days == 365 or days== 366:
#            self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#     def set_season(self, season):
#         self.__season = season
# year = Year(365, 'Зима')
# print(year.get_days(),year.get_season())
# year.set_days(365)
# year.set_season('осень')
# print(year.get_days(), year.get_season())

# class Person:
#     def __init__(self, name,age):
#         self.__name= name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name 
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age <= 0:
#             raise ValueError('Еще не родился') 
#         self.age = age 
# person = Person('Иван', 40)
# print(Person.name)
# print(Person.age)
# person.name = 'колян'
# person.age = 22
# print(Person.name)
# print(Person.age)




# class My_list(list):
#     def delete_last_elem(self):
#         self.remove(self[-1])
        



# class Year:
#     def __init__(self, days,season):
#         self.__days = days
#         self.__season = season
#     @property
#     def days(self):
#         return self.__days
#     @days.setter
#     def days_setter(self,days):
#         if days == 365 or days== 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#     @property
#     def season(self):
#         return self.__season
#     @season.setter
#     def set_season(self, season):
#         self.__season = season
#     @season.deleter
#     def del_season(self):
#         del self.season
# year = Year(365, 'Зима')
# print(year.days)
# print(year.season)
# del Year.season




# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.05.23
# web


# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#     def __add__(self,other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price + other
#     def __sub__(self,other):  #__sub__ магический метод вычитания
#         if isinstance(other, Item):
#             return self.price - other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price - other
#     def __mul__(self,other):   #__mul__ -  магический метод умножения
#         if isinstance(other, Item):
#             return self.price * other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price * other
#     def __truediv__(self,other): #__truediv__ - магический метод деления
#         if isinstance(other, Item):
#             return self.price / other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price / other
# item_1 = Item('Видеокарта',15, 0.8)
# item_2 = Item('Процессор',12,0.1)
# total_price_1 = item_1 + item_2
# total_price_2 = item_1 - item_2
# total_price_3 = item_1 * item_2
# total_price_4 = item_1 / item_2
# print(total_price_1, total_price_2,total_price_3,total_price_4)

# # Alchimistry
# from tkinter import *
# from random import *
# window = Tk()
# window.geometry('600x600')
# class Fire:
#     image = PhotoImage(file='elements\_fire.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Ground):
#             return Clay
#         elif isinstance(other, Water):
#             return Steam
# class Water:
#     image = PhotoImage(file='elements\water.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Steam
#         elif isinstance(other,Dust):
#             return Ground
#         elif isinstance(other, Air):
#             return Tornado
# class Air:
#     image = PhotoImage(file='elements\wind.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Tornado
# class Clay:
#     image = PhotoImage(file='elements\pottery.png').subsample(4,4)
# class Aroma:
#     image = PhotoImage(file='elements\_aroma.png').subsample(4,4)
# class Ground:
#     image = PhotoImage(file='elements\ground.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
# class Dust:
#     image = PhotoImage(file='elements\dust.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Ground
# class Steam:
#     image = PhotoImage(file='elements\steam_.png').subsample(4,4)
# class Tornado:
#     image = PhotoImage(file='elements\_tornado.png').subsample(4,4)
    
# canvas = Canvas(window,width=600, height=600)
# canvas.pack()
# elements = [Ground(), Fire(), Water(), Air(), Dust()]
# for elem in elements:
#     canvas.create_image(randint(50,550), randint(50,550), image=elem.image)
# def move(event):
#     image_id = canvas.find_overlapping(event.x,event.y,event.x+10,event.y+10)
#     print(image_id)
#     if len(image_id) == 2:
#         elem_id_1, elem_id_2 = image_id[0], image_id[1]
#         element_1 = elements[elem_id_1-1]
#         element_2 = elements[elem_id_2-1]
#         new_element = None
#         try:
#             new_element = element_1 + element_2
#         except TypeError:
#             print('Нет такого элемента')
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(randint(50,550), randint(50,550), image=new_element.image)
#                 elements.append(new_element)
            
#     canvas.coords(image_id,event.x, event.y)
# window.bind('<B1-Motion>',move)
# window.mainloop()

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 08.05.23
# web
# sorted
# if __name__ == '__main__':
# from pprint import pprint
# goods = [
#     {
#         'name': 'Iphone',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'REALME C25s',
#         'brand': 'REALME',
#         'price': 650
#     }
# ]

# def item_price(item):
#     return item['price']

# print(sorted(goods, key=item_price))
# print(sorted(goods, key=lambda item: item['price'])) #lambda
# pprint(sorted(goods, key=lambda item: item['price'])) #lambda + pprint


# Функция filter
# apple_list = list(filter(lambda item: item['brand']== "Apple", goods))
# pprint(apple_list)

# MAP

# numbers_list = ['1','2','3','4','5']

# numbers_list = list(map(int, numbers_list))
# print(numbers_list)

# names_list = ['Данил', 'Никита', 'Настя']
# surnames_list = ['Петров', 'Кипров', 'Бабиджонова']
# # full_names_list = list(map(lambda name, surname:f'{name} {surname}', names_list, surnames_list))
# # pprint(full_names_list)

# # ENUMERATE

# from pprint import pprint
# goods = [
#     {
#         'name': 'Iphone',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'REALME C25s',
#         'brand': 'REALME',
#         'price': 650
#     }
# ]
# indexed_goods = []

# for i, item in enumerate(goods):
#     indexed_goods.append({i : item})

# pprint(indexed_goods)
# patronymic_list = ['Данилович', 'Никитич', 'Олеговна']
# for name, surname,patronymic in zip(names_list, surnames_list,patronymic_list):
#     print(name, surname, patronymic)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 13.05.23
# from pprint import *
# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def __repr__(self):
#         return f"{self.brand}({self.price})"
# items_list = (
#     Item(1000,'Apple'),
#     Item(1200,'Apple'),
#     Item(900,'Samsung'),
#     Item(700,'Samsung'),
#     Item(660,'Xiaomi')
# )
# apple_list = list(filter(lambda Item: Item.brand == "Apple", items_list))
# pprint(apple_list)


# names_list = ['данил', 'артём', 'никита', 'влад']

# fixed_names_list = list(map(lambda name: name.capitalize(),names_list))
# print(fixed_names_list)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 28.05.23
# web
# import sqlite3

# try:
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
# except sqlite3.DatabaseError:
#     print('Произошла ошибка подключения :/')

# finally:
#     connection.close()


#  тоже самое через контекстный менеджер
# class User:
#     def __init__(self,name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
# def create_table_user(cursor):
#     command = """
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             surname TEXT, 
#             gender TEXT
#         );
#         """
#     cursor.execute(command)
# def add_user(cursor, user):
#     command = """
#     iNSERT INTO users (name, surname, gender) VALUES (?,?,?);
#     """
#     cursor.execute(command, (user.name, user.surname, user.gender))
# def get_all_users_list(cursor):
#     command = """
#     SELECT * FROM users;
#     """
#     result = cursor.execute(command)
#     users = result.fetchall()
#     print(users)
# def get_user_by_id(cursor, user_id):
#     command = """
#     SELECT * FROM users WHERE id = ?;
#     """
#     result = cursor.execute(command, (user_id,))
#     user_id = result.fetchall()
#     print(user_id)
# def user_name_update_by_id(cursor,value, user_id):
#     command ="""
#     UPDATE users SET name = ? WHERE id = ?;
#     """
#     cursor.execute(command, (value,user_id))
# def clear_table(cursor):
#     command ="""
#     DELETE FROM users;
#     """
#     cursor.execute(command)
# def delete_user_by_id(cursor, user_id):
#     command ="""
#     DELETE FROM users 
#     WHERE id = ?;
#     """
#     cursor.execute(command, (user_id,))
# def get_user_by_gender(cursor,user_gender):
#     command = """
#     SELECT * FROM users WHERE gender = ?;
#     """
#     result = cursor.execute(command, (user_gender,))
#     user_id = result.fetchall()
#     print(user_id)
# if __name__ == '__main__':
#     with sqlite3.connect('data.db') as cursor:
#         clear_table(cursor)
#         create_table_user(cursor)
#         add_user(cursor, User(name='Максим', surname='Иванов', gender='male'))
#         add_user(cursor, User(name='Владимир', surname='Петров', gender='male'))
#         add_user(cursor, User(name='Ксения', surname='Иванова', gender='female'))
#         get_all_users_list(cursor)
#         # get_user_by_id(cursor, 1)
#         # user_name_update_by_id(cursor,' Иван', 1)
#         # get_user_by_id(cursor, 1)
#         # delete_user_by_id(cursor, 2)
#         # get_all_users_list(cursor)
#         get_user_by_gender(cursor, 'female')
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 29.05.23
# web
# import os
# current_path = os.path.abspath(__file__)
# # print(__file__)
# # print(current_path)
# parent_path = os.path.join(current_path,'..')
# print(parent_path)

# # def recurs(count):
# #     print(count)
# #     if count ==5:
# #         return
# #     recurs(count + 1)
# #     print(count)

# # recurs(0)


# def get_all_files(path):
#     for i_name in os.listdir(path):
#         new_path = os.path.join(path, i_name)
#         if os.path.isdir(new_path):
#             print('Папка', i_name)
#         else:
#             print('-', i_name)

# get_all_files(parent_path)






# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 12.06.23
# web

def strcounter(s): #aabc O(N + M) => O(N + N) => O(N)
    syms_counter = {}
    for sym in s: #abc M(уник)
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
        
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter('aabcddscxv')






































