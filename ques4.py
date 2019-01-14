#program to print freq distribution of only nouns in a given file
import nltk
import pandas as pd

filename = input("Enter file name:")
dict = {}
words = []
tagged = []
with open(filename, 'r') as file:
    data = file.read()
    sentences = nltk.tokenize.sent_tokenize(data)
    for i in sentences:
        word = nltk.tokenize.word_tokenize(i)
        words.extend(word)
#get a tagged list of all the words
tagged = nltk.pos_tag(words)

#only add nouns to the freq distribution
for (word, pos) in tagged:
    if pos[0] == 'N':
        if not word in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word]+1
df = pd.DataFrame(dict, index=[0])
print(df)