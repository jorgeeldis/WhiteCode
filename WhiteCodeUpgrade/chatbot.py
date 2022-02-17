import random
import pickle
import json
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import nltk
import numpy as np
import tkinter
from tkinter import *

lemmatizer = WordNetLemmatizer()
model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):

    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#39FF14", font=("Courier", 12))

        res = chatbot_response(msg)
        ChatLog.insert(END, "WhiteCode: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("WhiteCode")
base.geometry("843x550")
base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="black", height="8",
               width="200", font="Courier",)

ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=("Courier", 12), text="Send", width="8", height="8",
                    bd=0, bg="black", activebackground="#3c9d9b", fg='#39FF14',
                    command=send)

EntryBox = Text(base, bd=0, bg="black", width="32",
                height="5", font="Courier", foreground="#39FF14")


scrollbar.place(x=825, y=6, height=430)
ChatLog.place(x=6, y=6, height=430, width=825)
EntryBox.place(x=6, y=450, height=90, width=710)
SendButton.place(x=730, y=450, height=90, width=95)

base.mainloop()
