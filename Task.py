import datetime as dt


class Task:
    def __init__(self, text):
        self.text = text


class CalendarTask(Task):
    def __init__(self, date):
        date = reversed(date)
        self.date = dt.date(*[int(x) for x in date.split()])


class AnnoyingTask(Task):
    def __init__(self, delta):
        self.date = dt.now()
        self.delta = dt.timedelta(int(delta))
