from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    coreatedDate = models.DateTimeField(auto_now_add=True)
    timeField = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)], null=True, blank=True)
    timeTotal = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ["completed"]