import speech_recognition as sr
import pyttsx3


class V2v:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def toSpeak(self, text, rate=150, voice_id=0):

        engine = pyttsx3.init()
        # Setting the speaking rate (words per minute)
        engine.setProperty('rate', rate)
        # Getting all available voices
        voices = engine.getProperty('voices')
        # Setting a specific voice (if specified)
        if voice_id is not None:
            engine.setProperty('voice', voices[voice_id].id)
        engine.say(text)
        engine.runAndWait()

    def toText(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Saying something:")
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio)

            except sr.UnknownValueError:
                text = "Could not understand audio"
            except sr.RequestError as e:
                text = "Recogntion error; {0}".format(e)
        return text


# d = V2v()
# datatext = d.toText()

# d.toSpeak(datatext)
