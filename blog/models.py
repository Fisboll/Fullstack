from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
SUBGENRES = (
    (0, 'Strategy'), (1, 'Survival and horror'), (2, 'Fantasy'), (3, 'Sci-Fi'),
    (4, 'Action-adventure'), (5, 'Comedy'), (7, 'Cyberpunk'),
    (8, 'Apocalyptic'), (9, 'MMORPG'))


class post(models.Model):
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='game_posts')
    content = models.TextField(max_length=2000)
    image = CloudinaryField('image', default='placeholder')
    comments = models.BigIntegerField()
    game = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

# Create your models here.
