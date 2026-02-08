from datetime import timedelta

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return f"{self.id}. {self.question_text} - {self.pub_date.date()}"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days = 1)
    
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("published date")
    
class Choice(models.Model):
    def __str__(self):
        return f"{self.choice_text} - {self.votes} votes"
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
