import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello there! How may I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "cupcake" in command:
        speak("Whisk 1 1/4 cups flour, 1 1/4 tsp baking powder, and 1/4 tsp salt. In another bowl, beat 6 tbsp soft butter, 3/4 cup sugar, 2 tbsp oil, and 1 1/2 tsp vanilla until fluffy, then add 2 eggs one at a time. Mix in the dry ingredients alternating with 1/2 cup plus 2 tbsp milk. Fill 12 paper liners 3/4 full and bake at 350°F (176°C) for 15 to 18 minutes.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True

def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__ == "__main__":
    main()