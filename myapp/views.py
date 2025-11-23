from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Restaurant, MenuItem, Category, Order


def home(request):
    """Home page with restaurant listings"""
    restaurants = Restaurant.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        restaurants = restaurants.filter(
            Q(name__icontains=search_query) |
            Q(cuisine_type__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Filter by cuisine
    cuisine_filter = request.GET.get('cuisine', '')
    if cuisine_filter:
        restaurants = restaurants.filter(cuisine_type__icontains=cuisine_filter)
    
    # Sort
    sort_by = request.GET.get('sort', 'rating')
    if sort_by == 'delivery_time':
        restaurants = restaurants.order_by('delivery_time')
    elif sort_by == 'delivery_fee':
        restaurants = restaurants.order_by('delivery_fee')
    else:
        restaurants = restaurants.order_by('-rating')
    
    # Get unique cuisines for filter
    cuisines = Restaurant.objects.filter(is_active=True).values_list('cuisine_type', flat=True).distinct()
    
    context = {
        'restaurants': restaurants,
        'search_query': search_query,
        'cuisine_filter': cuisine_filter,
        'sort_by': sort_by,
        'cuisines': cuisines,
    }
    return render(request, 'home.html', context)


def restaurant_detail(request, slug):
    """Restaurant detail page with menu"""
    restaurant = get_object_or_404(Restaurant, slug=slug, is_active=True)
    menu_items = restaurant.menu_items.filter(is_available=True)
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        menu_items = menu_items.filter(category=category_filter)
    
    # Get unique categories
    categories = menu_items.values_list('category', flat=True).distinct()
    
    context = {
        'restaurant': restaurant,
        'menu_items': menu_items,
        'categories': categories,
        'category_filter': category_filter,
    }
    return render(request, 'restaurant_detail.html', context)


def menu_item_detail(request, restaurant_slug, item_id):
    """Menu item detail page"""
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug, is_active=True)
    menu_item = get_object_or_404(MenuItem, id=item_id, restaurant=restaurant, is_available=True)
    
    context = {
        'restaurant': restaurant,
        'menu_item': menu_item,
    }
    return render(request, 'menu_item_detail.html', context)
