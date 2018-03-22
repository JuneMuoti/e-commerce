from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.core.exceptions import ObjectDoesNotExist
def index(request):
    products=Product.my_product()
    return render (request,'index.html',{'products':products})

class AddToCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get("id")
        cart_add = Product.objects.get(id=id)
        id_ = cart_add.get_specific_product()
        user = self.request.user
        print(id_, user)
        if user.is_authenticated():
            if user in cart_add.cart.all():
                cart_add.cart.remove(user)
                return redirect('/')
            else:
                cart_add.cart.add(user)
        return id_

def get_product(request,product_id):
    try:
        item = Product.objects.get(id = product_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'product.html', {"item":item})
def cart(request):
    return render(request,'cart.html')
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        queryList = request.GET.get("category")
        searched_product = Product.search_by_category(queryList)
        message = f"{queryList}"

        return render(request, 'search.html',{"message":message,"searched_product": searched_product})

    else:
        message = "You haven't searched for any businesses"
        return render(request, 'search.html',{"message":message})
