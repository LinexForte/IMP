#Импорт библиотек
import csv

#Определение списков
unsorted_songs = []
sorted_songs = []

#Определение функций
def compareBig(big, less):
    '''Описание функции compareBig.
        Посимвольно сравнивает строки и если предполагаемо большая строка оказалась большей возвращает True наче False
        Описание аргументов:
	    big – предполагаемо большая строка в алфовитном порядке
	    less – предполагаемо меньшая строка в алфовитном порядке
	    Описание возврата:
	    True или False
    '''
    for i in range(min(len(big), len(less))):
        if big[i] > less[i]:
            return True
        elif big[i] < less[i]:
            return False
    return False

def iterate():
    '''Описание функции iterate.
        Перебирает строки в неотсортированном списке, находит наименьший в алфовитном порядке имя автора, записывает в отсортированный список и удаляет строку из неотсортированного списка.
    '''
    minimum = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
    for row in unsorted_songs:
        if compareBig(minimum, row[1]):
            sorted_songs.append([row[2], row[1], row[3]])
            minimum = row[1]
            del row

#Сортировка
with open("songs.txt", encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file, delimiter = "?")
    unsorted_songs = file_reader
    for row in file_reader:
        iterate()

#Вывод результата
print(f"{sorted_songs[-1][0]}, {sorted_songs[-1][1]}, {sorted_songs[-1][2]}")
print(f"{sorted_songs[-2][0]}, {sorted_songs[-2][1]}, {sorted_songs[-2][2]}")
print(f"{sorted_songs[-3][0]}, {sorted_songs[-3][1]}, {sorted_songs[-3][2]}")
print(f"{sorted_songs[-4][0]}, {sorted_songs[-4][1]}, {sorted_songs[-4][2]}")
print(f"{sorted_songs[-5][0]}, {sorted_songs[-5][1]}, {sorted_songs[-5][2]}")