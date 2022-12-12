def findWordsInFile(filename):
    return findUniqueWordsInList(readFile(filename))
def readFile(filename):
    file = open(filename, encoding="UTF-8")
    strings = []
    for line in file:
        strings.append(line.replace('\n', ''))
    file.close()
    return strings
def findUniqueWordsInList(strings):
    uniqueWords = []
    for string in strings:
        expstring = string.split(" ")
        for element in expstring:
            if not element.lower() in uniqueWords:
                uniqueWords.append(element.lower())
    return uniqueWords
print(findWordsInFile("input.txt"))
