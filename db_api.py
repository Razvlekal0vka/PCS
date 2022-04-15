import flask

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/entrance_to_account/<str:login_password>', methods=['GET'])
def entrance_to_account():
    return "Обработчик в news_api"