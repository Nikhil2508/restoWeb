from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsletter.views import home,contact
from ecommerce2.views import about
from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView, OrdersList, OrderDetail
from orders.views import AddressSelectFormView


urlpatterns = [
    # Examples:
    url(r'^$', home , name='home'),
    url(r'^contact/$', contact , name='contact'),
    url(r'^about/$', about , name='about'),
    url(r'^carts/$', CartView.as_view() , name='cart'),
    url(r'^orders/$', OrdersList.as_view() , name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view() , name='order_detail'),
    url(r'^carts/count$', ItemCountView.as_view() , name='item_count'),
    url(r'^checkout$', CheckoutView.as_view() , name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view() , name='order_address'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view() , name='checkout_final'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
