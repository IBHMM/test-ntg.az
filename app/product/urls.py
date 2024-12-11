from .views import ProductListView, ProductDetailView, search_products, get_brands, get_brands_with_images, get_all_categories, get_parent_categories, get_categories
from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', search_products, name='product-search'),
    path('get-brands/', get_brands, name='get-brands'),
    path('brand-with-image', get_brands_with_images),
    path('parent-categories/', get_parent_categories),
    path('categories/', get_categories),
    path('all-categories/', get_all_categories)
]
