from app.orator.user import User
from app.orator.permission import Permission
from datetime import datetime

class DDDSampleRpository:

    @staticmethod
    def permissions_index():
        return Permission.all().serialize()

    @staticmethod
    def index():
        return User \
            .select(
                "users.id", "users.name", "users.email", "users.birth_date",
                "users.permission_id", "permissions.permission"
            ) \
            .join('permissions', 'users.permission_id', '=', 'permissions.id') \
            .get() \
            .serialize()

    @staticmethod
    def show(id):
        user = User \
            .select(
                "users.id", "users.name", "users.email", "users.birth_date",
                "users.permission_id", "permissions.permission"
            ) \
            .join('permissions', 'users.permission_id', '=', 'permissions.id') \
            .find(id) \
            .serialize()

        return user

    @staticmethod
    def update(id, params):
        # print(params)
        params = {
            'name': params['name'],
            'email': params['email'].get_label(),
            'permission_id': params['permission_id'],
            'birth_date': params['birth_date_input'].get_date(),
            'updated_at': datetime.now().isoformat()
        }

        User \
            .where('id', id) \
            .update(params)

        return User.find(id).serialize()
