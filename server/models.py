import mongoengine as me


class Task(me.EmbeddedDocument):
    name = me.StringField()
    hours = me.IntField()
    minutes = me.IntField()
    date_time = me.DateTimeField()
