from django.shortcuts import render, redirect
from .forms import ToDoList_form
from django.utils import timezone
from .models import Users_notes, ToDoList_data
from django.http import Http404, JsonResponse
from django.views.generic import TemplateView


# Add new note
def Add_new_note(request):
	if request.method == "POST":
		form = ToDoList_form(request.POST)

		if form.is_valid():
			obj = form.clean()
			obj = form.save(commit = False)
			obj.date_created = timezone.now()
			obj.user = request.user

			obj.save()
			form.save_m2m()
			add_to_users_notes = Users_notes.objects.get(user=request.user)
			add_to_users_notes.notes.add(obj)
			return redirect('/')
	else:
		form = ToDoList_form()
	return render(request,'notes/new_note.html', context = {'forms': form})

def done(request, pk):
	data = {}
	if request.is_ajax():
		try:	
			note_id = int(pk)
			obj = ToDoList_data.objects.get(pk = note_id)
			diff = timezone.now() - obj.date_created
			
			if request.user.is_authenticated == True:
				if obj.user == request.user:
					if obj.done == True:
						obj.done = False
					else:
						obj.done = True
					obj.save()
					data['success'] = True
					data['message'] = "Done"
				else:
					data['success'] =  False
					data['message'] = "Fail"
			return JsonResponse(data)
		except ToDoList_data.DoesNotExist:
			raise Http404("Error")
	else:
		raise Http404("Page doesn't exist!")

def delete(request,pk):
	try:
		note_id = int(pk)
		obj = ToDoList_data.objects.get(pk = note_id)
		if request.user.is_authenticated == True:
			if obj.user == request.user:
				if obj.deleted == True:
					obj.deleted = False
				else:
					obj.deleted = True
				obj.save()
			return redirect('/')

		else:
			return redirect('/')
	except ToDoList_data.DoesNotExist:
		raise Http404("Error")

def archive(request,pk):
	try:
		note_id = int(pk)
		obj = ToDoList_data.objects.get(pk = note_id)
		if request.user.is_authenticated == True:
			if obj.user == request.user:
				if obj.archive == True:
					obj.archive = False
				else:
					obj.archive = True
				obj.save()
			return redirect('/')

		else:
			return redirect('/')
	except ToDoList_data.DoesNotExist:
		raise Http404("Error")

class Archive(TemplateView):
	model = Users_notes
	template_name = "notes/archive.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = Users_notes.objects.get(user = self.request.user)
		context['sort_by_when'] = ['Today', 'Tomorrow', 'This week', 'Next week', 'Future']
		return context

class Trash(TemplateView):
	model = Users_notes
	template_name = "notes/trash.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = Users_notes.objects.get(user = self.request.user)
		context['sort_by_when'] = ['Today', 'Tomorrow', 'This week', 'Next week', 'Future']
		return context