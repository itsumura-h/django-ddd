from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from app.domain.services.ddd_sample_service import DDDSampleService


class DDDSample:
    def index(request):
        users = DDDSampleService.index()
        users = [
            {
                'id': val['id'],
                'name': val['name'],
                'email': val['email'].get_label(),
                'permission': val['permission'].get_ja_label(),
                'age': val['birth_date_db'].get_age()
            }
            for val in users
        ]
        return JsonResponse({'value': users})


    def show(request, id):
        user, options = DDDSampleService.show(id)
        data = {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'].get_label(),
            'permission': user['permission'].get_ja_label(),
            'birth_date': user['birth_date_db'].get_str_number()
        }
        info = [
            {
                'id': val['id'],
                'permission': val['permission'].get_ja_label(),
            }
            for val in options
        ]
        return JsonResponse({'value': {'info': info, 'data': data}})

    def store(request, id):
        params = request.POST
        print(params)