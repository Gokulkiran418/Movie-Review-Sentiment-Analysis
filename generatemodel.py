import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from tkinter import Tk, Label, Text, Button

# Load IMDB movie review dataset
imdb = tf.keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# Pad the sequences to have consistent length
train_data = pad_sequences(train_data, maxlen=300)
test_data = pad_sequences(test_data, maxlen=300)

# Create the model
model = Sequential()
model.add(Embedding(10000, 128, input_length=300))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, train_labels, epochs=30, validation_data=(test_data, test_labels))

# Save the model
model.save('G:\\vscode\\Projects\\sentiment_analysis\\movie_review_model.h5')