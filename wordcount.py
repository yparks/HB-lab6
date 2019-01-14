# put your code here.


def word_count(text_file):
    words = {}
    file = open(text_file) 
    for line in file:
        word_list = line.rstrip().split(" ")

        for word in word_list:
            words[word] = words.get(word, 0) + 1

    file.close()
    for word, fre in words.items():
        print(word, fre)
