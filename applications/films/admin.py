from django.contrib import admin
from applications.films.models import *

class FilmsAdmin(admin.ModelAdmin):
    list_display = ('film' ,'rate', 'likes')



# Register your models here.
admin.site.register(Films)
admin.site.register(Review, FilmsAdmin)
# admin.site.register(Rating)
