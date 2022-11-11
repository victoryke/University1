from random import randint


def monty_hall(iterations):
    stay = 0
    change = 0
    for i in range(0, iterations):
        choose = randint(1, 3)
        car = randint(1, 3)
        if choose == car:
            stay += 1
        else:
            change += 1
    result = str([stay / iterations * 100, change / iterations * 100])
    return result
