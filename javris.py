# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import pywhatkit

# # Initialize the speech engine
# engine = pyttsx3.init()

# def speak(text):
#     print("Jarvis:", text)
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}")
#     except Exception:
#         speak("Sorry, I didn't catch that. Please say it again.")
#         return "none"
    
#     return query.lower()

# def wish_me():
#     hour = int(datetime.datetime.now().hour)
#     if hour < 12:
#         speak("Good morning!")
#     elif hour < 18:
#         speak("Good afternoon!")
#     else:
#         speak("Good evening!")
#     speak("I am Jarvis. How can I assist you?")

# # Main program starts here
# if __name__ == "__main__":
#     wish_me()
#     while True:
#         command = take_command()

#         if 'wikipedia' in command:
#             speak('Searching Wikipedia...')
#             command = command.replace("wikipedia", "")
#             results = wikipedia.summary(command, sentences=2)
#             speak("According to Wikipedia")
#             speak(results)

#         elif 'open youtube' in command:
#             speak("Opening YouTube...")
#             webbrowser.open("https://youtube.com")

#         elif 'search' in command:
#             speak("Searching online...")
#             pywhatkit.search(command.replace("search", ""))

#         elif 'time' in command:
#             time = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The time is {time}")

#         elif 'exit' in command or 'stop' in command:
#             speak("Goodbye!")
#             break


