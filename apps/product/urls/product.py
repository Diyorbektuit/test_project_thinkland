from django.urls import path

from apps.product.views.product import ProductListView, CategoryListView, ProductRetrieveView, CategoryRetrieveView


urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("products/<int:id>/", ProductRetrieveView.as_view()),
    path("categories/<int:id>/", CategoryRetrieveView.as_view()),
    ]