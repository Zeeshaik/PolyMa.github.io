import sys
import speech_recognition as sr
import datetime
import pyaudio
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PolyMaGui import Ui_PolyMaGui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am Polyma sir. please tell me how may i help you?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()


    def run(self):
        self.TaskExecution()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print("User said: ", self.query)

        except sr.RequestError:
            speak("Sorry, my speech service is down ")
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that")
            return "None"
        return self.query

    def TaskExecution(self):
        wishMe()

        try:
            while True:
                self.query = self.take_command()
                # logics for executing tasks
                if "what is your name" in self.query:
                    speak("My name is Jarvis")

                elif 'play' in self.query:
                    song = self.query.replace('play', '')
                    speak('playing online')
                    pywhatkit.playonyt(song)


                elif 'time' in self.query:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    speak('Current time is ' + time)

                elif "sbtet" in self.query:
                    speak("Opening SBTET")
                    webbrowser.open("https://www.sbtet.telangana.gov.in")

                elif "board notification" in self.query:
                    speak("Opening board notification official site")
                    webbrowser.open("https://www.sbtet.telangana.gov.in/?page_id=175")

                elif "wikipedia" in self.query:
                    speak("Searching wikipedia....")
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    print(results)
                    speak(results)

                elif "diploma results" in self.query:
                    speak("Opening Diploma results official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentResult")


                elif "diploma hall ticket" in self.query:
                    speak("Opening diploma official site")
                    webbrowser.open("https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/Hallticket")

                elif "diploma exam fee" in self.query:
                    speak("Opening Diploma exam fee payment official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/DiplomaFeePayment")

                elif "student attendance" in self.query:
                    speak("Opening Diploma student attendance official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentAttendance")

                elif "student feedback" in self.query:
                    speak("Opening Diploma student feedback official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentFeedBack")

                elif "consolidate result" in self.query:
                    speak("Opening Diploma consolidate result official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentConsolidatedResult")

                elif "backlogs exception" in self.query:
                    speak("Opening Diploma backlog exception official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentOnlineRequest")

                elif "student request" in self.query:
                    speak("Opening Diploma student request official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/StudentRequestForm")

                elif "check application" in self.query:
                    speak("Opening Diploma student request official site")
                    webbrowser.open(
                        "https://exams.sbtet.telangana.gov.in/index.html#/Dashboard/Diploma/GenuinenessCheckForm")

                elif "diploma colleges" in self.query:
                    speak("Opening Diploma colleges information in telangana")
                    webbrowser.open("https://dtets.cgg.gov.in/BeforeLoginDistrictCollege.do")

                elif "polycet" in self.query:
                    speak("Opening polycet official site")
                    webbrowser.open("https://tspolycet.nic.in/default.aspx")


                elif "search" in self.query:
                    speak("What do you want to search?")
                    search = self.take_command()

                    url = "https://google.com/search?q=" + search
                    webbrowser.get().open(url)
                    speak("Here is what I found for" + search)

                elif "location" in self.query:
                    speak("what is the location you searching for?")
                    location = self.take_command()
                    url1 = "https://google.com/maps/place/" + location
                    webbrowser.get().open(url1)
                    speak("Here is the location" + location)



                elif "quit" in self.query:
                    speak("thank you! I hope I have fulfill your requirement")
                    exit()

        except sr.UnknownValueError:
            speak("sorry, I am unable to search")


startExecution = MainThread()

FROM_MAIN_ = loadUiType
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PolyMaGui()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("122.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("125.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("130.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("127.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()

    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_4.setText(label_time)
        self.ui.label_5.setText(label_date)


app = QApplication(sys.argv)
PolyMa = Main()
PolyMa.show()
exit(app.exec_())

