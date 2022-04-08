from django.urls import re_path 
from users import views 
 
urlpatterns = [ 
    re_path(r'^api/users/$', views.user_list),
    re_path(r'^api/users/(?P<pk>[0-9]+)$', views.user_detail),
]