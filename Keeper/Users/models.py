from django.db import models
from Organizations.models import Organizations
from Groups.models import Groups
# Create your models here.

class Users(models.Model):
    """
    Custom user model
    """
    first_name = models.CharField("First Name", max_length=150, default=None)
    last_name = models.CharField("Surname", max_length=200, default=None)
    project_image = models.ImageField("Avatar", blank=True, null=True,
                                      width_field="width_field", height_field="height_field",
                                      upload_to="Images/Avatars", default="Images/None/no-img.gif")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    organizations = models.ForeignKey(Organizations, related_name="Organization_Users")
    groups = models.ForeignKey(Groups, related_name="Group_Users")
    password = models.CharField('Password', max_length=20, default='password')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
