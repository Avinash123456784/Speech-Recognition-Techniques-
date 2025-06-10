import speech_recognition as sr
import pyautogui
import time

COMMANDS = {
    "jump": "space",
    "left": "left",
    "right": "right",
    "shoot": "ctrl",
    "pause": "esc"
}

def execute_command(command):
    key = COMMANDS.get(command.lower())
    if key:
        pyautogui.press(key)
        print(f"✅ Executed: {command}")
        with open("command_log.txt", "a") as log:
            log.write(f"{command}\n")
    else:
        print(f"❌ Unknown command: {command}")

def listen_and_act():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Say a command: [jump, left, right, shoot, pause]")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        try:
            while True:
                print("🔊 Listening...", end="\r")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"🎮 Command recognized: {command}")
                execute_command(command)

        except KeyboardInterrupt:
            print("\n🛑 Voice control stopped.")
        except sr.UnknownValueError:
            print("⚠️ Could not understand.")
        except sr.RequestError:
            print("❌ Speech Recognition service error.")

if __name__ == "__main__":
    listen_and_act()
