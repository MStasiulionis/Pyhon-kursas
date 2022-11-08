from django.contrib import admin
from .models import Game, Genre, Publisher, GameReview


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'date_created', 'reviewer', 'content')


admin.site.register(Game, GameAdmin)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(GameReview, ReviewAdmin)
