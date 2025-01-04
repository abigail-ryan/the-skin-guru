from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand, SkinType
from articles.models import Post

# Create your views here.

def all_products(request):
    """
    A view to show all products, including sorting and searching
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    skin_type = SkinType.objects.all()

    query = None
    skin_type = None
    categories = None
    brand = None
    sort = None
    direction = None
    current_sorting = None

    related_articles = []

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif sortkey == 'brand':
                sortkey = 'brand__name'
            elif sortkey == 'skin_type':
                sortkey = 'skin_type__name'


            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    
            products = products.order_by(sortkey)

            current_sorting = f'{sort}_{direction}'

        if 'skin_type' in request.GET:
            skin_type_names = request.GET.getlist('skin_type')
            if skin_type_names:
                products = products.filter(skin_type__name__in=skin_type_names)
                skin_type = SkinType.objects.filter(name__in=skin_type_names)

                # Retrieve related articles based on the selected skin types
                related_articles = Post.objects.filter(skin_type__name__in=skin_type_names)

        if 'category' in request.GET:
            category_names = request.GET.getlist('category')
            if category_names:
                products = products.filter(category__name__in=category_names)
                categories = Category.objects.filter(name__in=category_names)

        if 'brand' in request.GET:
            brand_names = request.GET.getlist('brand')
            if brand_names:
                products = products.filter(brand__name__in=brand_names)
                brand = Brand.objects.filter(name__in=brand_names)


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

    if not related_articles and not query:  #  gets all articles when no filtering is applied
        related_articles = Post.objects.all()
        
    current_sorting = f'{sort}_{direction}'

    context = {
        'products' : products,
        'search_term' : query,
        'current_brand' : brand,
        'current_skin_type' : skin_type,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'related_articles': related_articles,
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