from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class MobileModel(models.Model):
    brand =models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    color = models.TextField()
    order=tinymce_models.HTMLField(default="")
    # description =models.CharField(max_length=50)
class News(models.Model):
    news_title= models.CharField(max_length=50)
    news_description = tinymce_models.HTMLField(default="")

    # image = models.ImageField(upload_to="uploads", height_field=None, width_field=None, max_length=100,default=None)
