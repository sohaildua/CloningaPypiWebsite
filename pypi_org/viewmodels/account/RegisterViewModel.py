from pypi_org.viewmodels.shared.viewmodelbase import VideoModelBase

from pypi_org.infrastructure import request_dict

from pypi_org.services.user_service import find_user_by_email
class RegisterViewModel(VideoModelBase):
    def __init__(self):
        super().__init__()
        self.error = None
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name'
        elif not self.email or not self.email.strip():
            self.error = 'You must specify a email'
        elif not self.password:
            self.error = 'You must specify a password'
        elif len(self.password.strip()) < 5:
            self.error = 'The password must be at least 5 characters'
        elif find_user_by_email(self.email):
            self.error = 'A user with that email address already exists.'
