import datetime
import os
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible  # only if you need to support Python 2
class ChineseTable(models.Model):
    # ...
    title_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='caterlist/static')
    place_for_service_text = models.CharField(max_length=100)
    location_text = models.CharField(max_length=100)
    description_text = models.TextField()
    price_start_number = models.IntegerField(default=0)
    price_end_number = models.IntegerField(default=1)
    def __str__(self):
        return self.title_text
    def filename(self):
        return os.path.basename(self.image.url)

@python_2_unicode_compatible  # only if you need to support Python 2
class FoodImage(models.Model):
    chinesetable  = models.ForeignKey(ChineseTable, on_delete=models.CASCADE)
    foodImage = models.ImageField(upload_to='caterlist/static')
    foodImage_detail = models.CharField(max_length=10)
    def __str__(self):
        return self.foodImage_detail

@python_2_unicode_compatible  # only if you need to support Python 2
class SetMenu(models.Model):
    chinesetable  = models.ForeignKey(ChineseTable, on_delete=models.CASCADE)
    setMenu_number = models.CharField(max_length=5)
    setMenu_price = models.IntegerField(default=1)
    setMenu_name = models.CharField(max_length=100)
    setMenu_detail = models.TextField()
    def __str__(self):
        return self.setMenu_name
    

