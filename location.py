import requests

class Location:
    def find_location(self):
        res=requests.get('https://ipinfo.io')
        data=res.json()
        region = data['region']
        return region

