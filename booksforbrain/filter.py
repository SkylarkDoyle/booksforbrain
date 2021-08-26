import django_filters
from .models import Book
from django import forms

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['genre']

        