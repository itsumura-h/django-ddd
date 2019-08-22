from ..orator.sample_user import SampleUser

class SampleUserRepository:
    @staticmethod
    def index():
        return SampleUser \
            .select(
                'sample_users.id', 'sample_users.name', 'sample_users.email',
                'sample_permissions.permission'
            ) \
            .join(
                'sample_permissions',
                'sample_users.permission_id',
                '=',
                'sample_permissions.id'
            ) \
            .get() \
            .serialize()
