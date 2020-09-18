from datetime import datetime

class DateTime:
    def Date(self):
        now = datetime.now()
        DDMMYY= now.strftime("%d-%m-%Y")
        return DDMMYY
        
    def Time(self):
        now = datetime.now()
        HHMM= now.strftime("%H-%M")
        timestamp = datetime.timestamp(now)
        return HHMM


           
