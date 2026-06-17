# U-2-Net Background Removal API

A FastAPI-based background removal service powered by U-2-Net. This API automatically segments the foreground object and removes the image background, returning a transparent PNG image encoded in Base64 format.

---

## 🌐 Live API Endpoint (HuggingFace)

You can directly use the deployed API:

### 🔗 Remove Background Endpoint

POST https://umscorleonis-background-remover-space.hf.space/remove-bg

---

## 🚀 Features

- Automatic background removal
- U-2-Net deep learning segmentation model
- Transparent PNG output
- FastAPI REST API
- Base64 encoded response
- Supports PNG and JPG images

---

## 📦 Project Structure

.
├── .gitattributes
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
└── u2net_model.py

---

## ⚙️ Installation

### 📥 Clone Repository

git clone https://github.com/your-username/u2net-background-removal-api.git
cd u2net-background-removal-api

---

### 📌 Install Dependencies

pip install -r requirements.txt

---

## 📚 Required Packages

fastapi
uvicorn
torch
torchvision
numpy
pillow
python-multipart

---

## 📦 Model Weights

Download pretrained model:

saved_models/u2net.pth

---

## ▶️ Run API Locally

uvicorn app:app --host 0.0.0.0 --port 8000

API will be available at:

http://localhost:8000

---

## 🔌 API Endpoints

### ❤️ Health Check

GET /

Response:

{
  "status": "success",
  "message": "U-2-Net API is running. Use POST /remove-bg"
}

---

### 🎯 Remove Background

POST /remove-bg

| Parameter | Type | Required | Description |
|----------|------|----------|-------------|
| image    | File | Yes      | Input image |

---

## 📤 Example Request (Python)

import requests

url = "http://localhost:8000/remove-bg"

files = {
    "image": open("photo.jpg", "rb")
}

response = requests.post(url, files=files)
print(response.json())

---

## ☁️ HuggingFace API Usage

import requests

url = "https://umscorleonis-background-remover-space.hf.space/remove-bg"

files = {
    "image": open("photo.jpg", "rb")
}

response = requests.post(url, files=files)
print(response.json())

---

## 📥 Example Response

{
  "status": "success",
  "message": "✅ Background removed",
  "result_base64": "iVBORw0KGgoAAAANSUhEUg..."
}

---

## 🧠 How It Works

1. Upload image
2. Image preprocessing
3. U-2-Net predicts foreground mask
4. Mask converted to alpha channel
5. Output returned as transparent PNG

---

## 🛠 Technology Stack

- FastAPI
- PyTorch
- Torchvision
- U-2-Net
- NumPy
- Pillow

---

## 🤖 Model

U-2-Net is a deep learning model designed for salient object detection and background removal with high accuracy.

---

## 👩‍💻 Author

Sukma Wati

---

## 📄 License

This project is intended for educational, research, and portfolio purposes.
