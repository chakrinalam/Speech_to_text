import speech_recognition as sr

def main():
    # Create recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎤 Speak something (I’m listening)...")
        audio = recognizer.listen(source)  # listen until silence

        try:
            print("\nRecognizing...")
            text = recognizer.recognize_google(audio, language="en-IN")  # change language if needed
            print("✅ You said: " + text)
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"⚠️ Could not request results; {e}")

if __name__ == "__main__":
    main()
