from django.db import models

# Create your models here.
class Tasks(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    STATUS_CHOICES = (
        ('PENDING','pending'),
        ('COMPLETE','complete'),
        ('CANCELED','canceled')
        )
    Status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='PENDING')
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Name