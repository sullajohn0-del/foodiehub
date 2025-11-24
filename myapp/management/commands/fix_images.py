from django.core.management.base import BaseCommand
from myapp.models import Restaurant, MenuItem


class Command(BaseCommand):
    help = 'Fix restaurant and menu item images with better URLs'

    def handle(self, *args, **options):
        # Update restaurant images
        restaurant_images = {
            'Jollibee': 'https://images.unsplash.com/photo-1513185158878-8d064c2de2a2?w=500',
            'Mang Inasal': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=500',
            'Goldilocks': 'https://images.unsplash.com/photo-1571115764595-644a1f56a55c?w=500',
            'Chowking': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=500',
            'Kamayan sa Palaisdaan': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=500',
            'Max\'s Restaurant': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=500',
            'Barrio Fiesta': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=500',
            'Aristocrat Restaurant': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=500',
            'Pancake House': 'https://images.unsplash.com/photo-1506084868230-bb9d95c24759?w=500',
            'Tapa King': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=500'
        }

        # Update menu item images by category
        menu_images = {
            'Chicken': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=300',
            'Pasta': 'https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=300',
            'Burgers': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=300',
            'Desserts': 'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=300',
            'Sandwiches': 'https://images.unsplash.com/photo-1606755962773-d324e9a13086?w=300',
            'Grilled': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=300',
            'Sisig': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Rice': 'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300',
            'Noodles': 'https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=300',
            'Soup': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=300',
            'Filipino Dishes': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Appetizers': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Pork': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300',
            'Vegetables': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=300',
            'Spicy': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'BBQ': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300',
            'Beef': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=300',
            'Pancakes': 'https://images.unsplash.com/photo-1506084868230-bb9d95c24759?w=300',
            'Rice Meals': 'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300',
            'Silog Meals': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Beverages': 'https://images.unsplash.com/photo-1544145945-f90425340c7e?w=300',
            'Chicken Inasal': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=300',
            'Pork BBQ': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300',
            'Combo Meals': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Cakes': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=300',
            'Pastries': 'https://images.unsplash.com/photo-1571115764595-644a1f56a55c?w=300',
            'Dim Sum': 'https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=300',
            'Seafood': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300',
            'Stews': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=300'
        }

        # Update restaurant images
        for restaurant_name, image_url in restaurant_images.items():
            try:
                restaurant = Restaurant.objects.get(name=restaurant_name)
                restaurant.image_url = image_url
                restaurant.save()
                self.stdout.write(f'Updated image for {restaurant_name}')
            except Restaurant.DoesNotExist:
                self.stdout.write(f'Restaurant {restaurant_name} not found')

        # Update menu item images
        for menu_item in MenuItem.objects.all():
            if menu_item.category in menu_images:
                menu_item.image_url = menu_images[menu_item.category]
                menu_item.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated all images!'))