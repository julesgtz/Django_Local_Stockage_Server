from django.db import models
import os
class Files(models.Model):
    file = models.FileField(upload_to='media/')
    ip = models.GenericIPAddressField(null=True, blank=True)
    user = models.CharField(max_length=40,null=True, blank=True)

    def filename(self):
        return os.path.basename(self.file.name)