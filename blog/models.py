from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
SUBGENRES = (
    (0, 'Strategy'), (1, 'Survival and horror'), (2, 'Fantasy'), (3, 'Sci-Fi'),
    (4, 'Action-adventure'), (5, 'Comedy'), (7, 'Cyberpunk'),
    (8, 'Apocalyptic'), (9, 'MMORPG'))


class game(models.Model):
    name = models.CharField(50)
    platform = models.CharField(100)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(2000)
    release_date = models.DateTimeField(setattr)
    posts = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='game_posts')


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
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class comments(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.content} by {self.name}"


class UserProfile(models.Model):
    """
    Extends User model.
    Allows User to add further information in
    addition to that required for Registration.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    is_mod = models.BooleanField(default=False)
    user_image = CloudinaryField('image', default='placeholder')
    owner = models.BigIntegerField(unique=True)

    def __str__(self):
        return f'{self.user.username} Profile

# Create your models here.
