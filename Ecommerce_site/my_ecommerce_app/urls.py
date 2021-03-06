from django.conf.urls import url
from . import views
from .views import AddToCart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^product/(\d+)',views.get_product,name ='product'),
    url(r'^cart/',views.cart,name ='cart'),
    # url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^product/(\d+ )', AddToCart.as_view(), name='cart')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
