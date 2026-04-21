
from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models
from bson import ObjectId


    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


    # Use default Django User model. Team will be stored as a CharField on User via profile or directly in test data.


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


    name = models.CharField(max_length=100)
    description = models.TextField()


    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.PositiveIntegerField()
