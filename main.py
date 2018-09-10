import wolframalpha
import os
import speech_recognition as sr
import pyttsx
from tkinter import ttk
import io
import base64
import turtle

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from urllib.request import urlopen
    from urllib.request import urlopen
import thread,re
import tkinter.font
import tkinter.messagebox
from progressbar import ProgressBar, Percentage, ETA, FileTransferSpeed, Bar


root=Tk()
root.configure(background="#030719")
root.title("Artificial Intellegence - Jarvis")
root.state('zoomed')

def update_text(userinput_text):
	print ("update text")
	label_input['text']=userinput_text

def get_answer(question):
	app_id='7H8VWR-43EJVJQWEV' # wolframalpha app ID
	if question=="who are you" or question=="what is your name":
		answer="I am Jarvis, a virtual artificial intelligence"
	else:
		try:
			client = wolframalpha.Client('7H8VWR-43EJVJQWEV')
			res = client.query(question)
			for pod in res.pods:
			    for sub in pod.subpods:
			        print(sub)
			# print(next(res.results).text)
			print ('$$$$$$$$$$$$$$$$$$$$$$$')

			print(next(res.results).text)
			answer=next(res.results).text
		except:
			answer="Something went wrong. Lets try it again. Shall we?"
	engine = pyttsx.init()
	# engine.say('Sally sells seashells by the seashore.')
	engine.say(answer)
	update_text(answer)
	engine.runAndWait()


def audio():
	button_activate['text']="Jarvis Activated.."
	button_activate['state']='disabled'
	pb.start()
	while True:
		# Record Audio
		r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("Say something!")
		    userinput= "Say Something..."
		    update_text(userinput)
		    audio = r.listen(source)
		 
		# Speech recognition using Google Speech Recognition
		try:
		    # for testing purposes, we're just using the default API key
		    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		    # instead of `r.recognize_google(audio)`
		    userinput=r.recognize_google(audio)
		    print("You said: " + userinput)
		    
		    update_text(userinput)
		    get_answer(userinput)

		    
		except sr.UnknownValueError:
		    print("Google Speech Recognition could not understand audio")
		    userinput="Google Speech Recognition could not understand audio"
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))
		    userinput="Could not request results from Google Speech Recognition service; {0}".format(e)
		# update_text(userinput)
def performanceBoost():
		# update_text("Activating voice recognization...")
	t1=thread.start_new_thread( update_text, ("Say Something..", ) )
	t2=thread.start_new_thread( audio,())

frame1=Frame(root,height=330, width=660,borderwidth=2,relief=RIDGE,bg='#030719',highlightbackground='white')
frame1.pack()
frame1.place(relx=0.3, rely=0.4)
	
label_input=Label(frame1, text="",font='Verdana 8 bold',fg='#0C90F2',bg='#030719', wraplength=600)
label_input.pack(anchor=W)
label_input.place(relx=0.5, rely=0.5, anchor=CENTER)


button_activate=Button(root,text="Activate",command=performanceBoost,width=15,justify='center',borderwidth=4,font='Verdana 8 bold')
button_activate.pack(anchor=W)
button_activate.place(relx=0.5, rely=0.2, anchor=CENTER)

pb = ttk.Progressbar(frame1, orient="horizontal", length=660, mode="determinate")
pb.pack()
pb.place(rely=0.95)

# tk.PhotoImage(file="C:/Users/abangerx/Pictures/black-wallpaper-13.jpg")

root.mainloop()
	# t1=thread.start_new_thread( gui, ())
	# t2=thread.start_new_thread( audio,())
