def get_unique(text):
    unique_words_list = []
    words_list = text.split()
    for element in words_list:
        if (text.find(element)==text.rfind(element)):
            unique_words_list.append(element)
    return sorted(unique_words_list)

def read_file(filename):
    file = open(filename, encoding='utf-8')
    text = ""
    for line in file:
        text += line
    return get_unique(text.lower())

def save_file(filename, unique_words):
    file = open(filename, 'w', encoding='utf-8')
    file.write(f"Unique words counter: {len(unique_words)}\n")
    for element in unique_words:
        file.writelines(element + "\n")
    file.close()

save_file("output.txt", read_file("input.txt"))