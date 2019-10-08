from datetime import date, datetime

from app.domain.domain_models.value_objects import (
    EmailValueObject,
    PermissionValueObject,
    DatetimeValueObject,
    BirthdateDBValueObject,
    BirthdateInputValueObject
)

class DDDSampleEntity:
    def __init__(self, id: int = None, name: str = None, email: str = None,
                 password: str = None, permission: str = None,
                 permission_id: int = None, birth_date_db: date =None,
                 birth_date_input: str =None, created_at: datetime = None,
                 updated_at: datetime = None):
        self.__id = id
        self.__name = name
        self.__email = EmailValueObject(email) if email else None
        self.__password = password
        self.__permission = PermissionValueObject(permission) \
                            if permission else None
        self.__permission_id = permission_id
        self.__birth_date_db = BirthdateDBValueObject(birth_date_db) \
                                if birth_date_db else None
        self.__birth_date_input = BirthdateInputValueObject(birth_date_input) \
                                    if birth_date_input else None
        self.__created_at = DatetimeValueObject(created_at) \
                            if created_at else None
        self.__updated_at = DatetimeValueObject(updated_at) \
                            if updated_at else None

    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'password': self.__password,
            'permission': self.__permission,
            'permission_id': self.__permission_id,
            'birth_date_db': self.__birth_date_db,
            'birth_date_input': self.__birth_date_input,
            'created_at': self.__created_at,
            'updated_at': self.__updated_at
        }
