from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    search = request.GET.get('q')
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(slug__icontains=search)
        )
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 2 if index <= max_index else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'items': items,
        'page_range': page_range,
    }
    return render(request,'index.html',context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, pk=id, slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    related = Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request,'detail.html',{'product': product, 'related':related, 'cart_product_form': cart_product_form})











