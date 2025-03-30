import datetime as dt


class Task:
    def get_info(self):
        return self.text, self.date, self.type, self.user


class CalendarTask(Task):
    def __init__(self, text, date, user_id):
        date = date.split()[::-1]
        print(date)
        self.date = dt.date(*[int(x) for x in date])
        self.text = text
        self.type = 'calendar'
        self.user = user_id


class AnnoyingTask(Task):
    def __init__(self, text, delta, user_id):
        self.delta = dt.timedelta(minutes=int(delta))
        self.date = dt.now() + self.delta
        self.text = text
        self.type = 'annoying'
        self.user = user_id
