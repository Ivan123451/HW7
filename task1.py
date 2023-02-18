# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
#
# Вывод:
# Парам пам-пам

verse = str(input('Винни давай стих: '))


my_list = verse.split()

glasnie = ['а', 'я', 'у', 'ю', 'о', 'ё', 'е', 'э', 'и', 'ы']


list_of_word = []

for i in range(len(my_list)):
    counter = 0
    for j in range(len(glasnie)):
        counter += my_list[i].count(glasnie[j])
    list_of_word.append(counter)

print(f'количестов гласных в каждом слове {list_of_word}')

Flag = True
for i in range(1, len(list_of_word)):
    if list_of_word[i] != list_of_word[i-1]:
        Flag = False

if Flag == True:
    print('Парам пам-пам')
else:
    print('Пам парам')


