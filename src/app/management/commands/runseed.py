import random
from django.core.management.base import BaseCommand
from datetime import datetime
from django.contrib.auth.hashers import make_password
from faker import Faker

from app.orator.permission import Permission
from app.orator.user import User

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        fake = Faker('ja')
        Permission.insert([
            {
                'id': 1,
                'permission': 'administrator',

            },
            {
                'id': 2,
                'permission': 'user',

            },
        ])

        User.insert([
            {
                'id': i,
                'name': f'user{i}',
                'email': f'user{i}@gmail.com',
                'password': make_password(f'Password{i}'),
                'permission': 1 if i % 2 == 0 else 2,
                'birth_date': fake.date_between(start_date='-60y', end_date='-20y').isoformat(),
                'created_at': str(datetime.now()),
                'updated_at': str(datetime.now())
            }
            for i in range(1, 200)
        ])