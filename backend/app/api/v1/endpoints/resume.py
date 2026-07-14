from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.resume_parser import extract_text_from_pdf

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "text": text,
    }
