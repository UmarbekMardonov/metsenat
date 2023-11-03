from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel


class HolatiChoice(models.TextChoices):
    yangi = 'YANGI'
    bekor_qilingan = 'BEKOR QILINGAN'
    modiratsiya = 'MODIRATSIYADA'


class Sponsor(BaseModel):
    type = models.BooleanField(default=False)  # False is Jismoniy
    full_name = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    used_amount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=HolatiChoice.choices, default=HolatiChoice.modiratsiya
    )
    office_name = models.CharField(max_length=220, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-id']
