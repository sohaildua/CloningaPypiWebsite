import flask
import os


from pypi_org.views import home_views
from pypi_org.views import package_views
from pypi_org.views import cms_views
from pypi_org.views import account_views

from pypi_org.data import  db_session

app = flask.Flask(__name__)


def setup_db():
    db_file=os.path.join(os.path.dirname(__file__),'db','pypi.sqlite')
    db_session.global_init(db_file )


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def register_blueprints():
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(account_views.blueprint)



if __name__ == '__main__':
    main()
