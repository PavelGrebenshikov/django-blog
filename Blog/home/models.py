from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category = models.CharField("Категории", max_length=150, default="Posts", blank=False)
    slug = models.SlugField(max_length=128, unique=True, blank=True, default=None)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('post_page', kwargs={'slug': self.slug})

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

# Модель постов
class Posts(models.Model):
    author = models.CharField("Имя автора", max_length=100, blank=False)
    title = models.CharField("Заголовок поста", default="", max_length=100, blank=False)
    text = models.TextField("Содержание поста", blank=False)
    create_date = models.DateField("Дата создания", auto_now_add=True)
    published = models.BooleanField("Опубликовать: ", default=False)
    category_post = models.ForeignKey(Category, verbose_name="Категория поста", null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_number', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comments(models.Model):
    post = models.OneToOneField(Posts, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField("Ваше имя", max_length=100, blank=False)
    text = models.TextField("Поля для вашего текста")
    create_date = models.DateTimeField("Дата создания комментария", auto_now_add=True)
    
    class Meta():
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-create_date']