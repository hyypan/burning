# coding: utf-8
from django.contrib.auth.models import AbstractUser, UserManager, User as U, Permission as P
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.FileField()

    class Meta:
        db_table = 'user'


class UserPermissions(models.Model):
    user = models.ForeignKey(User)
    permission = models.ForeignKey(P)

    class Meta:
        db_table = 'user_user_permissions'


class Belongs(BaseModel):
    comments = models.CharField(help_text='评论', max_length=256)
    views = models.IntegerField(help_text='浏览次数', default=0)
    loves = models.IntegerField(help_text='赞次数', default=0)

    class Meta:
        db_table = 'yp_belongs'


class Articles(BaseModel):
    title = models.CharField(verbose_name=u'文章标题', max_length=256, default='')
    content = models.TextField()
    belongs = models.ForeignKey(Belongs)

    class Meta:
        db_table = 'yp_articles'
