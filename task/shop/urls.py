from django.urls import path
from . import views
from .views import BikeView


urlpatterns = [
    path('', views.index_view, name='index.html'),
    path('bikes/', views.bike_view, name='bikes.html'),
    path('bikes/<int:bike_id>/', BikeView.as_view(), name='bike_details.html'),
    path('order/<int:order_id>/', views.order_view, name='order.html')
]
