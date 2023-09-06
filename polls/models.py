import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class NewModel(models.Model):        
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=200)
    field2 = models.IntegerField(default=0)
    field3 = models.TextField(max_length= 500)
    field4 = models.CharField(max_length=200)
    field5 = models.IntegerField(default=0)
    field6 = models.TextField(max_length= 500)
    field7 = models.CharField(max_length=200)
    field8 = models.IntegerField(default=0)
    field9 = models.TextField(max_length= 500)
