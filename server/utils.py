from bson.json_util import dumps
import datetime as dt


def check_required_params(required_params, sent_params):
    for arg in required_params:
        if arg not in sent_params:
            return dumps({
                'error': 'Required params {} not sent.'.format(required_params)
                    }), 422


def get_tasks(task_model):
    try:
        return task_model.objects.to_json(), 200
    except:
        return 'Unable to retrieve data from sorveterias', 400


def create_or_update_task(task_model, data):
    required_params = ('name', 'hours', 'minutes')
    check_result = check_required_params(required_params, data)
    if check_result is not None:
        return check_result

    task_matched = task_model.objects(
            name=data['name'],
            date_time=dt.date.today()
    ).first()

    if task_matched is not None:
        return update_task(task_matched, data)
    else:
        return create_task(task_model, data)


def update_task(task_matched, data):
    new_time = dt.timedelta(
                    hours=task_matched.hours + data['hours'],
                    minutes=task_matched.minutes + data['minutes']
            )
    new_hours_minutes = str(new_time).split(':')
    new_hours = int(new_hours_minutes[0])
    new_minutes = int(new_hours_minutes[1])

    action = task_matched.modify(hours=new_hours, minutes=new_minutes)

    if action:
        return task_matched.to_json(), 200
    else:
        return 'Error on updating task.', 400


def create_task(task_model, data):
    new_task = {
            'name': '',
            'hours': 0,
            'minutes': 0,
            'date_time': dt.date.today()
            }

    for key in new_task:
        if key in data:
            new_task[key] = data[key]

    try:
        task = task_model(**new_task)
        task.save()

        return task.to_json(), 201
    except Exception as e:
        # todo: Add raccoon_log
        print(e)
        return 'Error on creating task.', 400
