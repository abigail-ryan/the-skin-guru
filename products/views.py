from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Brand, SkinType

# Create your views here.

def all_products(request):
    """
    A view to show all products, including sorting and searching
    """
    products = Product.objects.all()
    query = None
    skin_type = None
    categories = None
    brand = None

    if request.GET:

        if 'skin_type' in request.GET:
            skin_type_names = request.GET.getlist('skin_type')
            if skin_type_names:
                products = products.filter(skin_type__name__in=skin_type_names)
                skin_type = SkinType.objects.filter(name__in=skin_type_names)

        if 'category' in request.GET:
            category_names = request.GET.getlist('category')
            if category_names:
                products = products.filter(category__name__in=category_names)
                categories = Category.objects.filter(name__in=category_names)

        if 'brand' in request.GET:
            brand_names = request.GET.getlist('brand')
            if brand_names:
                products = products.filter(brand__name__in=brand_names)
                brands = Brand.objects.filter(name__in=brand_names)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (
                    Q(name__icontains=query) | 
                    Q(description__icontains=query) | 
                    Q(brand__friendly_name__icontains=query) |
                    Q(skin_type__friendly_name__icontains=query) |
                    Q(category__friendly_name__icontains=query) |
                    Q(key_ingredients__icontains=query) 
                )
            products = products.filter(queries)
        
    
    context = {
        'products' : products,
        'search_term' : query,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }
    
    return render(request, 'products/product_detail.html', context)