import os

def count_words_in_file(file_name, word_count):
    file = open(file_name, 'r')
    data = file.read()
    words = data.split()
    clean_words = []
    for word in words:
        clean_words.append(word.strip())
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

filelist = []
path = 'textfiles\\'
for file in os.listdir(path):
    if file.endswith('.txt'):
        filelist.append(file)
word_count = {}
for file in filelist:
    count_words_in_file(path + file, word_count)
sorted_word_count = {key:value for key,value in sorted(word_count.items(),key = lambda item: item[1], reverse=True)}
trimmed_word_count = {key:value for key,value in sorted_word_count.items() if value >= 3}
print(trimmed_word_count)