import json
import os
import winsound
from win10toast import ToastNotifier
toaster=ToastNotifier()
#assets
APP_ICON=os.path.join("assets","app.ico")
COFFEE_ICON=os.path.join("assets","coffe.ico")
DOLPHIN=os.path.join("assets","dolphin.wav")

JSONFILE :dict
def load_json():

    with open("Appdata.json") as jsonfile:
        return json.load(jsonfile)
    
def update_json(data : dict):
    with open("Appdata.json","w") as jsonfile:
        json.dump(data,jsonfile,indent=2)

def __notifier(
        msg,icon=APP_ICON,title=None,sound=DOLPHIN
):
    toaster.show_toast(
        msg=msg,
        title=title if title else "Notification",
        icon_path=icon,
        threaded=True

    )
    if sound:
        winsound.PlaySound(sound,flags=winsound.SND_FILENAME)
        