from django.urls import path
from shoes.views import *

app_name='shoes'

urlpatterns=[
    path('nike/',nike,name='nike'),
    path('adidas/',adidas,name='adidas')
]