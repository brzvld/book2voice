#!/usr/bin/python3
#Читалка русских текстов голосом
#пустая строка, заканчивает читать
#https://pypi.org/project/gTTS/
from gtts import gTTS
import os


#чтение строки файла голосом
def read_file_to_voice(stroka):

  language = 'ru'

  #Создаем объект gTTS и сохраняем в файл
  tts = gTTS(text=stroka, lang=language)
  tts.save("hello.mp3")

  #Воспроизводим аудиофайл
  os.system("mpg321 hello.mp3")
  #===========================


# получим объект файла
with open("dictant.txt", "r") as file1:
    # итерация по строкам
    for line in file1:
        print(line.strip())
        read_file_to_voice(line)
