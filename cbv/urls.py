"""
URL configuration for cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userapp.views import UserAPIView,StudentListAPIView,StudentCreateAPIView,StudentRetriveAPIView,StudentDestroyAPIView,StudentUpdateAPIView,GetWithPost,GetWithDelete,GetWithUpdate,GetWithUpdateAndDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',UserAPIView.as_view()),
    path('api/users/<int:id>/',UserAPIView.as_view()),
    path('api/students/',StudentListAPIView.as_view()),
    path('api/addstudent/',StudentCreateAPIView.as_view()),
    path('api/viewstudent/<int:pk>/',StudentRetriveAPIView.as_view()),
    path('api/updatestudent/<int:pk>/',StudentUpdateAPIView.as_view()),
    path('api/deletestudent/<int:pk>/',StudentDestroyAPIView.as_view()),


    path('api/getwithpost/',GetWithPost.as_view()),
    path('api/getwithdelete/<int:pk>/',GetWithDelete.as_view()),
    path('api/getwithupdate/<int:pk>/',GetWithUpdate.as_view()),
    path('api/getwithupdateanddelete/<int:pk>/',GetWithUpdateAndDelete.as_view())
]
