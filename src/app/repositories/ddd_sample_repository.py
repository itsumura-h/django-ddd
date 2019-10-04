from app.orator.user import User
from app.orator.permission import Permission

class DDDSampleRpository:

    @staticmethod
    def index():
        return User \
                .select() \
                .join('permissions', 'users.permission_id', '=', 'permissions.id') \
                .get() \
                .serialize()