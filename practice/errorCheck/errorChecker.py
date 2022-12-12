def get_list(filename = "error_journal.txt"):
    try:
        file = open(filename, "r")
        iterator = int(file.readline())
        numbers = []
        for i in range(0,iterator):
            numbers.append(int(file.readline().replace('\n', '')))
        print(numbers)

    except FileNotFoundError:
        print('File doesnt exist')
    except ValueError:
        print('File is empty or have uncorrect iterations counter')
    finally:
        try:
            file.close()
        except UnboundLocalError:
            print()
