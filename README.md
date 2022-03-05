# Сервер по публикации отзывов

Простой сервер с одной моделью и особенностями.

### Данное приложение реализует:
*  авторизацию __django.auth__
* запросы к стороннему серверу
* изменение формы перед сохранением
* изменение стандартной панели администратора для модели отзыва:
    - добавление кнопки публикации
    - добавление неизменяемых полей
    - скрипт jQuery для обработки запроса на сервер

## Установка

Скачайте архив, установите необходимые библиотеки ( см. requirements.txt)

```
Django==4.0
mysqlclient==2.1.0
requests==2.27.1
```

Запустите __script.sql__ для создания базы данных и пользователя
```sql
create database reviews;
CREATE USER 'review_admin'@'localhost' IDENTIFIED BY 'Password 123';
GRANT  ALL PRIVILEGES ON reviews.* TO 'review_admin'@'localhost';
flush privileges
```

## Список конечных точек:

```python
urlpatterns = [
    path('', ReviewsListView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', CreateUserView.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/send/', csrf_exempt(SendReviewView.as_view()))
]

```
