from distutils.command.upload import upload
from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class bash_video(models.Model):
    video=models.FileField(upload_to='videos')

class yurtlar(models.Model):
    at_tm=models.CharField(max_length=50)
    at_ru=models.CharField(max_length=50,default=1)
    at_en=models.CharField(max_length=50,default=1)

    
    def __str__(self):
        return self.at_tm
    
    class Meta:
        ordering=['at_tm']

class uniwersitetler(models.Model):
    at_tm=models.CharField(max_length=200)
    at_ru=models.CharField(max_length=200)
    at_en=models.CharField(max_length=200)
    yurt=models.ForeignKey(yurtlar,on_delete=models.CASCADE)
    surat=models.FileField(upload_to="images")
    link=models.URLField()

    def __str__(self):
        return self.at_tm

    class Meta:
        ordering=['at_tm']

class Teswir(models.Model):
    at=models.CharField(max_length=50)
    uniwersitet=models.ForeignKey(uniwersitetler,on_delete=models.CASCADE)
    beyan=models.TextField()
    wagt=models.DateField()

    def __str__(self):
        return str(self.at)

class register(models.Model):
    at=models.CharField(max_length=50)
    gmail=models.EmailField()
    parol=models.CharField(max_length=8)
    phone=PhoneNumberField()

    def __str__(self):
        return self.at

class news(models.Model):
    title_tm=models.CharField(max_length=100)
    title_ru=models.CharField(max_length=100)
    title_en=models.CharField(max_length=100)
    surat=models.ImageField(upload_to='news_images')
    beyan_tm=models.TextField()
    beyan_ru=models.TextField()
    beyan_en=models.TextField()

    wagt=models.DateField()

    def __str__(self):
        return self.title_tm