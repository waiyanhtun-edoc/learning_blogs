"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #Page show all topics
    path('topics/',views.topics,name='topics'),
    #Inivitual pasge show all details
    path('topics/<int:topic_id>/' ,views.topic, name='topic'),
    # New Topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # New entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry page
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry')
]
