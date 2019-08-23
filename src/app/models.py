from django.db import models

# Create your models here.


class SamplePermission(models.Model):
    def __str__(self):
        return str(self.permission)

    permission = models.CharField(max_length=255)

    class Meta:
        db_table = 'sample_permissions'  # テーブル名
        verbose_name_plural = 'SamplePermissions'  # 複数形の時の名前


class SampleUser(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    permission = models.ForeignKey(SamplePermission, on_delete=models.PROTECT)
    birth_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'sample_users'
        verbose_name_plural = 'SampleUsers'
