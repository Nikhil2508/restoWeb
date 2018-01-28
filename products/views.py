from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from .models import Products, Category
from django.db.models import Q



class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "products/products_list.html"

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.products_set.all()
        default_products = obj.default_category.all()
        products = ( product_set | default_products).distinct()
        context["products"] = products
        return context


class ProductDetailView(DetailView):
    model = Products

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context["related"] = Products.objects.get_related(instance).order_by("?")
        return context

def product_detail_view_func(request, pk):
    product_instance = Products.objects.get(id = pk)
    template_name = 'products/products_detail.html'
    context = {

        "object":product_instance

    }
    return render(request,template_name,context)

class ProductListView(ListView):
    model = Products
    queryset = Products.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs
