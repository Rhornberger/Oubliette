from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='vegvisir.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} {self.img} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.img.path) 