import speech_recognition as sr
from datetime import datetime
import os

def take_voice_note():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Speak your note... (say 'stop recording' to cancel)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")

        if "stop recording" in text.lower():
            print("❌ Recording cancelled.")
            return

        save_note(text)

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")

def save_note(text):
    now = datetime.now()
    filename = f"note_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    directory = "notes"

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as file:
        file.write(text)

    print(f"✅ Note saved as {filepath}")

if __name__ == "__main__":
    take_voice_note()
