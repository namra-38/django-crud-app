from django.db import models

# Create your models here.
class Employe(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    EMPLOYE_CHOICES = (
        ('Perminent', 'Perminent'),
        ('Contract Based', 'Contract Based'),
        ('Grass Sales', 'Grass Sales'),
        ('Weekly Based', 'Weekly Based')
    )
    name = models.CharField(max_length = 30, null=True, blank=True)
    email = models.CharField(max_length = 45, null=True, blank=True)
    pay = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length = 30, null=True, blank=True)
    mobile_no = models.CharField(max_length = 11, null=True, blank=True)
    gender = models.CharField(max_length = 6,  choices=GENDER_CHOICES, null=True, blank=True)
    employe_categories = models.CharField(max_length = 14, choices=EMPLOYE_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.name


