from datetime import date, datetime
from ..value_objects import (
    EmailValueObject,
    PermissionValueObject,
    DatetimeValueObject,
    BirthdateValueObject
)


class SampleUserEntity:
    def __init__(self, id: int = None, name: str = None, email: str = None,
                 password: str = None, permission: str = None,
                 permission_id: int = None, birth_date=None,
                 created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.name = name
        self.email = EmailValueObject(email)
        self.password = password
        self.permission = PermissionValueObject(permission)
        self.permission_id = permission_id
        self.birth_date = BirthdateValueObject(birth_date)
        self.created_at = DatetimeValueObject(created_at)
        self.updated_at = DatetimeValueObject(updated_at)

    def get_index_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email.get_label(),
            'permission': self.permission.get_ja_label()
        }

    def get_store_dict(self):
        return {
            'name': self.name,
            'email': self.email.get_label(),
            'password': self.password,
            'permission_id': self.permission_id,
            'birth_date': self.birth_date.get_date(),
            'created_at': self.created_at.get_label(),
            'updated_at': self.updated_at.get_label()
        }

    def get_show_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email.get_label(),
            'permission': self.permission.get_ja_label(),
            'age': self.birth_date.get_age(),
            'created_at': self.created_at.get_label(),
            'updated_at': self.updated_at.get_label()
        }

    def get_edit_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email.get_label(),
            'permission_id': self.permission_id,
            'birth_date': self.birth_date.get_str_number(),
        }

    def get_update_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email.get_label(),
            'permission_id': self.permission_id,
            'birth_date': self.birth_date.get_date(),
            'updated_at': self.updated_at.get_label()
        }


class SamplePermissionEntity:
    def __init__(self, id: int = None, permission: str = None):
        self.id = id
        self.permission = PermissionValueObject(permission)

    def get_create_dict(self):
        return {
            'id': int(self.id),
            'permission': self.permission.get_ja_label()
        }
