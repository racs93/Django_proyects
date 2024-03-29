from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.addTodo, name='add'),
	path('updatetodo', views.updateLastTodo, name='updatetodo'),
	path('complete/<todo_id>', views.completeTodo, name='complete'),
	path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
	path('deleteall', views.deleteAll, name='deleteall')
]
