from flask import Flask, render_template
from navigationAlgoCode import *
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_path/<coords>')
def get_path(coords):
    #implement
    print("Sending coords: " + coords)
    points = []
    for coord in coords:
        points += coord
    return "OUTPUT POINTS HERE"

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
