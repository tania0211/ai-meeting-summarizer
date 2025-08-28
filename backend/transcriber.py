from faster_whisper import WhisperModel

# Load Whisper model once at the start
model = WhisperModel("base")  # You can also try "small", "medium", "large" if you want better accuracy

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes the given audio file and returns the full transcript as text.
    """
    segments, _ = model.transcribe(audio_path)

    # Combine all segments into one full transcript
    transcript = " ".join([segment.text for segment in segments])
    return transcript
 
