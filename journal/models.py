from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    CATEGORY_CHOICES = [
        ("Academic", "Academic Piece" ),
        ("Article", "Article"),
        ("Web", "Web Project"),
        ("Life", "Life Update"),
    ]
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=15,
        blank=True)

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Bio(models.Model):
    birthday = models.DateField()
    biography = models.TextField()
    biography_blurb = models.TextField(blank=True)
    def age(self):
        return timezone.now() - self.birthday
