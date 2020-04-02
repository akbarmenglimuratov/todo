from django.contrib import admin
from . import models
from django.contrib.auth.models import User

# Register your models here.
class todo(admin.ModelAdmin):
	list_display = ['user', 'when', 'title', 'text']

class user_note(admin.ModelAdmin):
	list_display = ['user'] 

admin.site.register(models.ToDoList_data, todo)
admin.site.register(models.Users_notes, user_note)
