import requests
import serial 
from playsound import playsound
import time

def email_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/UNIQUE_EVENT_NAME/with/key/UNIQUE_WEBHOOK_KEY", data=report) 
	
with serial.Serial('COM5', 9600) as ser:
	x = ser.readline()          # read one byte

	
if "Pressed" in str(x):
	print("Press")
	email_alert("test", "Press", "By Arduino")
	playsound("C:\\Users\\will\\Music\\Madeon-DreamDreamDream(OfficialAudio).mp3")
	
	