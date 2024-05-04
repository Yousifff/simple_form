from pyramid.view import view_config


@view_config(route_name='home', renderer='simple_form:templates/home.pt')
def my_view(request):
    return {'project': 'simple_form'}
