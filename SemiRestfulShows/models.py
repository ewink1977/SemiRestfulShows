from django.db import models
from datetime import date, datetime

class ShowValidation(models.Manager):
    def basicvalidator(self, postData):
        # Since the edit page allows blank entries, we need to verify each entry has data before
        # we run the validation statements, otherwise we'd have to write a different, mostly duplicate
        # validation function for both the ADD SHOW and EDIT SHOW pages.
        errors = {}
        if postData['showtitle']:
            dupcheck = Shows.objects.all()
            if len(postData['showtitle']) < 2:
                errors['showtitle'] = "Show title must be at least 2 characters long."
            for check in dupcheck:
                if postData['showtitle'] == check.title:
                    errors['showtitle'] = "Show title must be unique."
        if postData['shownet']:
            if len(postData['shownet']) < 3:
                errors['shownet'] = "Network name must be at least 3 characters (for 2 character network, add 'The' - e.g. 'The WB')."
        if postData['showreldate']:
            # Magic to make the date comparison work.
            dateentered = postData['showreldate']
            reldate = datetime.strptime(dateentered, "%Y-%m-%d")
            today = datetime.now()
            if reldate >= today:
                errors['showreldate'] = "The release date must be in the past."
        if postData['showdesc']:
            if len(postData['showdesc']) < 10:
                errors['showdesc'] = "Descriptions must be at least 10 characters."
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowValidation()
