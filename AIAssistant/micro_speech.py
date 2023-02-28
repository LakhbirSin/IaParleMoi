import openai
import azure.cognitiveservices.speech as speechsdk
import pyttsx3

# Configure OpenAI API
openai.api_key = ""

# Configure Azure Speech Services
speech_config = speechsdk.SpeechConfig(
    subscription="",
    region=""
)
speech_config.speech_synthesis_voice_name = ""

# Create a speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="fr-fr")

# Start recognition and get a result
result = speech_recognizer.recognize_once()

# Use OpenAI API to process the recognized text in French
Response = openai.Completion.create(
    engine="ada",
    prompt=result.text,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.6
)

# Use pyttsx3 to read the response aloud


engine = pyttsx3.init()   
engine.say(Response.choices[0].text)
engine.runAndWait()

# Print the results
print("Texte reconnu :", result.text)
print("Réponse:", Response.choices[0].text)