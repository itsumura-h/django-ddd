from django.core.management.base import BaseCommand
import re
import os


class Command(BaseCommand):
    help = 'Oratorのクラスを作ります。引数は頭文字大文字の英単語単数形で入力してください'

    def add_arguments(self, parser):
        parser.add_argument('Model', nargs='+')

    def handle(self, *args, **options):
        Model = options['Model'][0]
        model = Model.lower()

        # ==================== create model ====================
        model_path = f'app/orator/{Model}.py'
        content = f'''from . import Model

class {Model}(Model):
    __table__ = '{model}s' #DB内の実際のテーブル名を設定
    __timestamps__ = False #created_atとupdated_atを無効にするオプション
'''

        # ファイルが存在していたらエラー
        if os.path.exists(model_path):
            print(f'{model_path}は既に存在しています')
        else:
            with open(model_path, 'w') as f:
                f.write(content)
            print(f'{model_path}が作成されました')
