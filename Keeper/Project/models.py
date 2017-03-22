from django.db import models
from django.utils import timezone
from Organizations.models import Organizations, Groups, Users
# Create your models here.


class Projects(models.Model):
    """
    The projects model
    """
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(blank=True, null=True)
    name = models.CharField("Project Name", max_length=150, blank=False)
    date = models.DateField("Completion Date", default=timezone.now, blank=True)
    project_image = models.ImageField("Project Image", blank=True, null=True,
                                      width_field="width_field", height_field="height_field",
                                      upload_to="Images/", default="Images/None/no-img.gif")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField('Project Description', blank=True, null=True)
    github_url = models.CharField("Github Repo Url", max_length=200, blank=True, null=True)
    groups = models.ManyToManyField(Groups, blank=True, default=None)
    organization = models.ForeignKey(Organizations, blank=False, null=False)
    users = models.ManyToManyField(Users, blank=True, default=None)


    def __str__(self):
        return self.name


class SubProject(models.Model):
    """
    The subproject model
    """
    name = models.CharField("Sub-project Name", max_length=200)
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(blank=True, null=True)
    date = models.DateField("Completion Date", default=timezone.now, blank=True)
    projects = models.ForeignKey(Projects, related_name='subprojects', blank=True, null=True)
    groups = models.ManyToManyField(Groups, blank=True, default=None)
    organization = models.ForeignKey(Organizations, blank=False)
    users = models.ManyToManyField(Users, blank=True, default=None)
    def __str__(self):
        return self.name

