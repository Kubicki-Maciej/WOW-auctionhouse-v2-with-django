import json
with open('settings.json', 'r') as file:
    data = json.load(file)
    
DEBUG = data["DEBUG"]

class Timer:
    
    def __init__(self):
        if DEBUG:
            print('show timer')
        pass
    
    def start_timer():
        pass
    
    def end_timer():
        pass