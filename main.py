from typing import Optional
from fastapi import FastAPI
import os
import datetime
import random

# Initialize the FastAPI application
app = FastAPI(
    title="OCI DevOps Demo API",
    description="A fun and engaging FastAPI application for OCI DevOps demos!",
    version="1.0.0"
)

# Simulate a request counter (for demo purposes)
requests_served_count = 0

# List of fun facts or demo tips
FUN_FACTS = [
    "Did you know serverless functions scale automatically? ✨",
    "This API is powered by FastAPI and OCI Functions! 🚀",
    "DevOps makes deployment a breeze! 💨",
    "Keep calm and code on! 💻",
    "Your feedback helps us grow! 🌱",
    "Exploring the cloud, one function at a time! ☁️"
]

@app.get("/")
def read_root():
    """
    Root endpoint providing a fun welcome message, version, namespace,
    current server time, and a random fun fact.
    """
    global requests_served_count
    requests_served_count += 1

    # Get version from environment or default
    version = os.getenv('APP_VERSION', default='1.0.0')
    # Get namespace from environment or default
    namespace = os.getenv('POD_NAMESPACE', default='demo-namespace')
    # Get current server time
    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

    return {
        "message": "Hello, Cloud Explorer! Welcome to your OCI DevOps adventure! 🌟",
        "version": version,
        "namespace": namespace,
        "server_time_utc": current_time,
        "fun_fact": random.choice(FUN_FACTS),
        "requests_served_since_startup": requests_served_count
    }

@app.get("/greet/{name}")
def greet_user(name: str):
    """
    Endpoint to greet a user by name.
    """
    global requests_served_count
    requests_served_count += 1

    return {
        "message": f"Hey there, {name}! It's awesome to see you! 👋",
        "requests_served_since_startup": requests_served_count
    }

@app.get("/status")
def get_status():
    """
    Health check endpoint providing application status and simulated metrics.
    """
    global requests_served_count
    requests_served_count += 1

    version = os.getenv('APP_VERSION', default='1.0.0')
    namespace = os.getenv('POD_NAMESPACE', default='demo-namespace')
    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

    return {
        "status": "UP",
        "service_name": "OCI DevOps Health Checker",
        "version": version,
        "namespace": namespace,
        "last_checked_at_utc": current_time,
        "requests_processed": requests_served_count,
        "health_details": {
            "database_connection": "OK",
            "external_api_reachability": "OK"
        }
    }

# Example of how to run this locally for testing:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)