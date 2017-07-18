def create_api_routes(blueprint, request, utils, models):
    api = blueprint('api', __name__)

    @api.route('/api/tasks', methods=['GET', 'POST'])
    def tasks_create():
        if request.method == 'GET':
            return utils.get_tasks(models.Task)
        elif request.method == 'POST':
            return utils.create_or_update_task(models.Task, request.get_json())

    return api
