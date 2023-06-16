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
    likes = models.ManyToManyField(User, related_name='game_likes', blank=True)


class Meta:
    ordering = ['-created_on']


def __str__(self):
    return self.title


def number_of_likes(self):
    return self.likes.count()


class comments(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DataTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField()


class Meta:
    ordering = ["created_on"]


def __str__(self):
    return f"comment {self.content} by {self.name}"

# Create your models here.
