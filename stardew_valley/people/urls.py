from django.urls import path

from . import views


app_name = 'people'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/details/', views.VillagerDetailView.as_view(),
         name='villager_detail'),
]
