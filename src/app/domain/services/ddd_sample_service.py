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
                password=val['password'],
                birth_date_db=val['birth_date'],
                created_at=val['created_at'],
                updated_at=val['updated_at'],
                permission_id=val['permission_id'],
                permission=val['permission']
            ).to_dict()
            for val in users
        ]
        return users

    def show(id):
        user = DDDSampleRpository.show(id)
        print(user)
        user = DDDSampleEntity(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            password=user['password'],
            birth_date_db=user['birth_date'],
            created_at=user['created_at'],
            updated_at=user['updated_at'],
            permission_id=user['permission_id'],
            permission=user['permission']
        ).to_dict()
        return user