
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

from .views import blogPage, BlogPostDetailView


urlpatterns = [
    path('',blogPage, name ='blog'),  
    path('<slug>/',BlogPostDetailView.as_view(), name ='blog'),   

]