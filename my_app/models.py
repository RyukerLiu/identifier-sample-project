from django.db import models

class Sample(models.Model):
    filed_x = models.CharField(max_length=128, null=True)
    filed_y = models.CharField(max_length=128, null=True)
    filed_z = models.CharField(max_length=128, null=True)
    filed_other = models.CharField(max_length=128, null=True)

    class Meta(object):
        unique_together = [
            ["filed_x", "filed_y"]
        ]