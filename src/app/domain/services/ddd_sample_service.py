from app.repositories.ddd_sample_repository import DDDSampleRpository
from app.domain.domain_models.entities.ddd_sample_entity import DDDSampleEntity

class DDDSampleService:
    def index():
        users = DDDSampleRpository.index()
        users = [
            DDDSampleEntity(**val).to_dict()
            for val in users
        ]
        return users