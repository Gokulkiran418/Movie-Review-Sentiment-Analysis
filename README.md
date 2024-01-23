# Files
## generatemodel.py
Creates and saves the model.
model.save('G:\\vscode\\Projects\\sentiment_analysis\\movie_review_model.h5')

Change path to your desired path

## app.py
Runs a simple application that shows a textbox. You can type your own review.

loaded_model = tf.keras.models.load_model('G:\\vscode\\Projects\\sentiment_analysis\\movie_review_model.h5')

Replace file path with the path where you stored the model.
When you click predict, the program predicts whether the review is positive or negative.

## movie_review_model.h5
This is a sample model. Download this file and specify the its path in this line in app.py file.

loaded_model = tf.keras.models.load_model('G:\\vscode\\Projects\\sentiment_analysis\\movie_review_model.h5')

If you are using this model, there is no need to run the generatemodel.py file because it does the same thing, 
create a model.

# Prerequisites
pip install tkinter.

Install conda for easy installation of tensorflow and other packages
