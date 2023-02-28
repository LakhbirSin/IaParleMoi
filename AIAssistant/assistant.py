import streamlit as st
import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = ""

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

STOP_PHRASE = "exit"

conversation = ""
user_name= 'lakhbir'
bot_name = 'Jarvis'


st.title("Assistant vocal NMPP")

st.write("Parlez à votre assistant vocal. Pour arrêter, dites 'exit'.")

def listen():
    with mic as source:
        st.write("\n Ecoute...")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
    st.write("Analyse")

    try:
        user_input = r.recognize_google(audio,language="fr-fr")
        st.write(user_input)
        return user_input
    except:
        return None

while True:
    user_input = listen()
    if user_input == STOP_PHRASE:
        break
    
    if user_input is not None:
        prompt = user_name+":"+user_input+"\n"+bot_name+":"
        conversation+= prompt

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_str = response["choices"][0]["text"].replace("\n" , "")
        response_str  = response_str.split(
            user_name + ":", 1)[0].split(bot_name + ": " ,1)[0]

        conversation+=response_str+ "\n"
        st.write(bot_name + ": " + response_str)

        engine.say(response_str)
        engine.runAndWait()
