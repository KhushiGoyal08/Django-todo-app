from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup),
    path('add-todo',views.add_todo,name='add-todo'),
    path('logout',views.signout ,name='signout'),
    path('delete-todo/<int:id>',views.delete_todo ),
    path('change_status/<int:id>/<str:status>',views.change_todo)
]