from rest_framework.serializers import ModelSerializer, StringRelatedField, ImageField

from Project.models import Projects, SubProject
from Tasks.api.serializers import TasksSerializer

class SubProjectSerializer(ModelSerializer):
    """
    The SubProject model serializer
    """
    subprojecttasks = TasksSerializer(many=True, read_only=False)
    class Meta:
        """
        The SubProject model fields
        """
        model = SubProject
        fields = (
            'id',
            'completed',
            'completed_on',
            'name',
            'date',
            'projects',
            'subprojecttasks',
        )

class ProjectsSerializer(ModelSerializer):
    """
    The todo projects serializer
    """
    project_image = ImageField(max_length=None, use_url=True)
    subprojects = SubProjectSerializer(many=True, read_only=False)
    projecttasks = TasksSerializer(many=True, read_only=False)
    class Meta:
        """
        The Project model fields
        """
        model = Projects
        fields = (
            'id',
            'name',
            'completed',
            'completed_on',
            'date',
            'project_image',
            'description',
            'subprojects',
            'projecttasks',
            'github_url',
        )
