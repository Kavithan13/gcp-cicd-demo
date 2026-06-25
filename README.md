# 🚀 CI/CD Pipeline – Cloud Run Deployment

---

## 📌 Overview

This repository implements a CI/CD pipeline for deploying an application to Google Cloud Run.

The pipeline automates build, testing, security scanning, containerization, and deployment.

---

## ⚙️ Tech Stack

- CI/CD: Jenkins
- Containerization: Docker
- Registry: Artifact Registry
- Deployment: Cloud Run
- Security: Trivy
- Language: Python / Node (your app)

---

## 🔄 CI/CD Workflow

1. Code push to GitHub
2. Jenkins pipeline triggers
3. Build application
4. Run unit tests
5. Generate code coverage
6. Perform security scan (Trivy)
7. Build Docker image
8. Push image to Artifact Registry
9. Deploy to Cloud Run

---

## 🧱 Architecture

``
