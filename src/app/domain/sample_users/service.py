from .entity import Entity
from .gateway import Gateways
from ..value_objects import(
    EmailValueObject,
    PermissionValueObject,
    DatetimeValueObject,
    BirthdateValueObject,
)

class Service:
    @staticmethod
    def index():
        results = Gateways.index()
        results = [
            Entity(
                id = row['id'],
                name = row['name'],
                email = EmailValueObject(row['email']).get_label(),
                permission= PermissionValueObject(row['permission']).get_ja_label(),
            ).to_dict()
            for row in results
        ]
        return results

    @staticmethod
    def create():
        results = Gateways.create()
        results = [
            {
                'permission': PermissionValueObject(row['permission']).get_ja_label(),
                'permission_id': row['id']
            }
            for row in results['permissions']
        ]
        return results