FROM python:3.10-slim

# Install system deps
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 git curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Clone U-2-Net repo
RUN git clone https://github.com/xuebinqin/U-2-Net.git U2Net

# Download pretrained model
RUN mkdir saved_models && \
    curl -L -o saved_models/u2net.pth "https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy"

# Copy app code
COPY . .

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

