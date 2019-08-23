from django.core.management.base import BaseCommand
import re
import os


class Command(BaseCommand):
    help = 'DDDのためのファイルを作ります。引数はキャメルケースで入力してください'

    @staticmethod
    def to_sname(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def add_arguments(self, parser):
        parser.add_argument('Domain', nargs='+')

    def handle(self, *args, **options):
        Domain = options['Domain'][0]
        domain = self.to_sname(Domain)

        # ==================== create views ====================
        views_path = f'app/views/{domain}_views.py'
        content = f'''from django.shortcuts import redirect, render
from rest_framework.decorators import api_view

from ..domain.services.{domain}_service import {Domain}Service

# Create your views here.

class {Domain}Views:
    @api_view(['GET'])
    def index(request):
        """全件表示ページ

        Args:
            request ([type]): [description]
        """
        pass

    @api_view(['GET'])
    def create(request):
        """新規作成ページ

        Args:
            request ([type]): [description]
        """
        pass

    @api_view(['POST'])
    def store(request):
        """新規作成を実行

        Args:
            request ([type]): [description]
        """
        pass

    @api_view(['GET'])
    def show(request, id: int):
        """一件表示ページ

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        pass

    @api_view(['GET'])
    def edit(request, id: int):
        """一件編集ページ

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        pass

    @api_view(['POST'])
    def update(request, id: int):
        """一件編集を実行

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        pass

    @api_view(['POST'])
    def destroy(request, id: int):
        """一件削除を実行

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        pass
'''

        # ファイルが存在していたらエラー
        if os.path.exists(views_path):
            print(f'{views_path}は既に存在しています')
        else:
            with open(views_path, 'w') as f:
                f.write(content)
            print(f'{views_path}が作成されました')

        # ==================== create serivce ====================
        serivce_path = f'app/domain/services/{domain}_service.py'
        content = f'''from ..domain_models.entities.{domain}_entity import {Domain}Entity
from ...repositories.{domain}_repository import {Domain}Repository


class {Domain}Service:
    @staticmethod
    def index():
        pass

    @staticmethod
    def store():
        pass

    @staticmethod
    def show(id: int):
        pass

    @staticmethod
    def edit(id: int):
        pass

    def update(id: int):
        pass

    @staticmethod
    def delete(id: int):
        pass
'''

        # ファイルが存在していたらエラー
        if os.path.exists(serivce_path):
            print(f'{serivce_path}は既に存在しています')
        else:
            with open(serivce_path, 'w') as f:
                f.write(content)
            print(f'{serivce_path}が作成されました')

        # ==================== create entity ====================
        entity_path = f'app/domain/domain_models/entities/{domain}_entity.py'
        content = f'''# from ..value_objects import (
# )

class {Domain}Entity:
    def __init__(self):
        pass
'''
        # ファイルが存在していたらエラー
        if os.path.exists(entity_path):
            print(f'{entity_path}は既に存在しています')
        else:
            with open(entity_path, 'w') as f:
                f.write(content)
            print(f'{entity_path}が作成されました')

        # ==================== create repository ====================
        repository_path = f'app/repositories/{domain}_repository.py'
        content = f'''class {Domain}Repository:
    pass
'''

        # ファイルが存在していたらエラー
        if os.path.exists(repository_path):
            print(f'{repository_path}は既に存在しています')
        else:
            with open(repository_path, 'w') as f:
                f.write(content)
            print(f'{repository_path}が作成されました')
