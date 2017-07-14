import mongoengine as me
import datetime as dt


class Task(me.Document):
    name = me.StringField()
    hours = me.IntField(default=0)
    minutes = me.IntField(default=0)
    date_time = me.DateTimeField(default=dt.date.today())
