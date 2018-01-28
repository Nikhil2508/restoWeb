from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsletter.views import home,contact
from ecommerce2.views import about
from products.views import product_detail_view_func, ProductDetailView, ProductListView



urlpatterns = [
    # Examples:
    url(r'^$', ProductListView.as_view() , name='product_list'),
    url(r'^(?P<pk>\d+)$', ProductDetailView.as_view() , name='product_detail'),
]
