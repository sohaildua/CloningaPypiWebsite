import flask

from pypi_org.infrastructure import cookie_auth, request_dict


class VideoModelBase:
    def __init__(self):
        self.request: Request = flask.Request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.user_id: Optional[str] = cookie_auth.get_user_id_via_auth_cookie(flask.request)

    def to_dict(self):
        return self.__dict__
