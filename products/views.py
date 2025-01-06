from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand, SkinType, Review
from checkout.models import Order
from articles.models import Post
from .forms import ReviewForm

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

    reviews = product.reviews.all().order_by("-created_on")
    review_count = reviews.filter(approved=True).count()

    # Check if the user has purchased this product
    user_has_purchased = False
    if request.user.is_authenticated:
        # Check if any of the user's orders contain this product
        user_has_purchased = Order.objects.filter(
            user_profile__user=request.user,
            lineitems__product=product).exists()
        
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save() 
            messages.add_message(
                request, messages.SUCCESS,
                'Your review is submitted and awaiting approval'
            )

            return redirect('product_detail', product_id=product.id)  # Redirect to avoid resubmission

    else:
        review_form = ReviewForm() 

    context = {
        'product' : product,
        'reviews': reviews,
        'review_count': review_count,
        "review_form": review_form,
        'user_has_purchased': user_has_purchased,
    }
    
    return render(request, 'products/product_detail.html', context)


def review_edit(request, product_id, review_id):
    """
    View to edit reviews
    """
    # Get the product and the review to be edited
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)  

        if review_form.is_valid() and review.user == request.user: 
            review = review_form.save(commit=False)
            review.product = product 
            review.approved = False  
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated successfully!')
            return redirect('product_detail', product_id=product.id)  
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    else:
        review_form = ReviewForm(instance=review) 

    context = {
        'product': product,
        'review_form': review_form,
        'review': review,
    }

    return render(request, 'products/review_edit.html', context)  


def review_delete(request, product_id, review_id):
    """
    View to delete reviews
    """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return redirect('product_detail', product_id=product.id)