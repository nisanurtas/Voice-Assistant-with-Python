from __future__ import print_function
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os 
import time
from datetime import datetime
import random
from random import choice
from pydub import AudioSegment
import pywhatkit
import webbrowser
import subprocess
import pyjokes



import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

r= sr.Recognizer()


# def speeding():
#     in_path = 'answer.mp3'
#     ex_path = 'speed.mp3'
#     sound = AudioSegment.from_file(in_path)
#     slower_sound = speed_swifter(sound, 1.3)
#     slower_sound.export(ex_path, format="mp3")

# def speed_swifter(sound, speed=1.0):
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
#     return sound_with_altered_frame_rate


def record(ask = False):
    with sr.Microphone() as source: #get the voice from mic
        if ask:
            print(ask)
        audio = r.listen(source)  
        voice ="" #first its value is empty
        try: 
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Sistem Çalışmıyor")
        return voice
            
            
def response(voice):
        if"merhaba" in voice:
            speak("sana da merhaba")
            
        if "teşekkürler" in voice or "teşekkür ederim" in voice:
            speak("rica ederim")
            exit()
            
        if "görüşürüz" in voice:
            speak("görüşürüz canım")
            exit()
            
        if "nasılsın" in voice:
            speak("İyiyim,sen nasılsın?")
            
        if "iyiyim" or "ben de iyiyim" in voice:
            speak("İyi olmana sevindim!")
            
        if "hangi gündeyiz" in voice:
            today =time.strftime("%A")
            today.capitalize()
            if today == "Monday":
                today=="Pazartesi"
                
            elif today == "Tuesday":
                today=="Salı"
                
            elif today == "Wednesday":
                today=="Çarşamba"
                
            elif today == "Thursday":
                today=="Perşembe"
                
            elif today == "Friday":
                today=="Cuma"
                
            elif today == "Saturday":
                today=="Cumartesi"
                
            elif today == "Sunday":
                today=="Pazar"
                
            speak(today)
            
        if "saat kaç" in voice:
            select = ["Saat şu an: ","Hemen bakıyorum: "]
            clock =datetime.now().strftime("%H:%M")
            # speak(datetime.now().strftime("%H:%M"))
            select =random.choice(select) 
            speak(select + clock)  
            #time.sleep(10) bir süre uyku modu için
            
        if "uygulama aç" in voice:
            speak("Hangi uygulamayı açmamı istiyorsun?")
            runApp =record()
            runApp =runApp.lower()
            if "death stranding" in runApp:
                os.startfile("D:/FileHistory/Hp/MISO/Data/C/Users/Hp/Downloads/Death Stranding (2021_11_28 09_39_56 UTC).exe")
            elif "journey" in runApp:
                os.startfile()
            else: 
             speak("İstediğin uygulama çalıştırma listemde yok.")
             
        if "not et" or "bunu hatırla" in voice:
            speak("Dosya ismi ne olsun?")
            txtFile=record() + ".txt"
            speak("Ne yazmak istiyorsun?")
            theText=record()
            f = open(txtFile, "w",encoding="utf-8")
            f.writelines(theText)
            f.close()

        if "play" in voice:
            song = voice.replace("playing "+ " ")
            speak("playing"+song)
            pywhatkit.playonyt(song)
            
        if "search" in voice:
            ind = voice.replace("search")
            search = voice.split()[ind+ 1:]
            webbrowser.open("https://www.google.com.tr/"+  "+".join(search))
            speak("Searching"+ str(search) + "on google" ) 
            
        if "google" in voice:
            ind = voice.replace("google")
            search = voice.split()[ind+ 1:]
            webbrowser.open("https://www.google.com.tr/"+  "+".join(search))
            speak("Searching"+ str(search) + "on google" ) 
            
        if "bana bir şaka söyle" or "şaka" in voice:
            speak(pyjokes.get_joke())
            
        if "nerede" in voice:
            ind =voice.replace("is")
            location = voice.split()[ind+1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("Aradığın yer burada" + str(location))
            webbrowser.open(url)
            
def speak(string):
    tts = gTTS(text=string,lang="tr") #connect to google
    file = "answer.mp3"
    tts.save(file) 
    #speeding()
    playsound(file)
    os.remove(file)
   # os.remove("speed.mp3")
    
    
def test(wake):
    if "miso" in wake:
        answers =["Efendim?","Seni dinliyorum...","Senin için ne yapabilirim?","Merhaba"]
        answers=random.choice(answers)
        speak(answers)
        if wake != '':
            voice=wake.lower()
            print(wake.capitalize())
            response(voice)
        
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def google_calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        
    except HttpError as error:
        print('An error occurred: %s' % error)

    return service;


def calendarEvents(num,service):
    speak("Merhaba,iyi günler.Bugün yapılacak işler bunlar: ")
      # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print(f'Getting the upcoming {num} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=num, singleEvents=True,
                                              orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
    for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    

while True: #to make voice assistant listen all the time
    voice = record()
    if voice != '':
        voice = voice.lower() #to make it work even if its lowercase 
        print(voice) # to print on terminal
        response(voice) 
    
