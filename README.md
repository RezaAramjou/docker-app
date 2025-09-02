# Demo Docker Application

This is a simple Python Flask application packaged in a Docker container. It serves a "Hello" message on the root URL and a health check on the `/health` endpoint.

---

## ## Prerequisites

* Docker installed and running.

---

## ## Usage

### ### 1. Build the Docker Image

From the root of this repository, run the following command to build the Docker image. This will create an image tagged as `demo-app`.

**Important**: Replace `your-dockerhub-username` with your actual Docker Hub username.

```bash
docker build -t your-dockerhub-username/demo-app:latest ./app
```

### ### 2. Run the Container Locally

To test the container on your local machine, run:

```bash
docker run -p 3000:3000 your-dockerhub-username/demo-app:latest
```

You can then access the application at `http://localhost:3000` in your web browser or test the health check with `curl http://localhost:3000/health`.

### ### 3. Push the Image to a Registry

To make the image available for deployment on a server, you need to push it to a container registry like Docker Hub.

First, log in to your Docker Hub account from the terminal:
```bash
docker login
```

Then, push the image:
```bash
docker push your-dockerhub-username/demo-app:latest
```
