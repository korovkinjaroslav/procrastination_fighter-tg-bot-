import datetime as dt


class Task:
    def get_info(self):
        return self.text, self.date


class CalendarTask(Task):
    def __init__(self, text, date):
        date = date.split()[::-1]
        print(date)
        self.date = dt.date(*[int(x) for x in date])
        self.text = text


class AnnoyingTask(Task):
    def __init__(self, text, delta):
        self.delta = dt.timedelta(minutes=int(delta))
        self.date = dt.now() + self.delta
        self.text = text
