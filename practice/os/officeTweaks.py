import os
from pdf2docx import Converter
from docx2pdf import convert
import re
from PIL import Image
import docx2pdf

def playTweaks():
    showMenu()
    choise = int(input("Введите номер"))
    while choise != 5:
        if choise == 0:
            print(changeDir())
        elif choise == 1:
            print(convertPDFtoDOCX())
        elif choise == 2:
            print(convertDOCXtoPDF())
        elif choise == 3:
            print(changeResolution())
        elif choise == 4:
            print(deleteGroupOfFiles())
        else:
            break
        showMenu()
        choise = int(input("Введите номер"))
def showMenu():
    print("Текущая директория:" + os.getcwd())
    print("0:Сменить рабочий каталог")
    print("1:Преобразовать PDF в DOCX")
    print("2:Преобразовать DOCX в PDF")
    print("3:Произвести сжатие изображений")
    print("4:Удалить группу файлов")
    print("5:Выход")
def changeDir():
    newdirname = input("Введите название директории")
    if(os.path.exists(newdirname)):
        if(os.path.isdir(newdirname)):
            os.chdir(newdirname)
    else:
        os.mkdir(newdirname)
    return "новая директория:" + newdirname

def convertPDFtoDOCX():
    filesInDirectory = os.listdir(os.getcwd())
    choise = showFilesInDirAndReturnChoise(filesInDirectory)
    pdfFile = filesInDirectory[choise]
    wordFile = pdfFile.replace('.pdf', '.docx')
    cv = Converter(pdfFile)
    cv.convert(wordFile)
    cv.close()
    return "удачно"
def showFilesInDirAndReturnChoise(filesInDirectory):
    showFilesInDir(filesInDirectory)
    choise = int(input("выберите файл"))
    return "удачно"

def convertDOCXtoPDF():
    filesInDirectory = os.listdir(os.getcwd())
    choise = showFilesInDirAndReturnChoise(filesInDirectory)
    docxFile = filesInDirectory[choise]
    pdfFile = docxFile.replace('.docx', '.pdf')
    convert(docxFile)
    return "удачно"
def changeResolution():
    filesInDirectory = os.listdir(os.getcwd())
    choise = showFilesInDirAndReturnChoise(filesInDirectory)
    imagePath = filesInDirectory[choise]
    with Image.open(imagePath) as img:
        print(img.format, img.size, img.format_description)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(imagePath, "JPEG", optimize=True, quality=1)
    return "удачно"
def deleteGroupOfFiles():
    filesInDirectory = os.listdir(os.getcwd())
    showFilesInDir(filesInDirectory)
    type = int(input("выберите тип удаления файлов 0 - фильтр, 1 - диапазон, 2-один файл"))
    if type == 0:
        patternType = int(input("введите фильтр типа 0-префикс 1-постфикс 2-подстрока 3-расширение"))
        if patternType == 0:
            substr = input('Введите префикс')
            for i in range(0, len(filesInDirectory)):
                if filesInDirectory[i].lower().startswith(substr.lower()):
                    path = f"{os.getcwd()}\{filesInDirectory[i]}"
                    os.remove(path)
        elif patternType == 1:
            substr = input('Введите постфикс')
            for i in range(0, len(filesInDirectory)):
                if filesInDirectory[i].lower().endswith(substr.lower()):
                    path = f"{os.getcwd()}\{filesInDirectory[i]}"
                    os.remove(path)
        elif patternType == 2:
            substr = input('Введите подстроку')
            for i in range(0, len(filesInDirectory)):
                if substr.lower() in filesInDirectory[i].lower():
                    path = f"{os.getcwd()}\{filesInDirectory[i]}"
                    os.remove(path)
        elif patternType == 3:
            substr = input('Введите расширение')
            for i in range(0, len(filesInDirectory)):
                if ('.'+substr.lower()) in filesInDirectory[i].lower():
                    path = f"{os.getcwd()}\{filesInDirectory[i]}"
                    os.remove(path)
    elif type == 1:
        rangeStart = int(input("начало диапазона"))
        rangeFinish = int(input("конец диапазона")) + 1
        for i in range(rangeStart,rangeFinish):
            path = f"{os.getcwd()}\{filesInDirectory[i]}"
            os.remove(path)
    elif type == 2:
        numberOfFile = int(input("Введите номер файла"))
        path = f"{os.getcwd()}\{filesInDirectory[numberOfFile]}"
        os.remove(path)

    return "удачно"
def showFilesInDir(filesInDirectory):
    for i in range(0,len(filesInDirectory)):
        print(f"{i} : {filesInDirectory[i]}")
playTweaks()