# Speech to Text

--> This is a simple speech-to-text program in Python using the SpeechRecognition library and Google Web Speech API.

--> It listens through your microphone and converts speech into text.

## Requirements :
Python 3.7+

-- Libraries:

--> SpeechRecognition

--> pyaudio

## Setup :

1. Create a virtual environment and activate it:

--> Windows (PowerShell):

 python -m venv venv
 .\venv\Scripts\activate

2. Install dependencies:

pip install SpeechRecognition

pip install pipwin

pip install pyaudio

## Change Language

-->Default language is English (India) (en-IN).

--You can change it in the code, for example:

   recognizer.recognize_google(audio, language="en-US")  # English (US)
   
   recognizer.recognize_google(audio, language="te-IN")  # Telugu
