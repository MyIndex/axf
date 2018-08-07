from django.db import models

# Create your models here.
class axf_wheel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_wheel'
