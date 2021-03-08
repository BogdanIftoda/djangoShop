from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.cart import Cart
from cart.forms import CartAddProductForm


def index(request):
    products = Product.get_all_product()
    featured_products = Product.get_all_featured_product()
    category = Category.get_all_category()
    return render(request, 'shop/index.html', {'products': products, 'featured_products': featured_products,
                                          'category': category})


def category_list(request, category_id):
    category = Category.get_all_category()
    products = Product.get_product_by_category_id(category_id)
    return render(request, 'shop/category.html', {'products': products, 'category': category})


def product_detail(request, slug):
    category = Category.get_all_category()
    product = Product.get_one_product(slug)
    form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'category': category, 'form': form})