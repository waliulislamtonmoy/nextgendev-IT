from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    subtitle = models.TextField(blank=True,null=True)
    call_to_action_text = models.CharField(max_length=100,blank=True,null=True)
    call_to_action_url = models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to="homepage/", blank=True,null=True)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title