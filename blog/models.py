from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
SUBGENRES = (
    (0, 'Strategy'), (1, 'Survival and horror'), (2, 'Fantasy'), (3, 'Sci-Fi'),
    (4, 'Action-adventure'), (5, 'Comedy'), (7, 'Cyberpunk'),
    (8, 'Apocalyptic'), (9, 'Other'))

# Create your models here.
