from rest_framework.generics import (
		CreateAPIView,
		DestroyAPIView,
		ListAPIView,
		UpdateAPIView,
		RetrieveAPIView,
	)

from .serializers import TasksSerializer, ImageSerializer
from Tasks.models import Tasks, Images

class TaskCreateView(CreateAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

class TaskDeleteView(DestroyAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

class TaskDetailView(RetrieveAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

class TaskListApiView(ListAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

class TaskUpdateApiView(UpdateAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

class ImageUploadView(CreateAPIView):
	queryset = Images.objects.all()
	serializer_class = ImageSerializer

class ImageDeleteView(DestroyAPIView):
	queryset = Images.objects.all()
	serializer_class = ImageSerializer

class ImageDetailView(RetrieveAPIView):
	queryset = Images.objects.all()
	serializer_class = ImageSerializer
	