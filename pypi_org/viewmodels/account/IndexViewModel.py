from pypi_org.viewmodels.shared.viewmodelbase import VideoModelBase

from pypi_org.services import user_service


class IndexViewModel(VideoModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.get_user_by_id(self.user_id)
