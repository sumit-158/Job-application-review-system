from datetime import datetime
from django.db import models


class Applicant(models.Model):
    """
    For crating model in the database
    """

    def nameFile(instance, filename):
        return "_".join([str(instance.first_name + "_" + instance.last_name), filename])

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=500)
    apply_date = models.DateTimeField(default=datetime.now, blank=True)
    resume = models.FileField(upload_to=nameFile, null=True)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        template = "{0.first_name} {0.last_name}"
        return template.format(self)
