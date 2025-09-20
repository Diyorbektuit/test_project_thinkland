from django.urls import path

from apps.product.views.product import ProductListView, CategoryListView


urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("categories/", CategoryListView.as_view())
    ]