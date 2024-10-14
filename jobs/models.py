from django.db import models
from users.models import CustomUser

class Job(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateTimeField()

class Bid(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 1})
    proposal = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
