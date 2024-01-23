import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from tkinter import Tk, Label, Text, Button

# Function to predict sentiment
def predict_sentiment(review):
    # Load the saved model
    loaded_model = tf.keras.models.load_model('G:\\vscode\\Projects\\sentiment_analysis\\movie_review_model.h5')

    # Tokenize and pad the input review
    tokenizer = Tokenizer(num_words=10000)
    tokenizer.fit_on_texts([review])
    sequence = tokenizer.texts_to_sequences([review])
    padded_review = pad_sequences(sequence, maxlen=300)

    # Predict sentiment
    prediction = loaded_model.predict(padded_review)

    return prediction[0][0]

# Function to get prediction and update label
def get_prediction():
    user_review = text_entry.get("1.0",'end-1c')
    prediction = predict_sentiment(user_review)
    print(prediction)
    
    result_label.config(text=f"Prediction: {'Positive' if prediction >= 0.75 else 'Negative'}")

# GUI using tkinter
root = Tk()
root.title("Movie Review Sentiment Analysis")

# Text entry for user review
text_entry = Text(root, height=5, width=40)
text_entry.pack()

# Button to get prediction
predict_button = Button(root, text="Predict", command=get_prediction)
predict_button.pack()

# Label to display result
result_label = Label(root, text="Prediction: ")
result_label.pack()

# Run the tkinter main loop
root.mainloop()