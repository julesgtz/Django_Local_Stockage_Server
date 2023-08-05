from django.db import models

class Files(models.Model):
    name = models.CharField(max_length=40)
    file = models.FileField(upload_to='uploads/')
    ip = models.GenericIPAddressField(null=True, blank=True)
    user = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def dico(self):
        return {"name":self.name, "file":self.file.name, "ip": self.ip, "user": self.user}