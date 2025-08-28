from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """
    Summarizes long meeting text using BART.
    """
    # Huggingface models have a token limit (~1024 words), so split long text
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""

    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summary += result[0]['summary_text'] + " "

    return summary.strip()
