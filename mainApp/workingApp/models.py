from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    book_list = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return self.user.username

    def toggle_admin_status(self):
        self.is_admin = not self.is_admin
        self.save()

class Book(models.Model):
    BOOK_CATEGORIES = (
        ('FICTION', 'Fiction'),
        ('NON_FICTION', 'Non-fiction'),
        ('SCIENCE', 'Science'),
        ('HISTORY', 'History'),
        ('BIOGRAPHY', 'Biography'),
    )
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo', blank=True, null=True)
    details = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=BOOK_CATEGORIES)
    borrowingDate=models.TimeField(null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})