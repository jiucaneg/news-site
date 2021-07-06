from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    author = models.ForeignKey(User, blank=True, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Отображать')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тег', related_name='posts')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


