from django.db import models
from django.contrib.auth.models import User


class ExtendUser(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=15, blank=True)

    def __reper__(self):
        return f'{self.mobile}'
