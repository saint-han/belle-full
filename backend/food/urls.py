from django.conf.urls import url
from . import views


urlpatterns = [
    url('food/', views.FoodListCreate.as_view()),
]
