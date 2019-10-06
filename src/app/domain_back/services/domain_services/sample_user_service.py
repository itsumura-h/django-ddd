from django.contrib.auth.hashers import make_password
from datetime import date, datetime

from ....repositories.sample_user_repository import SampleUserRepository
from ...domain_models.entities.sample_user_entity import (
    SampleUserEntity,
    SamplePermissionEntity
)
from pprint import pprint


class SampleUserService:

    @staticmethod
    def index():
        """SampleServiceのindexメソッド.

        Returns:
            users -- List[user]
        """
        users = SampleUserRepository.index()
        users = [
            SampleUserEntity(**val).get_index_dict()
            for val in users
        ]
        return users

    @staticmethod
    def create():
        """新規作成画面に必要なデータを取得するサービスクラス.

        Returns:
            permission -- Dict{id:int, permission:str}
        """
        params = SampleUserRepository.create()
        permissions = [
            SamplePermissionEntity(**val).get_create_dict()
            for val in params['permissions']
        ]
        return permissions

    @staticmethod
    def store(params):
        password = f"{params['name']}{date.today().year}"
        params['password'] = make_password(password)
        params['created_at'] = datetime.now()
        params['updated_at'] = datetime.now()
        new_user = SampleUserEntity(**params).get_store_dict()
        is_success = SampleUserRepository.store(new_user)
        if not is_success:
            raise Exception('新規作成失敗')

    @staticmethod
    def show(id):
        """SampleServiceのshowメソッド.

        Arguments:
            id {int} -- userテーブルのプライマリーキー

        Returns:
            user -- ユーザー
        """
        user = SampleUserRepository.show(id)
        user = SampleUserEntity(**user).get_show_dict()
        return user

    @staticmethod
    def edit(id):
        user = SampleUserRepository.edit(id)
        user = SampleUserEntity(**user).get_edit_dict()
        print(user)
        permissions = SampleUserRepository.get_sample_permissions()
        permissions = [
            SamplePermissionEntity(**val).get_create_dict()
            for val in permissions
        ]
        return user, permissions

    @staticmethod
    def update(id, params):
        params['updated_at'] = datetime.now()
        new_user = SampleUserEntity(id, **params).get_update_dict()
        SampleUserRepository.update(new_user)

    @staticmethod
    def destroy(id):
        is_success = SampleUserRepository.destroy(id)
        if not is_success:
            raise Exception('削除失敗')