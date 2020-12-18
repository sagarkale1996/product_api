from django.urls import path
from . import views
urlpatterns = [
    path('productcategory/', views.CategoryCRUD.as_view()),
    path('product/', views.ProductCRUD.as_view()),
]