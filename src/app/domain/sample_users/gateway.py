from .repository import Repository

class Gateways:
    @staticmethod
    def index():
        return Repository.index()
        
    @staticmethod
    def create():
        permissions = Repository.create()
        return {
            'permissions': permissions
        }