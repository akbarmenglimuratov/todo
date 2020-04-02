from django.shortcuts import render
from django.views.generic import TemplateView
from notes.models import Users_notes
from datetime import datetime
from django.utils import timezone

# class HomeView(TemplateView):
# 	model = ToDoList_data
# 	template_name = "home/home.html"

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		try:
# 			context['data'] = ToDoList_data.objects.all().order_by('-when')
# 		except ToDoList_data.DoesNotExist:
# 			context['data'] = {}
# 		return context


class HomeView(TemplateView):
	model = Users_notes
	template_name = 'home/home.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = Users_notes.objects.get(user = self.request.user)
		context['sort_by_when'] = ['Today', 'Tomorrow', 'This week', 'Next week', 'Future']
		context['today'] = timezone.now()
		return context

