from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True)
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    email = models.EmailField(max_length=254, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name="Пароль")
    def __str__(self):
        return self.first_name + " " + self.last_name

    REQUIRED_FIELDS = [ 'first_name', 'last_name', 'email', 'date_joined']



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name="Рейтинг")
    text = models.TextField(blank=True, null=True, verbose_name="Отзыв")
    date_created = models.DateTimeField()
    published = models.BooleanField(default=False)