from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/',views.create, name = 'create'),
    path('remark/', views.remark, name = 'remark'),
    path('posts/<int:id>/', views.detail_view, name = 'detail')
]