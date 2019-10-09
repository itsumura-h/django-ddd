from app.orator.user import User
from app.orator.permission import Permission
from datetime import datetime

class DDDSampleRpository:

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

        options = Permission.all().serialize()
        return user, options

    @staticmethod
    def update(id, params):
        # print(params)
        params = {
            'id': params['id'],
            'name': params['name'],
            'email': params['email'].get_label(),
            'permission_id': params['permission_id'],
            # 'permission': params['permission_ja'].get_en_label(),
            'birth_date': params['birth_date_input'].get_date(),
            'updated_at': datetime.now().isoformat()
        }
        print(params)

        User \
        .where('id', id) \
        .update(params)

        return User.find(id).serialize()