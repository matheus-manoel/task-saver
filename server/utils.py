import json
from bson.json_util import loads, dumps
import datetime as dt


def get_tasks(task_model):
    try:
        return task_model.objects.to_json(), 200
    except:
        return 'Unable to retrieve data from sorveterias', 400


def create_task(task_model, data):
    try:
        new_task = {
                'name': '',
                'hours': 0,
                'minutes': 0,
                'date_time': dt.datetime.now
                }

        for key in list(new_task.keys):
            if key in data:
                new_task[key] = data[key]

        task = task_model(**new_task)
        task.save()

        return new_task.to_json, 201
    except:
        return 'Error on creating task.', 400
