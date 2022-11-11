from random import randint

def getWordsFromFile(filename):
    file = open(filename, encoding='UTF-8')
    result = []
    for wordInLine in file:
        result.append(wordInLine.replace('\n', ''))
    return result
def updateRecord(record, filename="record.txt"):
    file = open(filename)
    oldRecord = int(file.readline())
    if oldRecord < record:
        file.write(record)
    file.close()
def play(fileWhereWordsFilename="words.txt"):
    gamePoints = 0
    words = getWordsFromFile(fileWhereWordsFilename)
    difficultyLevel = int(input('Выберите сложность от 1 до 3'));
    while str(input("Хотите сыграть? y/n")) != 'n' :
        if len(words)>0:
            wordKey = randint(0,len(words)-1)
            word = words[wordKey]
            del words[wordKey]
            livesPerGame = 4 + difficultyLevel;
            wordList = ['*' for i in range(0,len(word))];
            while True:
                print(wordList)
                symbol = str(input())
                if (symbol in word) and (symbol!=word):
                    for i in range(0,len(wordList)):
                        if word[i] == symbol:
                            wordList[i] = symbol
                            gamePoints += 1
                elif symbol == word:
                    break
                    gamePoints += 1
                else:
                    livesPerGame -= 1
                    print(livesPerGame)
                if livesPerGame == 0 :
                    break
                if not '*' in wordList:
                    break
            if livesPerGame==0:
                print('You loose')
            else:
                print('You win')
                print(word)
            updateRecord(gamePoints)
        else:
            print('GAME OVER')
            break
play('words.txt')


