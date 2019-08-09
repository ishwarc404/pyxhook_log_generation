
import os
def main_run():
    # complete info of activities
    import pyHook
    import pythoncom
    from datetime import datetime

    f = open("log.txt","w")
    pid_main  = os.getpid()  #we are getting the PID as we need to kill this subprocess later on
    f.write(str(pid_main) + "\n")

    def OnMouseEvent(event):
        #     print('MessageName:',event.MessageName)
        #     #print('Message:',event.Message)
        #     print('Time:',event.Time)
        #     #print('Window:',event.Window)
        #     print('WindowName:',event.WindowName)
        print('Position:',event.Position)
        #     #print('Wheel:',event.Wheel)
        #     #print('Injected:',event.Injected)
        #     #print('---')
      
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        

        # print("Current Time =", current_time)
        time = str(event.Time)
        record_string = 'Message_Name' + "$" + event.MessageName + "$" + "Time" + "$" + current_time  + "$" +'Window_Name' + "$" + event.WindowName+"\n"
        print(record_string)
        f.write(record_string)
        #f.write(str(dict([('Message_Name',event.MessageName),('Time',event.Time),('Window_Name',event.WindowName)]))+"\n")
        return True


    def OnKeyboardEvent(event):
        # print('MessageName:',event.MessageName)
        # #print('Message:',event.Message)
        # print('Time:',event.Time)
        # #print('Window:',event.Window)
        # print('WindowName:',event.WindowName)
        # #print('Ascii:', event.Ascii, chr(event.Ascii))
        # print('Key:', event.Key)
        # print('KeyID:', event.KeyID)
        # print('ScanCode:'), event.ScanCode
        # print('Extended:'), event.Extended
        # print('Injected:'), event.Injected
        # print('Alt'), event.Alt
        # print('Transition'), event.Transition
        # print('---')

        if(event.Key == "Escape"):    #escape key added as a hotkey for now. must be configurable later on.
            return False

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        time = str(event.Time)
        record_string = 'Message_Name' + "$" + event.MessageName + "$" + "Time" + "$" + current_time  + "$" +'Window_Name' + "$" + event.WindowName+"\n"
        print(record_string)
        f.write(record_string)
        return True

    hm = pyHook.HookManager()

    hm.MouseAll = OnMouseEvent
    hm.HookMouse()

    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()

    pythoncom.PumpMessages()
    hm.UnhookMouse()
    hm.UnHookKeyboard()


main_run()