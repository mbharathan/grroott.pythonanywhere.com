from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, default=None, blank=True, related_name = 'followed')
    bio = models.TextField(default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def num_follows(self):
        return self.followed.all().count()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

FOLLOW_CHOICES = (

('Follow', 'Follow'),
('Following', 'Following'),

)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    follow_value = models.CharField(choices= FOLLOW_CHOICES,default='Follow', max_length=10)


    def __str__(self):
        return str(self.profile)
        

class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    your_feedback = models.TextField()

    def __str__(self):
        return f'{self.subject}'
