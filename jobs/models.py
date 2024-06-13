from django.db import models
from accounts.models import CustomUser


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)
    position = models.CharField(max_length=255)
    experience = models.IntegerField(default=0)
    skills = models.TextField()
    vacancy = models.IntegerField(default=1)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
