from flask import Flask, request, render_template, url_for
import requests

app = Flask(__name__, static_folder='static' , template_folder='templates')

# route to the Homepage
@app.route('/page')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods=['POST', 'GET'])
def Get_Weather_Data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q': request.form.get('city'),
        'units': 'metric',
        'appid': '582d7c21a2eb650409ce81a274fc8b9c'
    }
    result = requests.get(url, params=param)
    data = result.json()
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
