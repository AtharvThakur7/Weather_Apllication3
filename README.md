# Weather App using Flask, Python, and OpenWeatherMap API ,Docker Containers and Render

The Weather App provides real-time weather data for any city globally. Built with Flask and powered by the OpenWeather API, it displays key weather metrics like temperature, humidity, and wind speed. The app is Dockerized for easy deployment and is hosted on Render for reliable, scalable performance.


# project Structure 


![alt image](https://github.com/AtharvThakur7/Weather_Apllication3/blob/596ebcad76a83eae9a9bae1e60d826e724f3e73d/Screenshot%202024-12-28%20234016.png)


## Live Demo

You can try the live demo of the Weather App here:

https://weather-app-latest-jnq1.onrender.com/


## Features

- City Weather Search:

Users can input the name of any city to get its current weather data.
- Current Weather Data:

- Displays key weather metrics such as:
Temperature (°C)

Humidity (%)

Wind Speed (m/s)

Weather Conditions (clear, cloudy, etc.)

Pressure (hPa)

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


## Future Improvements:
Add Forecasting: Allow users to get a weather forecast for the next 7 days or 24 hours.


## Conclusion
This Weather App provides a simple and efficient way to check the current weather for any city globally. By leveraging the OpenWeather API, Flask, and Docker, the app is easy to deploy and scale, making it suitable for both personal and production use.

With its real-time weather data, user-friendly interface, and deployment on Render, the app is a great example of how to create and deploy a modern web application. Whether you're looking for a basic weather tool or an app to build upon, this project serves as a solid foundation for further enhancements and customizations.

Feel free to explore, test, and contribute to this project. If you have any questions, suggestions, or improvements, feel free to reach out!






 
