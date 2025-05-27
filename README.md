# 🚀 CI/CD Flask Web App Project

This project demonstrates a complete CI/CD pipeline for a Python Flask web application using Jenkins, Docker, AWS, SonarQube, and Prometheus + Grafana for monitoring.

---

## 📦 Features

- Flask-based web application with Prometheus metrics
- Unit testing using `pytest`
- Docker containerization
- Jenkins CI/CD pipeline
  - Build
  - Test
  - Code Quality Analysis via SonarQube
  - Docker image push to Docker Hub
  - Deployment to AWS EC2
- Monitoring via Prometheus and Grafana

---

## 🏗️ Project Structure

```

myapp/
├── app.py                   # Main Flask app
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container definition
├── sonar-project.properties # SonarQube config
├── Jenkinsfile              # CI/CD pipeline definition
├── tests/
│   └── test\_app.py          # Unit tests
└── scripts/
└── deploy.sh            # Deployment script to AWS

````

---

## ⚙️ How to Run Locally

### Prerequisites

- Python 3.10+
- Docker
- Git

### Run the App

```bash
# Clone the repository
git clone https://github.com/yourusername/myapp.git
cd myapp

# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the app
python app.py
````

App will be available at `http://localhost:5000`.

### Run Tests

```bash
pytest tests/
```

---

## 🐳 Run with Docker

```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
```

---

## 🔐 CI/CD Pipeline (Jenkins)

Pipeline stages:

1. **Checkout Code** from GitHub
2. **Static Code Analysis** with SonarQube
3. **Run Unit Tests** with Pytest
4. **Build Docker Image**
5. **Push Image** to Docker Hub
6. **Deploy** to AWS EC2 instance

> Make sure you have credentials set up in Jenkins for Docker Hub and EC2 SSH access.

---

## ☁️ AWS Deployment

The deployment script connects to an EC2 instance via SSH and:

* Pulls the latest Docker image from Docker Hub
* Stops/removes existing container
* Runs the new container

You can configure EC2 IP and Docker Hub username in `scripts/deploy.sh`.

---

## 📊 Monitoring

### Prometheus

* Exposes metrics on `/metrics` endpoint using `prometheus_client`

### Grafana

* Connect Grafana to Prometheus and create dashboards for metrics like request count, memory usage, etc.

---

## 🧪 Code Quality with SonarQube

```bash
# Ensure sonar-project.properties is configured correctly
sonar-scanner
```

> Replace `sonar.login` token and `sonar.host.url` with your actual SonarQube settings.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

```
