from django.db import models

# Create your models here.
class Grade(models.Model):
    ganme=models.CharField(max_length=20)
    gstudentnum = models.IntegerField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()

class StoreInfo(models.Model):
    name = models.CharField(max_length=20, default='') #name属性，字段
    address = models.CharField(max_length=50, default="China") #address属性，字段

    #此方法在print对象的时候，可以打印字符串，类似java中的toString()方法
    def __str__(self):
        return self.name + self.address