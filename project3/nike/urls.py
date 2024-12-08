from django.urls import path
from nike.views import *

app_name='shoes'

urlpatterns=[
    path('nike/',nike,name='nike'),
]