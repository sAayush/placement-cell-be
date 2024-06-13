
from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'job_type', 'company_name',
                  'salary', 'position', 'experience', 'skills', 'vacancy', 'posted_by', 'posted_at']
