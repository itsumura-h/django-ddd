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
                permission_en=val['permission']
            ).to_dict()
            for val in users
        ]

        permissions = DDDSampleRpository.permissions_index()
        permissions = [
            DDDSampleEntity(
                id=val['id'],
                permission_en=val['permission']
            ).to_dict()
            for val in permissions
        ]
        return users, permissions

    def create(params):
        print(params)

    def show(id):
        user = DDDSampleRpository.show(id)
        user = DDDSampleEntity(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            birth_date_db=user['birth_date'],
            permission_id=user['permission_id'],
            permission_en=user['permission']
        ).to_dict()

        permissions = DDDSampleRpository.permissions_index()
        permissions = [
            DDDSampleEntity(
                id=val['id'],
                permission_en=val['permission']
            ).to_dict()
            for val in permissions
        ]

        return user, permissions

    def update(id, params):
        user = DDDSampleEntity(
            id=id,
            name=params['name'],
            email=params['email'],
            birth_date_input=params['birth_date'],
            permission_id=params['permission_id']
        ).to_dict()

        result = DDDSampleRpository.update(id, user)
        return result
