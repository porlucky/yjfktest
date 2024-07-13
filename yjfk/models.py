from django.db import models


# Create your models here.
class YJFKUser(models.Model):
    id = models.AutoField(primary_key=True)  # 默认就是自增的
    user_name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)  # 自动设置为当前时间
    item = models.CharField(max_length=50)  # 自动设置为当前时间
    user_id = models.BigIntegerField()
    add_datetime = models.DateTimeField()

    class Meta:
        db_table = 'yjfk_user'
