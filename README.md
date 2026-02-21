# AI Model Serving Platform

Production-ready AI model serving platform built with FastAPI, Docker, and Kubernetes-ready architecture.

This project demonstrates how to move from a trained ML model to a scalable, containerized, cloud-deployable inference service using real-world AI Platform Engineering principles.

---

## Problem Statement

Most machine learning projects stop at model training.

In real-world production systems, models must be:
- Packaged
- Served via API
- Containerized
- Monitored
- Scalable
- Infrastructure-managed

This project focuses on building the infrastructure layer around ML systems.

---

## Architecture

Model Training  
↓  
Model Serialization (joblib)  
↓  
FastAPI Inference Service  
↓  
Docker Container  
↓  
Kubernetes Deployment  

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Docker
- Kubernetes (deployment-ready structure)
- Terraform (infrastructure foundation)

---

## Project Structure

ai-model-serving-platform/
├── app/
├── docker/
├── k8s/
├── terraform/
└── README.md

---

## Run Locally

cd app  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python model.py  
uvicorn main:app --reload  

Verify health:

http://127.0.0.1:8000/health

---

## Containerized Deployment

docker build -t ai-model-serving -f docker/Dockerfile .  
docker run -p 8000:8000 ai-model-serving  

Verify:

http://localhost:8000/health

---

## API Endpoints

GET /health  
POST /predict  

---

## Engineering Focus

- Containerized model serving
- Stateless API design
- Health and reliability checks
- Kubernetes-ready deployment structure
- Infrastructure-first ML deployment mindset

---

## Author

Chandrasekhar Reddy Peechari  
AI Platform / DevOps Engineer
