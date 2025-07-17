from fastapi import FastAPI
import os
import random
from datetime import datetime

app = FastAPI(title="Love Express", version="1.0.2")

# Fun messages with emojis
LOVE_MESSAGES = [
    "You're the kubectl to my cluster ❤️",
    "My heart pings your IP 💘",
    "Our connection has 0% packet loss 💞",
    "You're my favorite endpoint 😍",
    "I'm 200 OK when I'm with you 💖"
]

# Deployment facts for the /about route
DEPLOYMENT_FACTS = [
    "Kubernetes was named after a Greek helmsman",
    "The first container ship sailed in 1956",
    "Over 5.6 million developers use GitHub",
    "80% of enterprises use cloud-native tech",
    "The cloud weighs more than 1 million elephants! ☁️🐘"
]

@app.get("/", tags=["Love API"])
def send_love():
    """Send some DevOps love with Kubernetes context!"""
    return {
        "message": random.choice(LOVE_MESSAGES),
        "version": app.version,
        "namespace": os.getenv('POD_NAMESPACE', 'ns-red'),
        "timestamp": datetime.utcnow().isoformat(),
        "secret": "You're awesome! 😎",
        "emoji": random.choice(["💻", "🚀", "🐳", "🔑", "🎯", "🌈"])
    }

@app.get("/about", tags=["Info"])
def deployment_info():
    """Fun facts about deployments"""
    return {
        "cloud_provider": "OCI",
        "service": "DevOps",
        "fun_fact": random.choice(DEPLOYMENT_FACTS),
        "architecture": os.getenv('HOSTNAME', 'unknown-arch')
    }

@app.get("/health", tags=["Health Check"])
def health_check():
    """Always healthy with extra love!"""
    return {
        "status": "💚 Green",
        "uptime": "∞",
        "message": "System is overflowing with love!"
    }