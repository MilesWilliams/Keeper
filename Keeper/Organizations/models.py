from django.db import models
from django.utils import timezone

# Create your models here.
class Organizations(models.Model):
    """
    Organization model
    """
    project_image = models.ImageField("Organization Logo", blank=True, null=True,
                                      width_field="width_field", height_field="height_field",
                                      upload_to="Images/", default="Images/None/no-img.gif")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    name = models.CharField("Organization Name", max_length=150, blank=False, null=False,
                            default=None)
    description = models.TextField()
    created_on = models.DateField("Created on", default=timezone.now)

    def __str__(self):
        return self.name
