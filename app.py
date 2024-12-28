# import logging as log
# import pandas as pd
# log.basicConfig(filename="Weather_App.log" , level=log.INFO , format='%(asctime)s %(levelname)s %(message)s')
# from flask import Flask, request, render_template, url_for
# import requests

# app = Flask(__name__, static_folder='static' , template_folder='templates')

# # route to the Homepage
# @app.route('/')
# def homepage():
#     try :
#         return render_template("index.html")
#     except Exception as e :
#         log.error(e)

# @app.route('/weatherapp', methods=['POST', 'GET'])
# def Get_Weather_Data():
#     try:
#         url = "https://api.openweathermap.org/data/2.5/weather"
#         param = {
#             'q': request.form.get('city'),
#             'units': 'metric',
#             'appid': '582d7c21a2eb650409ce81a274fc8b9c'
#         }
#         result = requests.get(url, params=param)
#         data = result.json()
#         # frame = pd.DataFrame(result.json())
#         # html_table = frame.to_html(index=False)
#         df = pd.read_json(data)
#         return df
#         # return data
#     except Exception as e :
#         log.error(e)

# if __name__ == "__main__":
#     try :
#         app.run(host='0.0.0.0' , port = 5001, debug=True)
#     except Exception as e :
#         log.error(e)    



#change 2 
# import logging as log
# import pandas as pd
# from flask import Flask, request, render_template, url_for
# import requests

# # Configure logging
# log.basicConfig(filename="Weather_App.log", level=log.INFO, format='%(asctime)s %(levelname)s %(message)s')

# # Initialize Flask app
# app = Flask(__name__, static_folder='static', template_folder='templates')

# # Route to the Homepage
# @app.route('/')
# def homepage():
#     try:
#         return render_template("index.html")
#     except Exception as e:
#         log.error(e)

# # Route to fetch and display weather data
# @app.route('/weatherapp', methods=['POST', 'GET'])
# def Get_Weather_Data():
#     try:
#         url = "https://api.openweathermap.org/data/2.5/weather"
#         param = {
#             'q': request.form.get('city'),
#             'units': 'metric',
#             'appid': '582d7c21a2eb650409ce81a274fc8b9c'
#         }
#         result = requests.get(url, params=param)
#         data = result.json()
        
#         # Convert JSON data to a DataFrame
#         df = pd.json_normalize(data)
        
#         # Render the DataFrame as an HTML table
#         html_table = df.to_html(index=False, classes='table table-striped')
        
#         # Pass the table to the template
#         return render_template("index.html", table=html_table)
#     except Exception as e:
#         log.error(e)
#         return "An error occurred. Please check the logs."

# if __name__ == "__main__":
#     try:
#         app.run(host='0.0.0.0', port=5001, debug=True)
#     except Exception as e:
#         log.error(e)












import logging as log
import pandas as pd
from flask import Flask, request, render_template, url_for
import requests

# Configure logging
log.basicConfig(filename="Weather_App.log", level=log.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Route to the Homepage
@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        log.error(e)

@app.route('/weatherapp', methods=['POST', 'GET'])
def Get_Weather_Data():
    try:
        # API call
        url = "https://api.openweathermap.org/data/2.5/weather"
        param = {
            'q': request.form.get('city'),
            'units': 'metric',
            'appid': '582d7c21a2eb650409ce81a274fc8b9c'
        }
        result = requests.get(url, params=param)
        data = result.json()

        # Normalize main JSON data
        df_main = pd.json_normalize(data)
        
        # Normalize the 'weather' column separately and merge back
        if 'weather' in data:
            weather_data = pd.json_normalize(data['weather'])  # Extract weather details
            weather_data.columns = [f'weather.{col}' for col in weather_data.columns]  # Prefix column names
            df_main = pd.concat([df_main, weather_data], axis=1)  # Merge the weather details

        # Drop nested columns you no longer need
        df_main.drop(columns=['weather'], errors='ignore', inplace=True)

        # Convert the DataFrame to an HTML table
        html_table = df_main.to_html(index=False, classes='table table-striped')

        # Render the table in the template
        return render_template("index.html", table=html_table)
    except Exception as e:
        log.error(e)
        return "An error occurred. Please check the logs."

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    except Exception as e:
        log.error(e)    

