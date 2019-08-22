import json
from django.core.management.base import BaseCommand
from datetime import datetime
from django.contrib.auth.hashers import make_password
from faker import Faker


class Command(BaseCommand):
    help = 'dataに配列を作ってね！app/fixtures/seed.jsonが出力されるよ！'

    def handle(self, *args, **options):
        fake = Faker()

        permission = [
            {
                'model': 'app.permission',
                'pk': 1,
                'fields': {
                    'permission': 'administrator'
                }
            },
            {
                'model': 'app.permission',
                'pk': 2,
                'fields': {
                    'permission': 'user'
                }
            },
        ]

        user = [
            {
                'model': 'app.user',
                'pk': i,
                'fields': {
                    'name': f'user{i}',
                    'email': f'user{i}@gmail.com',
                    'password': make_password(f'Password{i}'),
                    'birth_date': fake.date_between(start_date='-60y', end_date='today').isoformat(),
                    'permission': 1 if i % 2 == 0 else 2,
                    'created_at': str(datetime.now()),
                    'updated_at': str(datetime.now())
                }
            } for i in range(1, 200)
        ]

        data = permission + user

        # 自由に作って
        # data = {

        # }

        seeder_path = 'app/fixtures/seed.json'
        with open(seeder_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
