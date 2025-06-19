**#Minimal Flask App with Docker - Mini Project**

A lightweight containerized Python Flask app that returns “Hello, Docker!”.

**Project Structure :**

├── app.py              # Simple Flask API
├── requirements.txt    # Python dependencies
├── Dockerfile          # Instructions to build image
└── README.md

1.**Building the Image:**
  docker build -t flask-hello .

2.**Run the container:**
docker run -d -p 5000:5000 flask-hello

3.Visit: Open your browser: http://localhost:5000

Attached all the three files with the output screenshot.

**Learnings:**
1.Creating Docker images from Python apps
2.Using minimal base images
3.Port forwarding, container logs, and basic debugging

**Troubleshooting Commands:**
1. docker logs <container_id>
2. docker inspect <container_id>


**2. Run the Container with Environment Variable**

Updated docker2file, app2.py and output2 screenshot is attached
    docker run -d -p 5000:5000 -e USER_NAME=Kajal flask-app

    Now for output run below 02 links
    http://localhost:5000
    http://localhost:5000/about

    
**3. Start the App with Compose**

        docker-compose up --build -d
        docker-compose down
        Go to above links and check output




