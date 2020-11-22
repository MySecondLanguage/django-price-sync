from django.urls import path

from . import views

urlpatterns = [
    path('extract-product/', views.ExtractProductURL.as_view(), name='price.extract_product'),
]
