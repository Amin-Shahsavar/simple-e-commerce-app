from django.db import models
from django.utils.translation import gettext_lazy as _


class Auther(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=256)
    email = models.EmailField(_("Email"), max_length=256, unique=True)
    birth_date = models.DateField(_("Date of Birth"))

    def __str__(self):
        return self.full_name

    # class Meta:
    #     ordering = ['full_name']
