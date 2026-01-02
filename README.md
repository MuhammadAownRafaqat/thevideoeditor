# Simple Video Trimmer

A very simple video trimming app. Watch this video about the details of this project and how to run it: https://youtu.be/MWe9BlMGTxE

## Tech Stack
- React (frontend)
- FastAPI (backend)
- FFmpeg (video processing)

## Features
- Upload a video
- Trim video from the end (keep first X seconds)
- See trimmed video in outputs folder

## Setup
```bash
# Requirements
# Make sure you have Python 3.10+, Node.js, and FFmpeg installed and in PATH

# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (in a new terminal)
cd frontend
npm install
npm start
