# Project1
# Сейчас в мире активно обсуждается тема экологии и компания Coca-Cola обЪявила акцию
# (датой начала акции считать 01.09.2019):
# с каждого проданного литра 2% компания будет переводить деньги в фонд "Сибирь", акция расчитана на 25 лет.
#  Программа позволяет узнать какая площадь уже засажена и предположительно какая только будет на определенную дату,
#  также можно узнать сколько уже потраченно средств.
#  Всю инфомацию о колличестве проданных литров брять с официального сайта.
# Прим. Одна сосна занимает квадрат 2*2 м^2; год принимаем равный 365 дней; Сичтаем, что как только бутылка была
# купленна, дерево посажено; Никакие деревья не погибли;  Принимаем стоимость
# литра Coca-Cola 50 рублей, стоимость посадки одной сосны 5000 рублей;


import datetime



now = datetime.date(2019, 9, 1)
print('Дата начала акции:', now)
print('Дату конца периода в формате гггг, мм, дд')
a2 = int(input())  # Год
b2 = int(input())  # Месяц
c2 = int(input())  # День
then = datetime.date(a2, b2, c2)
print('Дата окончания установленного периода:', then)
print('Введите кол-во литров в год проданное компанией')
# Кол-во литров в год проданное компанией
d = int(input())
print('Введите Стоимость 1 литра')
# Стоимость 1 литра
g = int(input())
print('Введите стоимость посадки одного дерева')
# Стоимость посадки одного дерева
f = int(input())
# Кол-во деревьев в день
e = ((d/365)*g)*2/100/f

# Кол-во дней между датами.
delta = then - now
# Кол-во высаженных деревьев за период
sym = e*delta.days
# Общая площадь высаженных деревьев
S = sym*0.0004
print('Предположительное кол-во высаженных деревьев за период:', round(sym), 'ед.')
print('Предположительная площадь покрытия:', round(S, 1), 'Га')

print('Хотите ли узнать сколько позасаженно деревьев на сегодняшний день?')
answer = str(input())
if 'yes':
     now1 = datetime.date(2019, 9, 1)
     then1 = datetime.date.today()
     delta1 = then1 - now1
     sym1 = e * delta1.days
     S1 = sym1 * 0.0004
     print('Кол-во высаженных деревьев за период:', round(sym1), 'ед.')
     print('Площадь покрытия:', round(S1, 1), 'Га')
else:
    print('А жаль*(')
