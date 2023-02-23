from flask import Flask, escape, render_template, request, jsonify

import pickle

import pandas as pd
#
# from scipt import a
# b = a.y

import csv

import random

import re

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# from log import LogisticRegression

model = pickle.load(open("finalized_model.pkl", "rb"))

data = pd.read_csv("news.csv")

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

app = Flask(__name__)

@app.route("/get_random_number")
def get_random_number():
    return jsonify(random_text=random.choice(filtered_text_list))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/prediction', methods=["GET", "POST"])
def prediction():


    if request.method == "POST":
        news = request.form['news']
        print(news)
        predict = model.predict(vectorizer.transform([news]))[0]
        print(predict)
        if predict == 0:
            return render_template("prediction.html", prediction_text="The News is Real News📰")
        else :
            return render_template("prediction.html", prediction_text="The News is Fake News📰")
    else:
        return render_template("prediction.html")



if __name__ == '__main__':
    app.run(debug=True)
