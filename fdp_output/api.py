import multiprocessing
from flask import Flask, request, jsonify
import threading

host_name = "0.0.0.0"
port = 7003

app = Flask(__name__)             # create an app instance

APP_VERSION = "1.0.2"

_events_queue: multiprocessing.Queue = None
_events_queue_al: multiprocessing.Queue = None
_events_queue_aa: multiprocessing.Queue = None
_events_queue_up: multiprocessing.Queue = None

@app.route("/get", methods=['GET'])
def get_alerts():
    if 'auth' not in request.headers:
        return "unauthorized", 401
    auth = request.headers['auth']
    #if auth != 'very-secure-token':
    #    return "unauthorized", 401

    reqRole = "none"
    reqAction = "none"
    events = []
    while True:
        try:
            event1 = _events_queue.get_nowait()
            for item in event1["auths"]:
                if item['source_id'] == auth:
                    events.append(item)
                    reqRole = item['role']
                    reqAction = item['action']
                    break
            #    events.append(item)    
        except Exception as _:
                break
        
        if reqRole == "user" and reqAction == "get_alert":
            try:
                event2 = _events_queue_al.get_nowait()
                for item in event2["alerts"]:
                    events.append(item)
            except Exception as _:
                break
        elif reqRole == "user" and reqAction == "get_data":
            try:
                event3 = _events_queue_aa.get_nowait()
                for item in event3['new_data']:
                    events.append(item)
            except Exception as _:
                break
        elif reqRole == "admin" and reqAction == "get_update":
            try:
                event4 = _events_queue_up.get_nowait()
                for item in event4['ups']:
                    events.append(item)
            except Exception as _:
                break
        else:
            if reqRole == "admin" and reqAction == "get_data":
                events.append(
                    {
                        "Message": "Access denied"
                    }
                )
            if reqRole == "admin" and reqAction == "get_alert":
                events.append(
                    {
                        "Message": "Access denied"
                    }
                )
            if reqRole == "user" and reqAction == "get_update":
                events.append(
                    {
                        "Message": "Access denied"
                    }
                )
            

    return jsonify(events)

def start_rest(events_queue, events_queue_al, events_queue_aa, events_queue_up):
    
    global _events_queue ## for auth data
    _events_queue = events_queue

    global _events_queue_al ## for alert data
    _events_queue_al = events_queue_al

    global _events_queue_aa ## for current data
    _events_queue_aa = events_queue_aa

    global _events_queue_up ## for update data
    _events_queue_up = events_queue_up

    threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()

