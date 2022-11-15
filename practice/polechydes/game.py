from random import randint
import game_main
def play(fileWhereWordsFilename="polechydes/words.txt"):
    gamePoints = 0
    words = game_main.getWordsFromFile(fileWhereWordsFilename)
    difficultyLevel = int(input('Выберите сложность от 1 до 3'));
    while True:
        if len(words) > 0:
            if str(input("Хотите сыграть? y/n")) != 'n':
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
                game_main.updateRecord(gamePoints)
            else:
                print('GAME OVER')
                break
        else:
            break

