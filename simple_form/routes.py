def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_route('home', '/')
