import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'マイグレーション履歴の削除、マイグレーションファイルの再生成、seed再生成、seeder実行をするコマンド'

    def handle(self, *args, **options):
        subprocess.call(['python', 'manage.py', 'migrate', 'app', 'zero'])
        subprocess.call(['rm', '-fr', 'app/migrations'])
        subprocess.call(['mkdir', 'app/migrations'])
        subprocess.call(['touch', 'app/migrations/__init__.py'])
        subprocess.call(['python', 'manage.py', 'makemigrations'])
        subprocess.call(['python', 'manage.py', 'migrate'])
        subprocess.call(['python', 'manage.py', 'make_seed'])
        subprocess.call(['python', 'manage.py', 'loaddata', 'seed.json'])
