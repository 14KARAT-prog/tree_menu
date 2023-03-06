from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name="Item title")
    parent = models.ForeignKey('self', blank=True, null=True, related_name="childrens", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Heroes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title