from flask import Flask
from flask_cors import CORS
from data import *

app = Flask(__name__)
CORS(app)

@app.route('/api/country/<iso_code>')
def index(iso_code):
    return get_data(iso_code)

@app.route('/api/top/total-values')
def set_top_ten():
    return get_top_ten()

@app.route('/api/count/country-vaccine')
def set_count_of_vaccines_in_countries():
    return get_count_of_vaccines_in_countries()

#for testing the application
if __name__ == '__main__': 
    app.run(host='0.0.0.0')