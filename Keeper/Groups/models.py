from django.db import models
from Organizations.models import Organizations
# Create your models here.
class Groups(models.Model):
    project_image = models.ImageField("Group Logo", blank=True, null=True,
                                      width_field="width_field", height_field="height_field",
                                      upload_to="Images/Groups", default="Images/None/no-img.gif")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    name = models.CharField("Group Name", max_length=150, blank=False, null=False, default=None)
    description = models.TextField("Group Description")
    organizations = models.ForeignKey(Organizations, related_name='Organization')

    def __str__(self):
        return self.name