import sys
import os

# Tambahkan folder U2Net ke path Python
sys.path.append(os.path.join(os.path.dirname(__file__), "U2Net"))

# Sekarang import model dari repo U2Net
from model import U2NET, U2NETP

import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# Load model
model_path = "./saved_models/u2net.pth"
try:
    net = U2NET(3, 1)
    net.load_state_dict(torch.load(model_path, map_location="cpu"))
except RuntimeError:
    print("⚠️ U2NET besar gagal — mencoba versi ringan U2NETP...")
    net = U2NETP(3, 1)
    net.load_state_dict(torch.load(model_path, map_location="cpu"))

net.eval()
print("✅ U-2-Net model berhasil dimuat!")

# Fungsi helper
def preprocess_image(img):
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    return transform(img).unsqueeze(0)

def predict_mask(net, img):
    with torch.no_grad():
        input_tensor = preprocess_image(img)
        d1, _, _, _, _, _, _ = net(input_tensor)
        pred = d1[:, 0, :, :]
        pred = (pred - pred.min()) / (pred.max() - pred.min())
        return pred.squeeze().cpu().numpy()

def remove_bg(input_img):
    img = input_img.convert("RGB")
    mask = predict_mask(net, img)
    mask_resized = Image.fromarray((mask * 255).astype(np.uint8)).resize(img.size)

    img_np = np.array(img)
    mask_np = np.array(mask_resized) / 255

    result = np.dstack((img_np, (mask_np * 255).astype(np.uint8)))
    return Image.fromarray(result)
