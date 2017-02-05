from asterisk.ami import AMIClient
import time
from asterisk.ami import EventListener

def event_notification(source, event):
    os.system('notify-send "%s" "%s"' % (event.name, str(event)))

def event_listener(event,**kwargs):
    print(event)

client = AMIClient(address='127.0.0.1',port=5038)
client.login(username='admin',secret='secret5')

client.add_event_listener(event_listener, white_list=['Registry','PeerStatus'])

try:
    while True:
        time.sleep(10)
except (KeyboardInterrupt, SystemExit):
    client.logoff()
