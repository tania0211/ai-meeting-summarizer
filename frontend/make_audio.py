import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Meeting-style text
meeting_text = """
Hello everyone, thanks for joining today’s meeting. 
We need to finalize the project timeline. 
The frontend team should finish the UI by next Monday. 
The backend team must integrate the APIs by the end of this month. 
Please don’t forget to send your weekly reports. 
Next step is deployment testing. 
Thank you all.
"""

# Save audio as MP3
engine.save_to_file(meeting_text, "sample_meeting.mp3")
engine.runAndWait()

print("✅ Sample audio created: sample_meeting.mp3")
