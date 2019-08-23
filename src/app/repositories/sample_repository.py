from ..orator.sample.sample_user import SampleUser
from ..orator.sample.sample_permission import SamplePermission


class SampleRepository:

    @staticmethod
    def index():
        """サンプル画面で使うユーザー全件を取得するリポジトリ.

        Returns:
            List[user] -- ユーザー
        """
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

    @staticmethod
    def create():
        """新規作成画面に必要なデータを取得するリポジトリ."""
        return SamplePermission.all().serialize()

    @staticmethod
    def store(params):
        return SampleUser.insert(**params)


    @staticmethod
    def show(id):
        """サンプル画面で使うユーザー情報1件を取得するリポジトリ.

        Arguments:
            id {int} -- usersテーブルのプライマリーキー

        Returns:
            Dict{user} -- ユーザー
        """
        return SampleUser \
            .select(
                'sample_users.id', 'sample_users.name', 'sample_users.email',
                'sample_users.birth_date', 'sample_users.created_at',
                'sample_users.updated_at', 'sample_permissions.permission'
            ) \
            .join(
                'sample_permissions',
                'sample_users.permission_id',
                '=',
                'sample_permissions.id'
            ) \
            .find(id) \
            .serialize()

    @staticmethod
    def update(params):
        print(params)
        return SampleUser \
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
        return SampleUser.find(id).delete()
