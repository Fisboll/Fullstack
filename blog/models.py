from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

STATUS = ((0, 'Draft'), (1, 'Published'))
PLATFORM = (
    ('Playstation', 'Playstation'), ('Xbox', 'Xbox'), ('PC', 'PC'),
    ('VR', 'VR'), ('Nintendo', 'Nintendo'))
SUBGENRES = (
    (0, 'none'), (1, 'Survival and horror'), (2, 'Fantasy'), (3, 'Sci-Fi'),
    (5, 'Action-adventure'), (5, 'Comedy'), (7, 'Cyberpunk'),
    (8, 'Apocalyptic'), (9, 'MMORPG'), (10, 'Strategy'))


class Game(models.Model):
    name = models.CharField(max_length=50)
    subgenres = models.IntegerField(choices=SUBGENRES)
    platform = MultiSelectField(choices=PLATFORM)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=2000)
    release_date = models.DateTimeField(setattr)

    def __str__(self):
        return self.name.__str__()

    def __Str__(self):
        return self.subgenres.choices[1]


class Platform(models.Model):
    platform = [
        ('Playstation', 'Playstation'), ('Xbox', 'Xbox'), ('Pc', 'Pc'),
        ('VR', 'VR'), ('Nintendo', 'Nintendo')
    ]
    title = models.CharField(max_length=50)
    image = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='post_user')
    content = models.TextField(max_length=2000)
    image = CloudinaryField('image', default='placeholder')
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='game_posts')
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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"comment {self.content} by {self.name}"


class User_profile(models.Model):
    avatar = CloudinaryField('image', default='placeholder')
    display_name = models.TextField(max_length=30)
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    location = models.TextField(max_length=50)
    is_mod = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='user_profile')

# Create your models here.
