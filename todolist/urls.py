from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addTodoItem,name='add'),
    path('completed/<todo_id>',views.completedTodo,name='completed'),
    path('deletecompleted',views.deleteCompleted,name='deletecompleted'),
    path('deleteall',views.deleteAll,name='deleteall')
]