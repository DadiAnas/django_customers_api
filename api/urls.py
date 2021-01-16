from django.urls import path
from .views import CustomerAPIView

urlpatterns = [
    path('customers/', CustomerAPIView.as_view()),
    path('customers/<int:id>', CustomerAPIView.as_view()),
]
