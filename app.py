from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_cors import CORS
from main import recommend_songs
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/data_cleaned.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_songs', methods=['POST'])
def suggest_plans():
    input_song = request.form['input_song']

    song_capital = input_song.title()
    
    comment, songs = recommend_songs(song_capital, data)
    # Render the output on an HTML page
    return render_template('songs.html', comment= comment, song = songs)

if __name__ == '__main__':
    app.run(debug=True)
