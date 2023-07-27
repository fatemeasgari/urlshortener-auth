from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

#class s_l (models.Model):
#    full_link= models.CharField(max_length=200)
#    short_link=models.CharField(max_length=6)

#    def __str__(self):
#        return self.full_link
        
        

class full_link (models.Model):
    full_link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.full_link
        
    
class short_link (models.Model):
    full_id = models.ForeignKey (full_link, on_delete = models.CASCADE)
    short_link = models.CharField (max_length=6, unique=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # user_id = models.ForeignKey (User, on_delete = models.CASCADE) 
     
    def __str__(self):
        return f"{self.user_id} {self.short_link} {self.full_id}"
