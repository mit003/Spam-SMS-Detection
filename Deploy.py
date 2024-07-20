import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

from string import punctuation
from nltk.stem.porter import PorterStemmer 
ps = PorterStemmer()


def tranform_text(text):
    text = text.lower() #convert upper to lower charechters
    text = nltk.word_tokenize(text) # splite words

    # remove spacial char
    y=[]
    for i in text:
        if i.isalnum(): # isalnum () method is used to check whether the string consists of alphanumeric characters.
            y.append(i)

    # Remove Stop words
    text = y[:] # create clone of y (we can copy y)
    y.clear() 

    for i in text:
        if i not in stopwords.words('english') and i not in punctuation:
            y.append(i)

    #in nltk.stem.porter import PorterStemmer :: remove similer words and convert in to one word (stamming)
    #Example = [loved, loving, love, loves] == "love"
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")
input_sms = st.text_input("Enter the msg....")

if st.button('Predict'):
    ## Preprocess
    tranform_sms = tranform_text(input_sms)

    ## Vectorize
    vector_input = tfidf.transform([tranform_sms])

    ## Predict
    result = model.predict(vector_input)[0]

    ## Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

else:
    st.text("Enter txt")