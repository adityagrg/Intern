#program to compute freq distribution of words of a given file
import pandas as pd
import nltk

filename = input("Enter file name : ")

with open(filename, "r") as f:
    data = f.read()
    words = nltk.tokenize.word_tokenize(data)
    fd = nltk.FreqDist(words)
    final_df = pd.DataFrame(fd, index=[0])

print(final_df)