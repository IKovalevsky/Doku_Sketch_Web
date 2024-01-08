from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)
    title = models.CharField(max_length= 15)
    description = models.TextField(null= True, blank=True)
    complete = models.BooleanField(default= False)
    time_created = models.DateTimeField(auto_now_add= True)
    file_task = models.FileField(blank=True, upload_to="uploads/%Y/%m/%d/")

    def __str__(self) -> str:
        return self.title

    class Meta:
        order_with_respect_to = 'user'
