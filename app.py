import spacy
from spacy import displacy
import pickle
import warnings
from flask import Flask, request, render_template,redirect
from flask_misaka import Misaka



warnings.warn("first example of warning!", DeprecationWarning)

import os

nlp = pickle.load(open('nlp.pkl', 'rb'))

app = Flask(__name__)
Misaka(app)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['GET', 'POST'])
def extract():
    if request.method=='POST':
        txt = request.form['ner_text']
        doc=nlp(txt)
        result = displacy.render(doc,style="ent")

    return render_template('result.html',result=result)






if __name__ == "__main__":
    app.run(debug=True)
