import requests

FIELDS = ['EventName', 'EventType', 'StartDate', 'EndDate', 'StartMinute',
          'EndMinute', 'BuildingRoom', 'EventDescription']

class Client:
    def __init__(self, base):
        self.base_url = base.strip('/')
        self.start_url = base + '/Portal/GuestPortal.aspx'
        self.event_url = base + '/~api/search/eventMeeting'
        self.refresh()

    def refresh(self):
        self.session = requests.Session()
        self.session.get(self.start_url)

    def get_events(self, filt, limit=100):
        result = self.session.get(self.event_url,
                params={'fields': FIELDS, 'filter': filt._expr(), 'limit': limit})

        if result.status_code != 200:
            return []

        from . import event
        data = [event.Event(i) for i in result.json()["data"]]
        result = []
        for i in data:
            if i not in result:
                result.append(i)

        return result
