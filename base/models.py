from uuid import uuid4
from django.db import models

class Board(models.Model):
    # author =
    # city =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # members = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=True)
    
    def __str__(self):
        return self.name