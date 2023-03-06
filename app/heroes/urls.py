from django.urls import path, re_path

from heroes.views import *


urlpatterns = [
    path('', index, name='home'),  
    path('about/', about, name='about'),
    path('tree_menu/', treeMenu)
]