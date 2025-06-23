from django.urls import path
from .views import home, download_excel, history

urlpatterns = [
    path('', home, name='home'),
    path('download-excel/', download_excel, name='download_excel'),
    path('history/', history, name='history'),
]
