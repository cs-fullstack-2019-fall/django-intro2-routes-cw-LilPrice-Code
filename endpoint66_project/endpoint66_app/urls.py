from django.urls import path,include
from . import views

urlpatterns = [
    path('gogetthegood/', views.allGood),
    path('happyhappyjoyjoy/', views.joy),
    # path('', view),
    # path('', view),
    # path('', view),
]