def create_visual_routes(blueprint, request, models):
    visual = blueprint(
                    'visual', __name__,
                    static_folder='static',
                    template_folder='templates'
    )

    @visual.route('/', methods=['GET', 'POST'])
    def daily():
        return "yeahhh"

    return visual
