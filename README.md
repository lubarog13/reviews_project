# Сервер по публикации отзывов

Простой сервер с одной моделью и особенностями.

### Данное приложение реализует:
* авторизацию __django.auth__
* запросы к стороннему серверу
* переопредиление функции create в serializers
* изменение стандартной панели администратора для модели отзыва:
    - добавление кнопки публикации
    - добавление неизменяемых полей

## Установка

Скачайте архив, установите необходимые библиотеки ( см. requirements.txt)

```
Django==4.0
mysqlclient==2.1.0
requests==2.27.1
djangorestframework==3.13.1
```

Запустите __script.sql__ для создания базы данных и пользователя
```sql
create database reviews;
CREATE USER 'review_admin'@'localhost' IDENTIFIED BY 'Password 123';
GRANT  ALL PRIVILEGES ON reviews.* TO 'review_admin'@'localhost';
flush privileges
```

## Список url:

```python
urlpatterns = [
    path('', ReviewsListView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', CreateUserView.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/send/', csrf_exempt(SendReviewView.as_view())),
    # get, post
    path('api/review/', ReviewApiView.as_view()),
    path('api/review/<int:id>/', SendReviewView.as_view())
]

```
