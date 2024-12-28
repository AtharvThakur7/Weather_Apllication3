# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Set environment variables for Flask in production mode
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port 5001 (same as in your Flask app)
EXPOSE 5001

# Set the environment variable to avoid Python buffering
# ENV PYTHONUNBUFFERED 1

# Use Gunicorn to run the Flask application in production mode
CMD ["gunicorn", "-b", "0.0.0.0:5001", "app:app"]
