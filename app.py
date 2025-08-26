from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
import streamlit as st


word_index = imdb.get_word_index()
reversed_word_index = {value: key for key,value in word_index.items()}

model = load_model("simple_rnn_imdb.h5", compile=False)


#Helper function
#function to decode review
def decode_review(encoded_review):
    decoded_review = ' '.join([reversed_word_index.get(i-3,'?') for i in encoded_review])

#function to preproces user input
def preproces_text(text):
    words = text.lower().split()
    encoded_review = ([word_index.get(word,2) + 3 for word in words])
    padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review


st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a Movie Review to Classify it is a Positive or negative ")

user_input = st.text_area('Movie Review')

if st.button("classify"):
    preprocessed_input = preproces_text(user_input)

    #Make Prediction
    prediction = model.predict(preprocessed_input)

    sentiment = 'Positive' if prediction[0][0]>0.5 else 'Negative'

    st.write(f'sentiment: {sentiment}')
    st.write(f'score: {prediction[0][0]}')

else:
    st.write("please enter a movie review")
