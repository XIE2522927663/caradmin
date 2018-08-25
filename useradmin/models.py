from django.db import models
from django.utils.timezone import now

# Create your models here.
class User (models.Model):
    # TYPE = (
    #     ('A', '产品组')
    #     ('B', '客服组')
    #     ('C', '推广组')
    #     ('D', '调度组')
    #     ('E', '财务组')
    #     ('F', '理赔')
    # )
    name = models.CharField('登录账号', max_length=20)
    createTime = models.DateTimeField('创建时间', default=now)
    password = models.CharField('密码', max_length=20)
    active = models.BooleanField('是否激活', default=True)
    type = models.CharField('用户组', max_length=30)

    def __str__(self):
        return self.name