from django.db import models
from datetime import date

class Show_Validation(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title must be at least 2 characters long."
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters (for 2 character network, add 'The' - e.g. 'The WB')."
        if postData['release_date'] >= date.today():
            errors['release_date'] = "The release date must be in the past."
        if postData['description']:
            if len(postData['description']) < 10:
                errors['description'] = "Descriptions must be at least 10 characters."
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Show_Validation()
