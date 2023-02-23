import csv

import random

import re


import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
with open('enews.csv', encoding="UTF-8") as file:
    reader = csv.reader(file)

    next(reader)

    readers = list(reader)
    print(random.choice(readers))
    # print(readers[1])

    # count = 0
    mylist = []
    for row in readers:
        title = (row[2] + "" + row[1])
        # print(title)
        mylist.append(title)
    print(mylist)
    filtered_text_list = []
    for text in mylist:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(' +', ' ', text)
        words = nltk.word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        filtered_text = " ".join(filtered_words)
        filtered_text_list.append(filtered_text)

    print(filtered_text_list)

    x = random.choice(filtered_text_list)
    print(x)
    # # Convert text to lowercase
    # text = x.lower()
    #
    # # Remove numbers and special symbols
    # text = re.sub(r'[^\w\s]', '', text)
    # text = re.sub(r'\d+', '', text)
    #
    # # Remove unnecessary spaces
    # text = re.sub(' +', ' ', text)
    #
    # # Split the text into words
    # words = nltk.word_tokenize(text)
    #
    # # Remove stop words
    # stop_words = set(stopwords.words('english'))
    # filtered_words = [word for word in words if word not in stop_words]
    #
    # # Join the filtered words to form a new text
    # filtered_text = " ".join(filtered_words)
    #
    # print(filtered_text)

# myList = [re.sub(r'[^a-zA-Z]',' ',string) for string in mylist]
        # print(myList)
        # x = random.choice(myList)
        #
        # # stopwords from NLTK
        # my_stopwords = nltk.corpus.stopwords.words('english')
        #
        # # add the new custom stopwords to my stopwords
        # my_stopwords.extend(x)
        # x = x.lower()
        # x = " ".join(x.split())










