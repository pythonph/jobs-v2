from django.db import models
from django.db.models.functions import Lower


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='case insensitive uniqueness check'
            ),
        ]

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    is_remote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    class Meta:
        ordering = ['-created_at']
