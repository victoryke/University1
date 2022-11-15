
def getWordsFromFile(filename):
    file = open(filename, encoding='UTF-8')
    result = []
    for wordInLine in file:
        result.append(wordInLine.replace('\n', ''))
    return result
def updateRecord(record, filename="polechydes/record.txt"):
    file = open(filename, 'r')
    oldRecord = int(file.readline())
    file.close()
    if oldRecord < record:
        file = open(filename, 'w')
        file.write(str(record))
        file.close()