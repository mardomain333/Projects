from tkinter import Tk,ttk,StringVar,IntVar
from _app import *

JSONFILE=load_json()

App=Tk()
App.title("Sedimentary App")
App.iconbitmap(APP_ICON)
App.resizable(False,False)

def alert_check():
    JSONFILE['sedementry_alert']=bool(sedentary_alert.get())
    update_json(JSONFILE)

def interval_receiver(interval):
    JSONFILE['intervel']=int(interval.split()[0])
    update_json(JSONFILE)

#userinterface 
frame=ttk.Frame(App,padding=10)
frame.grid(row=0,column=0,padx=10,pady=10)

#checkbox
sedentary_alert =IntVar()
sedentary_alert.set(
    1 if JSONFILE['sedementry_alert'] else 0
)
check_box=ttk.Checkbutton(frame,text="Sedentary alert",variable=sedentary_alert,command=alert_check)
check_box.grid(row=0,column=0,padx=10)

#dropbox(option menu)
intervel_options=["10 min","15 min","20 min","30 min"]
intervel_value=StringVar()
intervel_value.set(
    f"{JSONFILE['intervel']} min"
)
dropdown=ttk.OptionMenu(frame,intervel_value,"select",*intervel_options,command=interval_receiver)
dropdown.grid(row=1,column=1,pady=5)
intervel_value.set(
    f"{JSONFILE['intervel']} min"
)

#interval label
lebal=ttk.Label(frame,text="Interval")
lebal.grid(row=1,column=0,pady=5)

App.mainloop()