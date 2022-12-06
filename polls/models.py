import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    qusetion = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# Create your models here.

#https://docs.djangoproject.com/ko/4.1/intro/tutorial02/ 여기 부분 에러

# Create three choices.
#>>> q.choice_set.create(choice_text='Not much', votes=0)
#<Choice: Not much>
#>>> q.choice_set.create(choice_text='The sky', votes=0)
#<Choice: The sky>
#>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
