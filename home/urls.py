from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='searchIndex'),
    #url(r'^register/', views.UserFormView, name='register'),

]
