from django.db import models

# Create your models here.
class Items(models.Model):
    #def __str__(self):
       # return self.item_name
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000,default='https://th.bing.com/th?id=OIP.fCc7R9uBPn0l4vJUjQihFAHaH_&w=240&h=259&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2')

