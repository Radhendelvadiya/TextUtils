from django.db import models


# create your model here
class FeedBack(models.Model):
    email = models.EmailField()
    feedback = models.TextField()

    class Meta:
        app_label = 'textutils'
