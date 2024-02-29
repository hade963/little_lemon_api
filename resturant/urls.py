from django.urls import path

from . import views
urlpatterns = [
  path('menu/', views.MenuitemsView.as_view()),
  path('menu/<int:pk>', views.SingleMenuitemView.as_view()),
]