# Flask Kubernetes DevOps Project

Production-style DevOps project demonstrating containerization, CI/CD automation, Kubernetes orchestration, and Helm-based deployments.

---

## Architecture

GitHub → GitHub Actions → Docker Hub → Kubernetes → Helm → Running Pods

Workflow:

1. Developer pushes code to GitHub
2. GitHub Actions builds Docker image
3. Image is pushed to Docker Hub
4. Kubernetes pulls the image
5. Helm deploys the application
6. Pods run inside the Kubernetes cluster

---

## Tech Stack

Application
- Python Flask

Containerization
- Docker
- Docker Hub

Orchestration
- Kubernetes (Minikube)

Infrastructure as Code
- Kubernetes YAML
- Helm Charts

CI/CD
- GitHub Actions

Development Environment
- macOS
- VS Code

---

## Project Structure

flask-k8s-devops/
```

app/
app.py
requirements.txt

k8s/
deployment.yaml
service.yaml
configmap.yaml

flask-chart/
Chart.yaml
values.yaml
templates/

.github/workflows/
deploy.yml

Dockerfile
README.md

```

---

## Application Endpoints

| Endpoint | Description |
|--------|--------|
| `/` | Welcome message |
| `/health` | Health check used by Kubernetes probes |
| `/info` | Application metadata (version + environment) |

Example response:

```

{
"status": "healthy"
}

```

---

## Kubernetes Features Demonstrated

### Deployments
Runs multiple replicas of the Flask container.

### Liveness Probe
Ensures containers are automatically restarted if unhealthy.

### Readiness Probe
Ensures traffic is only sent to healthy pods.

### Services
Provides stable network access to pods.

### ConfigMap
Separates configuration from application code.

Environment variables used:

APP_VERSION  
APP_ENV

---

## CI/CD Pipeline

The project includes a GitHub Actions pipeline that automatically:

1. Builds a Docker image
2. Pushes the image to Docker Hub
3. Makes the image available for Kubernetes deployments

Pipeline trigger:

```

git push → GitHub Actions → Docker Build → Docker Hub Push

```

---

## Helm Deployment

Kubernetes manifests are packaged into a **Helm chart** for reusable deployments.

Helm allows:

- templated Kubernetes resources
- environment-specific configurations
- easier upgrades

Example commands:

Install chart

```

helm install flask-app ./flask-chart

```

Upgrade deployment

```

helm upgrade flask-app ./flask-chart

```

---

## Running the Project Locally

Start Minikube

```

minikube start

```

Deploy with Helm

```

helm install flask-app ./flask-chart

```

Access the service

```

minikube service flask-app-flask-chart

```

---

## DevOps Concepts Covered

- Docker containerization
- Kubernetes deployments
- Health probes
- ConfigMap configuration
- CI/CD automation
- Helm chart packaging
- Infrastructure as Code

---

## Author

Siddhesh Sampakal  
MSc Artificial Intelligence — University of Galway

GitHub:
https://github.com/sid-510

Docker Hub:
https://hub.docker.com/u/siddheeshhh
```