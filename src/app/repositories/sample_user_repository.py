from ..orator.user import User
from ..orator.permission import Permission


class SampleUserRepository:

    @staticmethod
    def index():
        """サンプル画面で使うユーザー全件を取得するリポジトリ.

        Returns:
            List[user] -- ユーザー
        """
        return User \
            .select(
                'users.id', 'users.name', 'users.email',
                'permissions.permission'
            ) \
            .join(
                'permissions',
                'users.permission_id',
                '=',
                'permissions.id'
            ) \
            .get() \
            .serialize()

    @staticmethod
    def create():
        """新規作成画面に必要なデータを取得するリポジトリ."""
        permissions = SampleUserRepository.get_permissions()
        params = {
            'permissions': permissions
        }
        return params

    @staticmethod
    def store(params):
        return User.insert(**params)

    @staticmethod
    def show(id):
        """サンプル画面で使うユーザー情報1件を取得するリポジトリ.

        Arguments:
            id {int} -- usersテーブルのプライマリーキー

        Returns:
            Dict{user} -- ユーザー
        """
        return User \
            .select(
                'users.id', 'users.name', 'users.email',
                'users.birth_date', 'users.created_at',
                'users.updated_at', 'permissions.permission'
            ) \
            .join(
                'permissions',
                'users.permission_id',
                '=',
                'permissions.id'
            ) \
            .find(id) \
            .serialize()

    @staticmethod
    def edit(id):
        return User.find(id).serialize()

    @staticmethod
    def update(params):
        print(params)
        return User \
            .where('id', params['id']) \
            .update(**params)

    @staticmethod
    def destroy(id):
        """ユーザーを1件削除する.

        Arguments:
            id {int} -- usersテーブルのプライマリーキー

        Returns:
            bool -- 成功:True 失敗:False
        """
        return User.find(id).delete()

    @staticmethod
    def get_permissions():
        return Permission.all().serialize()
