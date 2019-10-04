import json
from datetime import date
from django.shortcuts import redirect, render
from app.orator.user import User


class WebSampleViews:
    def index(request):
        return render(request, 'web_sample/index.html')

    def vue_installed(request):
        users = json.dumps(User.select(
            'id', 'name', 'email').get().serialize())
        headers = json.dumps([
            {'text': 'id', 'value': 'id'},
            {'text': 'name', 'value': 'name'},
            {'text': 'email', 'value': 'email'},
        ])
        return render(request, 'web_sample/vue_installed.html', {'users': users, 'headers': headers})

    def checkform(request):
        check_result = {
            'standard': [
                {
                    'facility': '供給ポンプ\nCP2-1~CP2-7\nH2-1~HP2-6',
                    'check': [
                        {'name': '吐出圧力の確認', 'status': 0},
                        {'name': '電流値の確認', 'status': 1},
                        {'name': '異音の確認', 'status': 2},
                        {'name': '振動の有無', 'status': 3},
                        {'name': '外観の以上の確認', 'status': 0}
                    ]
                },
            ],
            'except': [
                {
                    'facility': '冷却塔\n冷却加熱塔\nCT-1,CHT-1,CHT-2',
                    'check': [
                        {'name': '散水状況の確認', 'status': 0},
                        {'name': '飛散の有無', 'status': 0}
                    ]
                },
                {
                    'facility': '供給系ストレーナ',
                    'check': [
                        {'name': '差圧の有無', 'status': 0}
                    ]
                }
            ],
            'note': '特記事項の内容'
        }

        

        
        return render(request, 'web_sample/checkform.html', {
            'check_result': check_result
        })
