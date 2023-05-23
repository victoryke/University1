


class Cell:
    def __init__(self, coord):
        self.coord = coord
        self.value = 0
    def makeVisited(self, playerNumber):
        self.value = playerNumber

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Board:
    def __init__(self):
        self.cells = []
        for i in range(0,9):
            self.cells.append(Cell(i))
            self.cells[i].value = 0
    def showCells(self, *args, **kwargs):
        values = ['■' for i in range(0,9)]
        i = 0
        for i in range(0,9):
            if (self.cells[i].value == 1):
                values[i] = 'o'
            elif (self.cells[i].value == 2):
                values[i] = 'x'

        print(f"{values[0]}|{values[1]}|{values[2]} 1 2 3")
        print(f"{values[3]}|{values[4]}|{values[5]} 4 5 6")
        print(f"{values[6]}|{values[7]}|{values[8]} 7 8 9")
    def visitCell(self, cellcoord, playerNumber):
        if(self.cells[cellcoord].value == 0):
            self.cells[cellcoord].makeVisited(playerNumber)
    def allCellAreNotVisited(self):
        for cell in self.cells:
            if(cell.value == 0):
                return True
        return False
    def winCheck(self, playerNumber):
        if (self.cells[0].value==playerNumber) and (self.cells[4].value==playerNumber) and (self.cells[8].value==playerNumber):
            return True
        elif (self.cells[2].value==playerNumber) and (self.cells[4].value==playerNumber) and (self.cells[6].value==playerNumber):
            return True
        elif (self.cells[0].value==playerNumber) and (self.cells[3].value==playerNumber) and (self.cells[6].value==playerNumber):
            return True
        elif (self.cells[1].value == playerNumber) and (self.cells[4].value == playerNumber) and (self.cells[7].value == playerNumber):
            return True
        elif (self.cells[2].value==playerNumber) and (self.cells[5].value==playerNumber) and (self.cells[8].value==playerNumber):
            return True
        elif (self.cells[0].value == playerNumber) and (self.cells[1].value == playerNumber) and (self.cells[2].value == playerNumber):
            return True
        elif (self.cells[3].value == playerNumber) and (self.cells[4].value == playerNumber) and (self.cells[5].value == playerNumber):
            return True
        elif (self.cells[6].value == playerNumber) and (self.cells[7].value == playerNumber) and (self.cells[8].value == playerNumber):
            return True
        else:
            return False
    def getUnVisitedCells(self):
        for cell in self.cells:
            if cell.value == 0:
                return cell.coord

board = Board()
whatGame = int(input('Do you wanna play with bot(1) or 2 players(2)'))
if(whatGame == 1):
    playerFirst = Player('zhamilka', 1)
    playerSecond = Player('alexa', 2)
    board.showCells()
    while board.allCellAreNotVisited():
        firstPlayerMove = int(input("Type your cell from 1 to 9 Zha"))
        board.visitCell(firstPlayerMove-1, playerFirst.number)
        if(board.winCheck(playerFirst.number)):
            print(f"{playerFirst.name} win!")
            break
        board.showCells()
        secondPlayerMove = board.getUnVisitedCells()
        board.visitCell(secondPlayerMove, playerSecond.number)
        if (board.winCheck(playerSecond.number)):
            print(f"{playerSecond.name} win!")
            break
        board.showCells()
elif(whatGame == 2):
    playerFirst = Player('zhamilka', 1)
    playerSecond = Player('alex', 2)
    board.showCells()
    while board.allCellAreNotVisited():
        firstPlayerMove = int(input("Type your cell from 1 to 9 Zha"))
        board.visitCell(firstPlayerMove-1, playerFirst.number)
        if(board.winCheck(playerFirst.number)):
            print(f"{playerFirst.name} win!")
            break
        board.showCells()
        secondPlayerMove = int(input("Type your cell from 1 to 9 Alex"))
        board.visitCell(secondPlayerMove-1, playerSecond.number)
        if (board.winCheck(playerSecond.number)):
            print(f"{playerSecond.name} win!")
            break
        board.showCells()

