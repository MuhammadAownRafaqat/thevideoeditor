from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import uuid
import os
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok= True)

@app.post("/trim")
async def trim_video(
    video: UploadFile = File(...),
    keep_seconds: int = Form(...)
):
    
    input_filename = f"{uuid.uuid4()}_{video.filename}"
    output_filename = f"trimmed_{input_filename}"

    input_path = os.path.join(UPLOAD_DIR, input_filename)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(input_path, "wb") as f:
        f.write(await video.read())

    ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"

    command = [
    ffmpeg_path,
    "-y",                  
    "-i", input_path,
    "-t", str(keep_seconds),
    "-c", "copy",
    output_path
    ]


    result = subprocess.run(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )

    print("FFMPEG STDOUT:", result.stdout)
    print("FFMPEG STDERR:", result.stderr)

    if result.returncode != 0:
        raise RuntimeError("FFmpeg failed")


    return FileResponse(
        output_path,
        media_type= "video/mp4",
        filename=output_filename
    )