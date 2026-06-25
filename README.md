# 🚀 CI/CD Pipeline – Cloud Run Deployment

---

## 📌 Project Overview

This repository implements a **CI/CD pipeline for application deployment on GCP** using Jenkins.

The pipeline automates:

- Build and test execution  
- Code coverage validation  
- Security scanning  
- Docker image creation  
- Deployment to Cloud Run  

---

## ⚙️ Technology Stack

| Layer | Tools |
|------|------|
| CI/CD | Jenkins |
| Containerization | Docker |
| Registry | Artifact Registry |
| Deployment | Cloud Run |
| Security | Trivy |
| Language | Application Code |

---

## 🔄 CI/CD Workflow

1. Developer pushes code to GitHub  
2. Jenkins pipeline is triggered  
3. Application is built  
4. Unit tests executed  
5. Code coverage generated  
6. Security scan using Trivy  
7. Docker image created  
8. Image pushed to Artifact Registry  
9. Application deployed to Cloud Run  

---

## 🚀 Pipeline Commands

```bash
# Build Docker image
docker build -t <image-name> .

# Push to Artifact Registry
docker push <image-name>

# Deploy to Cloud Run
gcloud run deploy <service-name> \
  --image=<image-name> \
  --region=asia-south1 \
  --platform=managed \
  --allow-unauthenticated

# Verify deployment
gcloud run services list
``
---

## 🛡 Security

Security is implemented using image scanning in the CI/CD pipeline.

- Container images are scanned using Trivy  
- Ensures no High or Critical vulnerabilities  
- Secure image deployment to Cloud Run  

```bash
trivy image <image-name>
---

## 💰 Cost Optimization

- Cloud Run scales to zero when idle  
- Pay-per-request model reduces cost  
- No infrastructure maintenance required  
- Efficient resource utilization  

This ensures minimal cost during low traffic.

---

## 🧯 Troubleshooting

### Pipeline Failure
- Check Jenkins logs for errors  

### Build Issues
- Verify Dockerfile and dependencies  

### Deployment Issues
- Ensure correct image path  
- Check Cloud Run logs  

### Image Push Failure
- Validate registry permissions

---

## 🏁 Conclusion

This repository demonstrates a fully automated CI/CD pipeline for building, testing, and deploying applications on GCP.

Key benefits:

- Automated build, test, and deployment process  
- Improved code quality with coverage and security scanning  
- Fast and reliable deployments using Cloud Run  
- Cost-efficient serverless execution  

This solution ensures a scalable and production-ready CI/CD workflow.
