from rest_framework.generics import (
	   DestroyAPIView,
	   ListAPIView,
	   UpdateAPIView,
	   RetrieveAPIView,
	   CreateAPIView,
	)
from Project.models import Projects, SubProject
from .serializers import ProjectsSerializer, SubProjectSerializer


class ProjectsCreateView(CreateAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer

class ProjectsDeleteView(DestroyAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer

class ProjectsDetailView(RetrieveAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer

class ProjectsListView(ListAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer

class ProjectsUpdateView(UpdateAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer


class SubProjectCreateView(CreateAPIView):
	queryset = SubProject.objects.all()
	serializer_class = SubProjectSerializer

class SubProjectDeleteView(DestroyAPIView):
	queryset = SubProject.objects.all()
	serializer_class = SubProjectSerializer

class SubProjectListView(ListAPIView):
	queryset = SubProject.objects.all()
	serializer_class = SubProjectSerializer

class SubProjectUpdateView(UpdateAPIView):
	queryset = SubProject.objects.all()
	serializer_class = SubProjectSerializer