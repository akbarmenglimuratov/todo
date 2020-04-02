from django.contrib import admin
from django.urls import path, include, re_path
from notes import views as note_view
from home import views as home_view

urlpatterns = [
	re_path(r'done/(?P<pk>\d+)$', note_view.done, name = 'done'),
	re_path(r'(?P<pk>\d+)/delete/', note_view.delete, name = 'delete'),
	re_path(r'(?P<pk>\d+)/archive/', note_view.archive, name = 'archive'),
	path('new_note/', note_view.Add_new_note, name = 'add_new_note'),
	path('archive/', note_view.Archive.as_view(), name = 'archive_view'),
	path('trash/', note_view.Trash.as_view(), name = 'Trash_view'),
	path('', home_view.HomeView.as_view(), name = "home_view")
]
