from django.contrib import admin

from .models import Massage, Comment
from rating.models import Rating, RatingStar


@admin.register(Comment)
class CommentAdminPanel(admin.ModelAdmin):
    list_display = ('name', 'massage', 'created', 'active')
    list_filter = ('active', 'created')


@admin.register(Massage)
class MassageAdminPanel(admin.ModelAdmin):
    list_display = ('name', 'price', 'created')
    list_filter = ('created', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Rating)
admin.site.register(RatingStar)



