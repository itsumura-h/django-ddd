from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from ..domain.services.domain_services.sample_service import SampleService
from pprint import pprint


# Create your views here.


class SampleViews:
    @api_view(['GET'])
    def index(request):
        """全件表示ページ.

        Args:
            request ([type]): [description]
        """
        users = SampleService.index()
        return render(request, 'sample/index.html', {'users': users})

    @api_view(['GET'])
    def create(request):
        """新規作成ページ.

        Args:
            request ([type]): [description]
        """
        permissions = SampleService.create()
        return render(request, 'sample/create.html', {'permissions': permissions})

    @api_view(['POST'])
    def store(request):
        """新規作成を実行.

        Args:
            request ([type]): [description]
        """
        try:
            name = request.POST['name']
            email = request.POST['email']
            birth_date = request.POST['birth_date']
            permission_id = request.POST['permission']

            params = {
                'name': name,
                'email': email,
                'birth_date': birth_date,
                'permission_id': permission_id
            }
            SampleService.store(params)
            return redirect('/sample/')
        except Exception as e:
            # エラーの時
            permissions = SampleService.create()
            params = {
                'permissions': permissions,
                'error': str(e),
                'old': {
                    'name': name,
                    'email': email,
                    'birth_date': birth_date,
                    'permission': permission_id
                }
            }

            return render(request, 'sample/create.html', params)

    @api_view(['GET'])
    def show(request, id: int):
        """一件表示ページ.

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        user = SampleService.show(id)
        return render(request, 'sample/show.html', {'user': user})

    @api_view(['GET'])
    def edit(request, id: int):
        """一件編集ページ.

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        user = SampleService.edit(id)
        permissions = SampleService.create()
        params = {
            'meta': {
                'data': {
                    'permissions': permissions
                }
            },
            'data': {
                'user': user
            }
        }
        return render(request, 'sample/edit.html', params)


    @api_view(['POST'])
    def update(request, id: int):
        """一件編集を実行.

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        try:
            name = request.POST['name']
            email = request.POST['email']
            birth_date = request.POST['birth_date']
            permission_id = request.POST['permission']

            params = {
                'name': name,
                'email': email,
                'birth_date': birth_date,
                'permission_id': permission_id
            }
            SampleService.update(id, params)
            return redirect(f'/sample/{id}/')
        except Exception as e:
            permissions = SampleService.create()
            params = {
                'meta': {
                    'data': {
                        'permissions': permissions
                    },
                    'error': str(e)
                },
                'data': {
                    'user': {
                        'id': id,
                        'name': name,
                        'email': email,
                        'birth_date': birth_date,
                        'permission_id': permission_id
                    }
                }
            }
            return render(request, 'sample/edit.html', params)


    @api_view(['POST'])
    def destroy(request, id: int):
        """一件削除を実行.

        Args:
            request ([type]): [description]
            id (int): primary_key
        """
        try:
            SampleService.destroy(id)
            return redirect('/sample/')
        except Exception as e:
            user = SampleService.show(id)
            params = {
                'error': str(e),
                'user': user
            }
            return render(request, 'sample/show.html', params)
