import time
import requests
import json
import csv
from win10toast import ToastNotifier

def get_client_id():
    with open('client_id.csv', 'r') as client_id_file:
        reader = csv.reader(client_id_file)
        client_id = list(reader)
        user_client_id = client_id[3][0][13:-1]
        return(user_client_id)

def live_check(streamer_name, client_id):
    twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" \
                            + streamer_name + "?client_id=" + client_id
    streamer_html = requests.get(twitch_api_stream_url)
    streamer = json.loads(streamer_html.content)
    if streamer['stream'] == None:
        return(False)
    else:
        return(True)

def toast_notification(streamer_name):
    toaster = ToastNotifier()
    toaster.show_toast("Twitch Notification", streamer_name + " is now live!", icon_path="twitch.ico", threaded=True)
    while toaster.notification_active(): time.sleep(0.1)

client_id = get_client_id()

notify = []
online = []

with open('streamer_list.csv', 'r') as streamer_list_file:
    reader = csv.reader(streamer_list_file)
    reader_list = list(reader)
    streamer_list = reader_list[0] [0:]
offline = streamer_list[0:]


while True:
    for x in offline:
        if live_check(x, client_id) is True:
            notify.append(x)
            offline.remove(x)
        else:
            pass

    for x in notify:
        toast_notification(x)
        online.append(x)
        notify.remove(x)

    for x in online:
        if live_check(x, client_id) is True:
            pass
        elif live_check(x, client_id) is False:
            offline.append(x)
            online.remove(x)
