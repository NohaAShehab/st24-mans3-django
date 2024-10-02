
from django.urls import path
from students.views import hello, hi, students_list, std_profile
# this list contains views written in students.views
urlpatterns = [
    path('intro', hello, name='myhello'),
    path('hi', hi, name='myhi'),
    path('list',students_list,name='mystudents_list' ),
    path('profile/<int:id>',std_profile,name='myprofile'),
]
