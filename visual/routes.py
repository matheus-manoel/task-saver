from flask import render_template


def create_visual_routes(blueprint, request, models):
    visual = blueprint(
                    'visual', __name__,
                    static_folder='static',
                    template_folder='templates'
    )

    @visual.route('/', methods=['GET'])
    def daily():
        return render_template('index.html')

    return visual
