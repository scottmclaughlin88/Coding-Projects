

#Open a file and count occurrances of specified words, such as 'technical', 'computer', 'usb'


#Open the file and read contents
#Loop through the document to find each


def open_legal_file(filename):
    words = []
    file = open(filename, 'r', encoding='UTF-8')
    words = file.read()
    return words.split()


def word_analysis(words,words_to_find):
    occurances = {}
    for word in words:
        for search_word in words_to_find:
            if word == search_word:
                if word not in occurances:
                    occurances[word] = 1
                else:
                    occurances[word] += 1
    return occurances

words = open_legal_file('legal1.txt')
words_to_find = ['technical','computer','usb','federal']
result = word_analysis(words,words_to_find)
print(result)