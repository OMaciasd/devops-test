from . import blueprint

@blueprint.route('/app')
def app_route():
    return "This is the app route!"
