from django.contrib import admin
from .models import Post, Habit, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'text',
                    'pub_date',
                    'habit')
    search_fields = ('title', 'text',)
    list_filter = ('pub_date',)
    list_editable = ('habit',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Habit)
admin.site.register(Comment)
admin.site.register(Follow)