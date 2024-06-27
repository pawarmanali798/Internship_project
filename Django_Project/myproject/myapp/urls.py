from django.urls import path
from .views import StudentView


urlpatterns=[
    path('student/',StudentView.as_view()), # get get, post create
    path('student/<int:rollno>',StudentView.as_view()) #put update, delete delete
]