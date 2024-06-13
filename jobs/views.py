from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsOrganization


class JobPostCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganization]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
