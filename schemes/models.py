from django.db import models


class Scheme(models.Model):

   OCCUPATION_CHOICES = [
    ('', 'Any'),
    ('Farmer', 'Farmer'),
    ('Student', 'Student'),
    ('Salaried Employee', 'Salaried Employee'),
    ('Self-employed', 'Self-employed'),
    ('Unemployed', 'Unemployed'),
    ('Homemaker', 'Homemaker'),
    ('Retired', 'Retired'),
    ('Widow', 'Widow'),
    ('Disabled', 'Disabled'),
 ]

   name = models.CharField(max_length=200)

   state = models.CharField(max_length=100)
   
   minimum_age = models.IntegerField(default=0)

   maximum_income = models.IntegerField(
        null=True,
        blank=True
    )

   required_occupation = models.CharField(
        max_length=50,
        choices=OCCUPATION_CHOICES,
        blank=True
    )

   disability_required = models.BooleanField(default=False)

   widow_required = models.BooleanField(default=False)

   description = models.TextField()
    
   official_link = models.URLField(blank=True)
    

   def __str__(self):
        return self.name