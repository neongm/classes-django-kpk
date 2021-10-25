from django.db import models

# Create your models here.

class Record(models.Model):
    # id = models.AutoField(primary_key=True)
    author_name = models.CharField('author name', max_length=100, default="None")
    record_title = models.CharField('record title', max_length=200)
    record_text = models.TextField('recoed text')
    
    def __str__(self):
        return self.record_title
