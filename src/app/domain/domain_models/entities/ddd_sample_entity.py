from datetime import datetime

from app.domain.domain_models.value_objects import 

class DDDSampleEntity:
    def __init__(self, id: int = None, name: str = None, email: str = None,
                 password: str = None, permission: str = None,
                 permission_id: int = None, birth_date=None,
                 created_at: datetime = None, updated_at: datetime = None):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__permission = permission
        self.__permission_id = permission_id
        self.__birth_date = birth_date
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__age = 

    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'password': self.__password,
            'permission': self.__permission,
            'permission_id': self.__permission_id,
            'birth_date': self.__birth_date,
            'created_at': self.__created_at,
            'updated_at': self.__updated_at
        }

    def set_age(self, birth_date):
        
        now = datetime.now()
        birth_date = birth_date.split('T')[0].split('-')
        year = birth_date[0]
        month = birth_date[1]
        date = birth_date[2]
        print(year, month, date)