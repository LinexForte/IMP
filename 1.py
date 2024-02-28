#Импорт библиотек
import csv

#Ввод имени автора
author = input("Введите имя автора : ")

#Обработка и запись в файл
with open("songs.txt", encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file, delimiter = "?")
    with open("songs_artist.csv", encoding="utf-8", mode="w") as w_file:
        file_writer = csv.writer(w_file)
        file_writer.writerow(["track_name","streams","date"])
        for row in file_reader:
            if row[1] == author:
                file_writer.writerow([row[2], row[0], row[3]])