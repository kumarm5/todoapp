from django.conf.urls import url
from todoapp.views import (
    todo,
    Todolist,
    Todoadd,
    Todoupdate,
    Tododelete
)

urlpatterns = [
    url(r'^$', todo ),
    url(r'^list/$', Todolist.as_view()),
    url(r'^add/$', Todoadd.as_view()),
    url(r'^update/(?P<pk>[\d-]+)/$', Todoupdate.as_view()),
    url(r'^delete/(?P<pk>[\d-]+)/$', Tododelete.as_view())
]