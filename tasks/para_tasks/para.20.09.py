import random
lives = 3
true_answers = 0
while True:
    first = random.randint(0, 100)
    second = random.randint(0,100)
    sign = random.randint(1,4)
    if sign==1:
        answer = input(f"{first} + {second} =")
    elif sign==2:
        answer = input(f"{first} - {second} =")
    elif sign==3:
        answer = input(f"{first} * {second} =")
    else:
        answer = input(f"{first} / {second} =")
    if answer.isdigit():
        answer = int(answer)
        if sign == 1:
            if(answer==(first + second)):
                print('You win')
                true_answers += 1
            else:
                print('You lose')
                lives = lives - 1
        elif sign == 2:
            if (answer == (first - second)):
                print('You win')
                true_answers += 1
            else:
                print('You lose')
                lives = lives - 1
        elif sign == 3:
            if (answer == (first * second)):
                print('You win')
                true_answers += 1
            else:
                print('You lose')
                lives = lives - 1
        else:
            if (answer == (first / second)):
                print('You win')
                true_answers += 1
            else:
                print('You lose')
                lives = lives -1
    else:
        print('введите число')
        lives = lives - 1
        continue
    if(lives == 0):
        print(f"True: {true_answers}")
        break