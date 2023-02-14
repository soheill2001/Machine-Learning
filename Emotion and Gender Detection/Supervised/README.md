# Voice Emotion Recognition
This is a Python code that extracts audio features from a dataset of audio recordings, and trains machine learning models to recognize the emotion expressed in those recordings.

## Dataset
The dataset used in this project is in the CSV format and contains information on audio recordings including the filename, gender, text ID, and the emotion expressed in the audio.

## Requirements
'''
Python 3.x
librosa
numpy
pandas
scikit-learn
'''
## Installation
Clone this repository to your local machine.
Install the required packages with pip install -r requirements.txt.
Usage
Place your audio files in a directory of your choice and set the VOICE_PATH variable to the path of that directory.
Set the DATA_PATH variable to the path of your CSV file.
Run the code.
The code will extract audio features from the files in the specified directory, match them to the corresponding labels in the CSV file, and shuffle the data before training and testing the machine learning models.