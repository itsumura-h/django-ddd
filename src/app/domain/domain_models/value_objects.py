import re
from datetime import date, datetime
import math


class EmailValueObject:
    def __init__(self, value):
        EMAIL_REGEX = re.compile(
            r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'
        )
        if not EMAIL_REGEX.match(value):
            raise Exception(f'「{value}」のメールアドレスの形式が正しくありません')
        else:
            self.__value = value

    def get_label(self):
        return self.__value


class PermissionValueObject:
    def __init__(self, value):
        self.__value = value

    def get_ja_label(self):
        """権限の日本語名を返すメソッド.

        Returns:
            str -- 権限の日本語名
        """
        if self.__value == 'administrator':
            return '管理者'
        elif self.__value == 'user':
            return '一般'

    def get_en_label(self):
        """権限の英語名を返すメソッド.

        Returns:
            str -- 権限の英語名
        """
        return self.__value


class DatetimeValueObject:
    def __init__(self, value):
        if isinstance(value, str):
            # 整形
            value = value.split('+')[0]
            self.__value = datetime.strptime(
                value,
                '%Y-%m-%dT%H:%M:%S.%f'
            )
        elif isinstance(value, datetime):
            self.__value = value

    def get_datetime(self):
        return self.__value

    def get_label(self):
        return self.__value.isoformat()


class BirthdateValueObject:
    """生年月日クラス:date/8文字のstr."""

    def __init__(self, value):
        if isinstance(value, date):
            self.__value = value
        elif isinstance(value, str):
            # 8文字の数字
            repattern = re.compile(r'[0-9]{8}')
            is_match = repattern.match(value)
            if not (is_match and len(value) == 8):
                raise Exception(f'{value}は8文字の数字ではありません')

            y = int(value[0:4])
            m = int(value[4:6])
            d = int(value[6:8])
            self.__value = date(y, m, d)

    def get_date(self):
        return self.__value.isoformat()

    def get_str_number(self):
        y = str(self.__value.year)
        m = str(self.__value.month).zfill(2)
        d = str(self.__value.day).zfill(2)
        return f'{y}{m}{d}'

    def get_age(self):
        today = date.today()
        diff_days = (today - self.__value).days
        diff_year = math.floor(diff_days / 365)
        return diff_year


class BirthdateDBValueObject:
    def __init__(self, value):
        if isinstance(value, str):
            self.__value = datetime.strptime(value, '%Y-%m-%d')

    def get_date(self):
        return self.__value.isoformat()

    def get_str_number(self):
        y = str(self.__value.year)
        m = str(self.__value.month).zfill(2)
        d = str(self.__value.day).zfill(2)
        return f'{y}{m}{d}'

    def get_age(self):
        today = datetime.today()
        diff_days = (today - self.__value).days
        diff_year = math.floor(diff_days / 365)
        return diff_year

class BirthdateInputValueObject:
    def __init__(self, value):
        self.__value = value