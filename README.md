# Distributed ImageServer

Project Overview
This project consists of a frontend that interacts with users, a backend built with Python (Flask) to handle API calls, and a Google Cloud Storage bucket to store the data (pictures or videos). Additionally, Prometheus and Grafana are used for monitoring and visualizing metrics.

Key Components

1. Frontend:
   - Role: Provides the user interface for users to upload and download pictures or videos.
   - Technologies: HTML, CSS
2. Backend:
   - Role: Handles API requests from the frontend, generates signed URLs for secure uploads and downloads, and interacts with the Google Cloud Storage bucket.
   - Technologies: Python, Flask.
3. Google Cloud Storage:
   - Role: Stores the uploaded pictures or videos securely.
   - Technologies: Google Cloud Storage (GCS).
4. Deployment on Google Kubernetes

   - Engine (GKE)
     The Flask application is containerized using Docker and deployed on Google Kubernetes Engine (GKE). A Kubernetes deployment
     YAML file is used to define the deployment configuration, ensuring that the Flask application runs in a scalable and managed environment.

5. Monitoring:
   - Role: Provides monitoring and visualization of the application's performance and health.
   - Technologies: Prometheus, Grafana.
