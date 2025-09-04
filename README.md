# Secure Demo Docker Application

This is a simple Python Flask application packaged in a Docker container. It was created as part of a 30-day cybersecurity capstone project to demonstrate vulnerability remediation and secure coding practices.

The application includes fixes for common vulnerabilities like SQL Injection and Cross-Site Scripting (XSS) by implementing input sanitization (`bleach`) and adding security headers.

---

## ## How to Use

### ### 1. Local Development Setup

For local development, it is recommended to use a Python virtual environment.

```bash
# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt
```

### ### 2. Build the Docker Image

From the root of this repository, run the following command to build the Docker image.

**Note**: Replace `your-dockerhub-username` with your actual Docker Hub username.

```bash
docker build -t your-dockerhub-username/demo-app:latest ./app
```

### ### 3. Run the Container Locally

To test the container on your local machine, run:

```bash
docker run -p 3000:3000 your-dockerhub-username/demo-app:latest
```
The application will be available at `http://localhost:3000`. You can test the health check endpoint with `curl http://localhost:3000/health`.

### ### 4. Push the Image to a Registry

To make the image available for deployment, push it to a container registry like Docker Hub.

```bash
# First, log in to your account
docker login

# Then, push the image
docker push your-dockerhub-username/demo-app:latest
```
