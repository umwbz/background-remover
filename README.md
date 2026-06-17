# U-2-Net Background Removal API

A FastAPI-based background removal service powered by U-2-Net. This API automatically segments the foreground object and removes the image background, returning a transparent PNG image encoded in Base64 format.

## Features

* Automatic background removal
* U-2-Net deep learning segmentation model
* Transparent PNG output
* FastAPI REST API
* Base64 encoded response
* Supports PNG and JPG images

## Project Structure

```text
.
├── app.py
├── u2net_model.py
├── saved_models/
│   └── u2net.pth
├── U2Net/
│   ├── model.py
│   └── ...
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/u2net-background-removal-api.git
cd u2net-background-removal-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Required Packages

```text
fastapi
uvicorn
torch
torchvision
numpy
pillow
python-multipart
```

## Model Weights

Download the pretrained U-2-Net model and place it inside:

```text
saved_models/u2net.pth
```

## Run the API

Start the FastAPI server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

## API Endpoints

### Health Check

**GET /**

Response:

```json
{
  "status": "success",
  "message": "U-2-Net API is running. Use POST /remove-bg"
}
```

### Remove Background

**POST /remove-bg**

Parameters:

| Parameter | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| image     | File | Yes      | Input image |

#### Example Request

```bash
curl -X POST \
  "http://localhost:8000/remove-bg" \
  -F "image=@photo.jpg"
```

#### Example Response

```json
{
  "status": "success",
  "message": "✅ Background removed",
  "result_base64": "iVBORw0KGgoAAAANSUhEUg..."
}
```

## How It Works

1. Upload an image.
2. The image is preprocessed and resized.
3. U-2-Net predicts the foreground mask.
4. The mask is converted into an alpha channel.
5. The result is returned as a transparent PNG image.

## Technology Stack

* FastAPI
* PyTorch
* Torchvision
* U-2-Net
* NumPy
* Pillow

## Model

This project uses the U-2-Net architecture, a deep learning model specifically designed for salient object detection and background removal.

## Author

Sukma Wati

## License

This project is intended for educational, research, and portfolio purposes.
