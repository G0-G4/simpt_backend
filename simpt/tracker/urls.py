from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('sections/', SectionList.as_view()),
    path('sections/<int:pk>/', SectionPK.as_view()),
    path('statuses/', StatusList.as_view()),
    path('statuses/<int:pk>/', StatusPK.as_view()),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskPK.as_view())
]
