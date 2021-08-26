from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    GENRES = (
        ('Bibles', 'Bibles'),
        ('Computer', 'Computer'),
        ('Encyclopedia', 'Encyclopedia'),
        ('History', 'History'),
        ('Language & Literature', 'Language & Literature'),
        ('Mathematics', 'Mathematics'),
        ('Medical', 'Medical'),
        ('Psychology', 'Psychology'),
        ('Science', 'Science'),
        ('Social Science', 'Social Science'),
        ('Technology & Engineering', 'Technology & Engineering')
    )
    book_image = models.URLField(max_length=200)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    price = models.FloatField()
    genre = models.CharField(max_length=100, choices=GENRES)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    book_link = models.URLField(max_length=200, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name

class OwnedBook(models.Model):
    OWNED = (
      ('not owned', 'not owned'),
      ('owned', 'owned')
    )
    reader = models.ForeignKey(User, related_name="owned", null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_sold = models.DateTimeField(auto_now_add=True)
    owned = models.CharField(max_length=100, null=True, choices=OWNED, default='not owned')
    

    