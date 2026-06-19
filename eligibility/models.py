from django.db import models


class EligibilitySearch(models.Model):

    state = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Eligibility Search"
        verbose_name_plural = "Eligibility History"

    def __str__(self):
        return f"{self.state} - {self.occupation}"