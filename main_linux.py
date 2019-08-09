from __future__ import print_function

# Libraries we need
import pyxhook
import time
import os
from datetime import datetime

def main_run():

	f = open("log.txt","w")
	pid_main  = os.getpid()  #we are getting the PID as we need to kill this subprocess later on
	f.write(str(pid_main) + "\n")



	# This function is called every time a key is presssed
	def OnMouseEvent(event):
	    global running
	    # print key info
	    now = datetime.now()
	    current_time = now.strftime("%H:%M:%S")
	    #time = str(event.Time)
	    record_string = 'Message_Name' + "$" + event.MessageName + "$" + "Time" + "$" + current_time  + "$" +'Window_Name' + "$" + event.WindowName+"\n"
	    print(record_string)
	    f.write(record_string)
	    return True





	# This function is called every time a key is presssed
	def kbevent(event):
	    global running
	    # print key info
	    now = datetime.now()
	    current_time = now.strftime("%H:%M:%S")

	    record_string = 'Message_Name' + "$" + event.MessageName + "$" + "Time" + "$" + current_time  + "$" +'Window_Name' + "$" + event.WindowName+"\n"
	    print(record_string)
	    f.write(record_string)
	    return True

	    # If the ascii value matches spacebar, terminate the while loop
	    if event.Ascii == 32:
		running = False


	# Create hookmanager
	hookman = pyxhook.HookManager()

	#mouse
	hookman.MouseMovement = OnMouseEvent
	hookman.HookMouse()
	hookman.MouseAllButtonsDown = OnMouseEvent
	hookman.MouseAllButtonsUp = OnMouseEvent

	# Define our callback to fire when a key is pressed down
	hookman.KeyDown = kbevent
	# Hook the keyboard
	hookman.HookKeyboard()
	# Start our listener
	hookman.start()

	# Create a loop to keep the application running
	running = True
	while running:
	    time.sleep(0.1)

	# Close the listener when we are done
	hookman.cancel()

main_run()
