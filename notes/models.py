from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

WHEN = (
	('today','Today'),
	('tomorrow', 'Tomorrow'),
	('thisWeek', 'This week'),
	('nextWeek', 'Next week'),
	('future', 'Future'),
)

class ToDoList_data(models.Model):
	title = models.TextField()
	text = models.TextField()
	when = models.CharField(max_length = 20, choices = WHEN, default = 'Today')
	date_created = models.DateTimeField()
	done = models.BooleanField(default = False)
	archive = models.BooleanField(default = False)
	deleted = models.BooleanField(default = False)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

class Users_notes(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	notes = models.ManyToManyField(ToDoList_data, blank = True)

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = Users_notes.objects.create(user = kwargs['instance'])

post_save.connect(create_profile,sender=User)