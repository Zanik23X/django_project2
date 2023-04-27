from django.urls import path, include
from django.contrib import admin
from posts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]



