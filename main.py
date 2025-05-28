import speech_recognition as sr

# Step 1: Create a recognizer
recognizer = sr.Recognizer()

# Step 2: Use microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)  # Record your voice

    try:
        # Step 3: Convert speech to text using Google
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("Network error. Please check your internet.")
