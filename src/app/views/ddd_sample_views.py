from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from app.domain.services.ddd_sample_service import DDDSampleService


class DDDSample:
    @api_view(['GET'])
    def index(request):
        users = DDDSampleService.index()
        users = [
            {
                'id': val['id'],
                'name': val['name'],
                'email': val['email'].get_label(),
                'permission': val['permission_en'].get_ja_label(),
                'age': val['birth_date_db'].get_age()
            }
            for val in users
        ]
        return JsonResponse({'value': users})

    @api_view(['GET'])
    def show(request, id):
        user, options = DDDSampleService.show(id)
        data = {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'].get_label(),
            # 'permission': {
            #     'key': user['permission_id'],
            #     'value': user['permission_en'].get_ja_label(),
            # },
            'permission_id': user['permission_id'],
            'permission': user['permission_en'].get_ja_label(),
            'birth_date': user['birth_date_db'].get_str_number()
        }
        info = [
            {
                'permission_id': val['id'],
                'permission': val['permission_en'].get_ja_label(),
            }
            for val in options
        ]
        return JsonResponse({
            'value':{
                'meta': {
                    'display': info # 表示に必要なデータ
                },
                'data': data # 実際のデータ
            }
        })

    @api_view(['PUT'])
    def update(request, id):
        params = request.data
        print(params)
        try:
            result = DDDSampleService.update(id, params)
            return JsonResponse({'value': {'result': result}})
        except Exception as e:
            return JsonResponse({'value': {'status': str(e)}})