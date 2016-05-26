import flask

frontend = flask.Blueprint(
    'frontend',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@frontend.route('/')
def index():
    return flask.render_template('base.html')
