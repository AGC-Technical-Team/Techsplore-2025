# Session 4: Docker Basics - Cultural Greetings App 🐳

## What We're Learning
How to put a simple Python app inside a **Docker container** - think of it like a magical box that runs the same way everywhere!

## 🎯 What is Docker? (Super Simple!)

**Docker** is like a **shipping container** for your code:
- Your app runs the same on any computer
- No more "it works on my machine" problems
- Easy to share and deploy

**Container** = Your app + everything it needs to run, all packaged together

## 📁 What's in This Folder?

```
Session 4/
├── app.py          # Our simple Python script
├── Dockerfile      # Instructions to build our container
└── README.md       # This guide!
```

## 🚀 Quick Start with Play with Docker

### Step 1: Go to Play with Docker
Visit: **https://labs.play-with-docker.com/**
- Click "Login" (use Docker Hub, GitHub, or create account)
- Click "Start" to get your playground
- Click "ADD NEW INSTANCE" to get a terminal

### Step 2: Upload Our Files
In the Play with Docker terminal, create our files:

```bash
# Create app.py
cat > app.py << 'EOF'
#!/usr/bin/env python3
# Super Simple Cultural Greetings - Perfect for Docker!

import time
import random

# Cultural greetings from around the world
greetings = [
    "Hello! (English)",
    "¡Hola! (Spanish)", 
    "Bonjour! (French)",
    "مرحبا (Arabic)",
    "你好 (Chinese)",
    "こんにちは (Japanese)",
    "नमस्ते (Hindi)",
    "Hujambo! (Swahili)"
]

print("🌍 Welcome to Cultural Greetings!")
print("This simple Python app is running inside Docker! 🐳")
print("="*50)

# Keep the container running and show greetings
while True:
    greeting = random.choice(greetings)
    print(f"Random greeting: {greeting}")
    time.sleep(5)  # Wait 5 seconds between greetings
EOF
```

```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
# Use Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy our simple Python script
COPY app.py .

# Run the Python script
CMD ["python", "app.py"]
EOF
```

### Step 3: Build Your Docker Image
```bash
# Build the container image
docker build -t cultural-greetings .

# Check if it was created
docker images
```

### Step 4: Run Your Container
```bash
# Run the container
docker run cultural-greetings
```

You should see greetings appearing every 5 seconds! 🎉

### Step 5: Stop the Container
Press `Ctrl+C` to stop it.

## 🔍 Understanding Each Part

### The Python Script (`app.py`)
```python
# Just a simple script that:
# 1. Shows cultural greetings
# 2. Runs forever (perfect for containers)
# 3. Uses only built-in Python (no extra dependencies)
```

### The Dockerfile
```dockerfile
FROM python:3.11-slim     # Start with Python installed
WORKDIR /app              # Create /app folder inside container
COPY app.py .             # Copy our script into container
CMD ["python", "app.py"]  # Run our script when container starts
```

## 🎮 Try These Docker Commands

### Basic Commands
```bash
# List all images on your system
docker images

# List running containers
docker ps

# List all containers (running + stopped)
docker ps -a

# Run container in background
docker run -d cultural-greetings

# Stop a running container
docker stop <container-id>

# Remove an image
docker rmi cultural-greetings
```

### Fun Experiments
```bash
# Run multiple containers at the same time!
docker run -d cultural-greetings
docker run -d cultural-greetings
docker run -d cultural-greetings

# See all your containers
docker ps

# Stop all containers
docker stop $(docker ps -q)
```

## 🤔 Cool Questions to Think About

1. **"What if I don't have Python installed on my computer?"**
   - Docker containers include Python! The app runs anyway.

2. **"What if I want to run this on Windows, Mac, and Linux?"**
   - Same container works everywhere! That's Docker magic.

3. **"What if I want to share this with a friend?"**
   - Just share the Dockerfile! They can build the same container.

## 🎪 Demo Ideas

### Show Docker Magic:
1. **Build the image** - show it appears in `docker images`
2. **Run the container** - show greetings appearing
3. **Run multiple containers** - show several running at once
4. **Stop everything** - show containers stopping

### Compare Regular vs Docker:
1. **Without Docker**: "You need to install Python, download script, run it"
2. **With Docker**: "Just run `docker run cultural-greetings`"

## 🚀 What's Next?

Once you understand this basic container, you can:
- ✅ Put any Python app in Docker
- ✅ Deploy to cloud services (AWS, Google Cloud, Azure)
- ✅ Scale your app to handle millions of users
- ✅ Update your app with zero downtime

## 🆘 Common Issues

### "Command not found: docker"
- You're probably not using Play with Docker
- Docker comes pre-installed in the playground!

### "Permission denied"
- In Play with Docker, you have full Docker access
- On your own computer, you might need `sudo docker`

### Container keeps stopping
- That's normal! Our script runs forever, but you can stop with Ctrl+C

## 🎓 Key Docker Concepts You've Learned

1. **Image** = Blueprint for containers (like a recipe)
2. **Container** = Running instance of an image (like a cooked meal)
3. **Dockerfile** = Instructions to build an image (like recipe steps)
4. **Build** = Create an image from Dockerfile
5. **Run** = Start a container from an image

---

**Congratulations!** 🎉 You've successfully containerized your first application!

**Next:** Try modifying `app.py` to add your own cultural greeting, rebuild the image, and run the new container!

---

## 🔗 Useful Links

- **Play with Docker**: https://labs.play-with-docker.com/
- **Docker Documentation**: https://docs.docker.com/
- **Docker Hub** (find pre-built images): https://hub.docker.com/
