from ..domain_models.entities.sample_user_entity import SampleUserEntity
from ...repositories.sample_user_repository import SampleUserRepository


class SampleUserService:
    @staticmethod
    def index():
        users = SampleUserRepository.index()

    @staticmethod
    def store():
        pass

    @staticmethod
    def show(id: int):
        pass

    @staticmethod
    def edit(id: int):
        pass

    def update(id: int):
        pass

    @staticmethod
    def delete(id: int):
        pass
