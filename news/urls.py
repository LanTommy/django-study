from django.urls import path
from . import views


urlpatterns = [
    # http://192.168.4.25:8000/news/index
    path('index',views.index_view),
]