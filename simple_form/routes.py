from simple_form.data.base_model import DBsession
import os
def includeme(config):

    db_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     'db',
                     'simple_form.db')
    )
    DBsession.db_init(db_file)

    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_route('home', '/')
