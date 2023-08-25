from django.db import models
from user_api.models import AppUser

class Collection(models.Model):

    col_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(AppUser, related_name='collection', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Story(models.Model):
    st_id = models.AutoField(primary_key=True)
    name = models.TextField()
    user_input = models.TextField(default='')
    generated_context = models.TextField(default='')
    collection = models.ForeignKey(Collection, related_name='stories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

