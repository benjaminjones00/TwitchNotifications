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
client_id = get_client_id()
  
def live_check(streamer_name, client_id):
    twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" \
                            + streamer_name + "?client_id=" + client_id
    streamer_html = requests.get(twitch_api_stream_url)
    streamer = json.loads(streamer_html.content)
    if streamer['stream'] == None:
        return('Offline')
    else:
        return('Online')
        
def toast_notification():
    toaster = ToastNotifier()
    toaster.show_toast("Twitch Notification", streamer_name + " streamer has gone live", icon_path="twitch.ico", threaded=True)
    while toaster.notification_active(): time.sleep(0.1)
        
with open('streamer_list.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
  test = your_list[0] [0:]
  print(test)
  for test in test:
      live_check(test, client_id)
