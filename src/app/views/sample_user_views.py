from django.shortcuts import redirect, render
from rest_framework.decorators import api_view

from ..domain.services.sample_user_service import SampleUserService

# Create your views here.

class SampleUserViews:
    @api_view(['GET'])
    def index(request):
        """全件表示ページ

        Args:
            request ([type]): [description]
        """
        users = SampleUserService.index()
        return render(request, 'sample/index.html')

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
