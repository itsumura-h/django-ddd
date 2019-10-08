from app.repositories.ddd_sample_repository import DDDSampleRpository
from app.domain.domain_models.entities.ddd_sample_entity import DDDSampleEntity

class DDDSampleService:
    def index():
        users = DDDSampleRpository.index()
        users = [
            DDDSampleEntity(
                id=val['id'],
                name=val['name'],
                email=val['email'],
                birth_date_db=val['birth_date'],
                permission_id=val['permission_id'],
                permission=val['permission']
            ).to_dict()
            for val in users
        ]
        return users

    def show(id):
        user, options = DDDSampleRpository.show(id)
        user = DDDSampleEntity(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            birth_date_db=user['birth_date'],
            permission_id=user['permission_id'],
            permission=user['permission']
        ).to_dict()

        options = [
            DDDSampleEntity(
                id=val['id'],
                permission=val['permission']
            ).to_dict()
            for val in options
        ]
        return user, options