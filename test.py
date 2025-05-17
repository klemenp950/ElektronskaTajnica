import whisper

model = whisper.load_model("turbo")  # lahko tudi "base", "small", "large"
result = model.transcribe("test.mp3", language="en")
print(result["text"])
