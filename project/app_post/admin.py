from django.contrib import admin

from .models import Post
from django.urls import reverse
from django.utils.html import format_html


class PostAuthor(admin.ModelAdmin):
    list_display = ('headline', 'author_link', 'creation_date')
    list_filter = ('creation_date', )

    def author_link(self, obj):
        link_to_the_author = reverse('admin:app_user_customuser_change', args=[obj.author_id])
        return format_html(f'<a href="http://127.0.0.1:8000/{link_to_the_author}">{obj.author}</a>')

admin.site.register(Post, PostAuthor)