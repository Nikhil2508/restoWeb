from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsletter.views import home,contact
from ecommerce2.views import about
from products.views import product_detail_view_func, ProductDetailView, ProductListView, CategoryListView, CategoryDetailView



urlpatterns = [
    # Examples:
    url(r'^$', CategoryListView.as_view() , name='category_list'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view() , name='category_detail'),
]
