from django.db import models
from user.models import Member


class Media(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Board(models.Model):
    b_title = models.CharField(max_length=50)
    b_content = models.CharField(max_length=200)
    b_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    # b_like = models.IntegerField(default=0)
    b_like = models.ManyToManyField(Member,related_name='likes', blank=True)
    b_date = models.DateTimeField(auto_now=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return self.b_title


class Comment(models.Model):
    c_content = models.CharField(max_length=50)
    c_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    c_board = models.ForeignKey(Board, on_delete=models.CASCADE)
    c_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.c_content
