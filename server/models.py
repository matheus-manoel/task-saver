import mongoengine as me


class Task(me.Document):
    name = me.StringField()
    hours = me.IntField()
    minutes = me.IntField()
    date_time = me.DateTimeField()
