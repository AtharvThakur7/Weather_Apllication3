import logging as log
import pandas as pd
log.basicConfig(filename="Weather_App.log" , level=log.INFO , format='%(asctime)s %(levelname)s %(message)s')
from flask import Flask, request, render_template, url_for
import requests

app = Flask(__name__, static_folder='static' , template_folder='templates')

# route to the Homepage
@app.route('/')
def homepage():
    try :
        return render_template("index.html")
    except Exception as e :
        log.error(e)

@app.route('/weatherapp', methods=['POST', 'GET'])
def Get_Weather_Data():
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        param = {
            'q': request.form.get('city'),
            'units': 'metric',
            'appid': '582d7c21a2eb650409ce81a274fc8b9c'
        }
        result = requests.get(url, params=param)
        data = result.json()
        frame = pd.DataFrame(result.json())

        return frame
    except Exception as e :
        log.error(e)

if __name__ == "__main__":
    try :
        app.run(host='0.0.0.0' ,port = 5002)
    except Exception as e :
        log.error(e)    
