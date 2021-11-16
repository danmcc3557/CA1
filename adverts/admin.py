from django.contrib import admin
from .models import Advert, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class AdvertAdmin(admin.ModelAdmin):
    inline = [
        CommentInLine
    ]

admin.site.register(Advert)
admin.site.register(Comment)