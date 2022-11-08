from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User,auth

# from viewflow.fields import CompositeKey

# Create your models here.
my_choices=(
    ('Easy','Easy'),
    ('Intemediate','Intermediate'),
    ('Hard','Hard')
)
class Web_Challenges(models.Model):
    Challenge_ID=models.CharField(max_length=8 ,primary_key=True) 
    Challenge_Name=models.CharField(max_length=50)
    Challenge_Discription=models.TextField()
    Challenge_Points=models.IntegerField()
    Challenge_Difficulty=models.CharField(max_length=13,choices=my_choices)
    Challenge_Answer=models.TextField()
    Challenge_Ratings=models.IntegerField(default=3)
    
class Web_Challenges_solve(models.Model):
    Username=models.CharField(max_length=25 )
    Challenge_id=models.CharField(max_length=8)





