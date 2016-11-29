from django.db import models
from django.contrib.auth.models import User
import date

# Create your models here.
Class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(balnk=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

    def new(self):
        return self.filter(added_at=date(date.date(now)))

    def popular(self):
        return self.order_by('rating')


Class Answer(models.Model):
    text = models.TetxField()
    added_at = models.DateField()
    question = ForeignKey(Question)
    author = models.ForeignKey(User)
