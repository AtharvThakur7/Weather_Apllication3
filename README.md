# Weather App using Flask, Python, and OpenWeatherMap API ,Docker Containers and Render

This project is a simple Weather App built using Flask and the OpenWeatherMap API. The application allows users to input a city name and retrieve current weather information, such as temperature, humidity, and other related weather data in metric units.


# project Structure 


![alt image](https://github.com/AtharvThakur7/Weather_Apllication3/blob/596ebcad76a83eae9a9bae1e60d826e724f3e73d/Screenshot%202024-12-28%20234016.png)

## Features

- City Weather Search:

Users can input the name of any city to get its current weather data.
- Current Weather Data:

- Displays key weather metrics such as:
Temperature (°C)

Feels Like Temperature (°C)

Humidity (%)

Wind Speed (m/s)

Weather Conditions (clear, cloudy, etc.)

Pressure (hPa)

Visibility (m)

Sunrise & Sunset Times

- Responsive UI:
The app's UI adjusts automatically for different screen sizes, making it easy to use on desktops, tablets, and mobile devices.

- Real-Time Data Fetching:
The app uses the OpenWeather API to fetch live weather data, ensuring that the information is up-to-date.

- Dockerized Application:
The app is containerized using Docker for consistent deployment across different environments.

- Production-Ready:
The app runs on Gunicorn in a production environment, making it scalable and robust.

- Error Handling:
The app handles errors such as invalid city names gracefully, displaying appropriate error messages.

- Deployed on Render:
The app is hosted on Render, providing a fast and reliable cloud platform for production deployment.

## Tech Stack

**Flask:** Python-based web framework for creating the app.

**Gunicorn:** A WSGI HTTP Server for running Flask in production.

**Requests:** For making HTTP requests to fetch weather data from the OpenWeather API.

**Pandas:** Used for handling and formatting the weather data 

**OpenWeather API:** Provides weather data from global cities.

**Docker:** Containerizes the application for consistent deployment across various environments.

**Render:** A platform for deploying web applications directly from Docker images.



 
