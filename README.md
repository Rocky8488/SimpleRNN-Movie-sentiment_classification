IMDB Movie Review Sentiment Analysis
This project is a simple sentiment analysis model that classifies movie reviews as either positive or negative. The model is built using a Recurrent Neural Network (RNN) with TensorFlow and Keras, and a web application is created with Streamlit to provide an interactive user interface.

Key Components
1. Model Training
The SimpleRNN.ipynb Jupyter Notebook details the process of training the sentiment analysis model. The notebook includes the following steps:

Data Loading: Using the built-in IMDB dataset from Keras, which contains 50,000 movie reviews.

Data Preprocessing: Tokenizing the text data and padding sequences to a fixed length.

Model Architecture: A sequential model is built with three layers:

An Embedding layer to convert word indices into dense vectors.

A SimpleRNN layer to process the sequence data.

A Dense layer with a sigmoid activation function for binary classification (positive/negative).

Training and Saving: The model is compiled and trained on the dataset, and the trained model is saved in simple_rnn_imdb.h5 format.

2. Streamlit Application
The app.py script contains the code for the web application. It loads the pre-trained model and provides a text area for users to input a movie review. Upon clicking the "Classify" button, the application preprocesses the input text and uses the model to predict the sentiment. The result, including the sentiment label and the confidence score, is then displayed to the user.

Files in the Repository
app.py: The Streamlit application script.

SimpleRNN.ipynb: The Jupyter Notebook for training the RNN model.

prediction.ipynb: A Jupyter Notebook that likely contains code for making predictions using the trained model.

simple_rnn_imdb.h5: The pre-trained Keras model file.

Setup and Installation
To run this project, you will need to have Python installed. It is recommended to use a virtual environment.

Clone the repository:

git clone <your-repo-url>
cd <your-repo-name>

Install the required libraries:
The Streamlit app and the training notebook depend on a few key libraries. You can install them using pip:

pip install tensorflow numpy streamlit

Run the Streamlit application:
To start the interactive web app, run the following command in your terminal:

streamlit run app.py

This will open a new tab in your web browser with the application running.

Usage
Navigate to the Streamlit app in your web browser.

Enter a movie review into the text area.

Click the "Classify" button to see the predicted sentiment (Positive or Negative) and the associated confidence score.

Enjoy!
