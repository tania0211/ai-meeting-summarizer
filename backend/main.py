from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel
from transformers import pipeline
import tempfile

app = FastAPI()


whisper_model = WhisperModel("base")


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_action_items(transcript: str):
    action_keywords = ["need to", "please", "should", "must", "let’s", "next step", "to do", "required"]
    sentences = transcript.split(".")
    actions = [s.strip() for s in sentences if any(k in s.lower() for k in action_keywords)]
    return actions


@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    segments, _ = whisper_model.transcribe(tmp_path)
    transcript = " ".join([segment.text for segment in segments])

    summary_text = summarizer(transcript, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

    actions = extract_action_items(transcript)

    return {
        "transcript": transcript,
        "summary": summary_text,
        "action_items": actions
    }
