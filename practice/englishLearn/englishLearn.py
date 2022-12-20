import pymorphy2
from translate import Translator
import csv

def getWordsNormalized(filename = "input.txt"):
    words = ""
    file = open(filename, encoding="UTF-8")
    for line in file:
        words += line.replace('\n', '')
    words = words.replace(' ', '')
    wordsNormalized = []
    morph = pymorphy2.MorphAnalyzer(lang="ru")
    for element in words:
        wordsNormalized.append(morph.parse(element)[0].normal_form)
    wordsStat = {}
    for element in wordsNormalized:
        if element in wordsStat:
            wordsStat[element] += 1
        else:
            wordsStat[element] = 1
    words = dict(sorted(wordsStat.items(), key=lambda item: -item[1]))
    translator = Translator(from_lang='ru', to_lang='en', provider='mymemory')
    data = []
    for word in words.keys():
        data.append([translator.translate(word),word,words[word]])
    with open('output.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter='|',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['перевод|слово|количество'])
        for element in data:
            writer.writerow(element)
    return data

print(getWordsNormalized())

