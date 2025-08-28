import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Text to simulate a meeting recording
meeting_text = """
Hello everyone, thanks for joining today’s meeting. 
We need to finalize the project timeline. The frontend team should finish the UI by next Monday. 
The backend team will integrate APIs by the end of this month. 
Also, please don’t forget to send your weekly progress reports. 
Let’s meet again next Friday to review updates. Thank you!
"""

# Save the speech to a file
output_file = "sample_meeting.wav"
engine.save_to_file(meeting_text, output_file)
engine.runAndWait()

print(f"Meeting audio saved as {output_file}")
