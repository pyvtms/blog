from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # отображение полей
    list_display = ['title', 'slug', 'authorr', 'publish', 'status']
    # добавление фильра по полям
    list_filter = ['status', 'created', 'publish', 'authorr']
    # строка поиска
    search_fields = ['title', 'body']
    # автоматического заполнение поля slug по полю title
    prepopulated_fields = {'slug': ('title', )}
    # Добавление поиского виджета в форме
    raw_id_fields = ['authorr']
    # навигация по датам
    date_hierarchy = 'publish'
    # упорядование
    ordering = ['-status', '-publish']