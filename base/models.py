from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Topic table
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Room table
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null for database and blank for from (ui)
    # participants = 
    updated = models.DateField(auto_now=True)     # it takes time every time (to get last time it updated)
    created = models.DateField(auto_now_add=True) # it takes time when we created (only at the first time)

    class Meta:
        ordering = ['-id'] # descending order by id

    def __str__(self):
        return str(self.name)
    
# Message table
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # one to many relationship (CASCADE means delete all the message if the Room was deleted)
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
