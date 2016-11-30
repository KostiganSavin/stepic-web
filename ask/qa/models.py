from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(default=datetime.date.today())
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

    def new(self):
        return self.filter(added_at=datetime.date.today())

    def popular(self):
        return self.order_by('rating')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
