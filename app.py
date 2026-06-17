from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from u2net_model import remove_bg  # import dari file yang baru
from PIL import Image
import io
import base64

app = FastAPI(title="U-2-Net Background Removal API")

@app.get("/")
async def root():
    return {"status": "success", "message": "U-2-Net API is running. Use POST /remove-bg"}

@app.post("/remove-bg")
async def remove_background(image: UploadFile = File(...)):
    try:
        image_data = await image.read()
        img = Image.open(io.BytesIO(image_data)).convert("RGBA")
        result_img = remove_bg(img)

        buf = io.BytesIO()
        result_img.save(buf, format="PNG")
        result_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

        return JSONResponse({
            "status": "success",
            "message": "✅ Background removed",
            "result_base64": result_base64
        })
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)
