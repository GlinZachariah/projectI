from django.db import models

# Create your models here.
class Branch(models.Model):
    branch= models.CharField(max_length=3, primary_key=True)
    sub1_name = models.CharField(max_length=10)
    sub2_name = models.CharField(max_length=10)
    sub3_name = models.CharField(max_length=10)
    sub4_name = models.CharField(max_length=10)
    sub5_name = models.CharField(max_length=10)
    sub6_name = models.CharField(max_length=10)
    sub7_name = models.CharField(max_length=10)
    sub8_name = models.CharField(max_length=10)
    sub9_name = models.CharField(max_length=10)
    sub10_name = models.CharField(max_length=10)
    sub11_name = models.CharField(max_length=10)
    sub12_name = models.CharField(max_length=10)
    sub13_name = models.CharField(max_length=10)

    def __str__(self):
        return self.branch

class Result(models.Model):
    reg_no = models.CharField(max_length=10, primary_key=True)
    branch= models.ForeignKey(Branch, on_delete=models.CASCADE)
    sub1 = models.CharField(max_length=10)
    sub2 = models.CharField(max_length=10)
    sub3 = models.CharField(max_length=10)
    sub4 = models.CharField(max_length=10)
    sub5 = models.CharField(max_length=10)
    sub6 = models.CharField(max_length=10)
    sub7 = models.CharField(max_length=10)
    sub8 = models.CharField(max_length=10)
    sub9 = models.CharField(max_length=10)
    sub10 = models.CharField(max_length=10)
    sub11 = models.CharField(max_length=10)
    sub12 = models.CharField(max_length=10)
    sub13 = models.CharField(max_length=10)

    def __str__(self):
        return self.reg_no
