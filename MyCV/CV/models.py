from django.db import models

# Create your models here.
class Person(models.Model):
    image         = models.ImageField(upload_to ='uploads/')
    name          = models.CharField(max_length=40)
    surname       = models.CharField(max_length=40)
    address       = models.CharField(max_length=100)
    email         = models.EmailField()
    description   = models.CharField(max_length=500)
    linkedin      = models.URLField()
    github        = models.URLField()
    youtube       = models.URLField()

    exp_title_1   = models.CharField(max_length=50)
    experience_1  = models.TextField()
    dur_exp_1     = models.CharField(max_length=40)

    exp_title_2   = models.CharField(max_length=50)
    experience_2  = models.TextField()
    dur_exp_2     = models.CharField(max_length=40)

    edu_title_1   = models.CharField(max_length=50)
    education_1   = models.TextField()
    dur_edu_1     = models.CharField(max_length=40)

    edu_title_2   = models.CharField(max_length=50)
    education_2   = models.TextField()
    dur_edu_2     = models.CharField(max_length=40)

    skill_1       = models.CharField(max_length=40)
    skill_2       = models.CharField(max_length=40)
    skill_3       = models.CharField(max_length=40)
    skill_4       = models.CharField(max_length=40)
    skill_5       = models.CharField(max_length=40)

    interests     = models.TextField()
