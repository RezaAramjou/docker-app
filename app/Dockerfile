# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY server.py .

# Expose port 3000 to the outside world
EXPOSE 3000

# Command to run the application
CMD ["python", "server.py"]
