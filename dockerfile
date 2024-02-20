# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir mysql-connector-python

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for database configuration
ENV DB_USER=root \
    DB_PASSWORD=admin \
    DB_HOST=vamshisql \
    DB_NAME=vamshidb

# Run app.py when the container launches
CMD ["python", "demo.py"]
