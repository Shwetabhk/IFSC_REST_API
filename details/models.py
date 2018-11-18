from django.db import models


class Bank(models.Model):
    ifsc = models.CharField(max_length=35, null=False)
    bank_id = models.IntegerField(null=False)
    branch = models.CharField(max_length=35, null=False)
    address = models.CharField(max_length=150,null=False)	
    city = models.CharField(max_length=50, null=False)
    district = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=35, null=False)
    bank_name = models.CharField(max_length=100, null=False)
