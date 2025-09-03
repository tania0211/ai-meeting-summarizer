# backend/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from faster_whisper import WhisperModel
from transformers import pipeline
import tempfile

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
whisper_model = WhisperModel("base")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_action_items(transcript: str):
    action_keywords = ["need to", "please", "should", "must", "let’s", "next step", "to do", "required"]
    sentences = transcript.split(".")
    return [s.strip() for s in sentences if any(k in s.lower() for k in action_keywords)]

@app.get("/")
def health_check():
    return {"status": "API running"}

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    segments, _ = whisper_model.transcribe(tmp_path)
    transcript = " ".join([s.text for s in segments])

    summary = summarizer(transcript, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    actions = extract_action_items(transcript)

    return {"transcript": transcript, "summary": summary, "action_items": actions}
