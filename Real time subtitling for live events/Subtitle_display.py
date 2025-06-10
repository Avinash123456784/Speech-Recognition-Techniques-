import speech_recognition as sr
import os
from datetime import datetime

def transcribe_and_display():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    # Prepare subtitle file
    now = datetime.now()
    filename = f"subtitles_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    directory = "subtitles_log"
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    print("\n🎙️ Real-Time Subtitling Started... (Press Ctrl+C to stop)\n")

    with open(filepath, "w") as file:
        try:
            while True:
                with mic as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening...", end="\r")
                    audio = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio)
                    print(f"📝 {text}")
                    file.write(text + "\n")
                    file.flush()
                except sr.UnknownValueError:
                    print("⚠️ Couldn't understand. Please speak clearly.")
                except sr.RequestError:
                    print("❌ Could not connect to the recognition service.")
                    break

        except KeyboardInterrupt:
            print("\n⏹️ Subtitling stopped. Subtitles saved to:", filepath)

if __name__ == "__main__":
    transcribe_and_display()
