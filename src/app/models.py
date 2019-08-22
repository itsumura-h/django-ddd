from django.db import models

# Create your models here.


class Permission(models.Model):
    def __str__(self):
        return str(self.permission)

    permission = models.CharField(max_length=255)

    class Meta:
        db_table = 'permissions'
        verbose_name_plural = 'Permissions'


class User(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
