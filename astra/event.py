from .client import FIELDS
from datetime import datetime, date, time

def date_plus_minutes(datestr, minute):
    if minute is None or datestr is None:
        return None

    hour = minute // 60
    minute %= 60

    return datetime.combine(
        datetime.strptime(datestr, "%Y-%m-%dT%H:%M:%S").date(),
        time(hour=hour, minute=minute)
    )

class Event:
    def __init__(self, our_fields):
        self.fields = dict(zip(FIELDS, our_fields))
        self.name = self.fields['EventName']
        self.type = self.fields['EventType']
        self.begin = date_plus_minutes(self.fields['StartDate'],
                self.fields['StartMinute'])
        self.end = date_plus_minutes(self.fields['EndDate'],
                self.fields['EndMinute'])
        self.location = self.fields['BuildingRoom']
        self.description = self.fields['EventDescription']

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return "{} ({}) from {} to {} in {}".format(self.name, self.type,
                self.begin, self.end, self.location)
