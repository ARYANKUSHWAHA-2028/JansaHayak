from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire, name='questionnaire'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]
