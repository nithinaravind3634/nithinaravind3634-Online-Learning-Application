from django.db import models


# Create your models here.
class teachermodel(models.Model):
    teacherusername=models.CharField(max_length=20)
    teacheremail=models.EmailField()
    teacherphone=models.CharField(max_length=10)
    teacherpassword=models.CharField(max_length=20)
  


class studentmodel(models.Model):
    studentusername=models.CharField(max_length=20)
    studentemail=models.EmailField()
    studentphone=models.CharField(max_length=10)
    studentpassword=models.CharField(max_length=20)


class postvideomodel(models.Model):
    teachername=models.CharField(max_length=20)
    videotopic=models.CharField(max_length=20)
    videodescription=models.TextField()
    videoupload = models.FileField(upload_to='videos/',blank=True, null=True)

class postfilemodel(models.Model):
    teachername=models.CharField(max_length=20)
    filetopic=models.CharField(max_length=20)
    filedescription=models.TextField()
    fileupload = models.FileField(upload_to='files/',blank=True, null=True)
    filethumbnail=models.FileField(upload_to='images/',blank=True,null=True)
    

class responsemodel(models.Model):
    username=models.CharField(max_length=20)
    response=models.TextField()
    teachername=models.CharField(max_length=20)
    videotopic=models.CharField(max_length=20)
    videodescription=models.TextField()