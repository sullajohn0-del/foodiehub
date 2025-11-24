from django.core.management.base import BaseCommand
from myapp.models import Restaurant, MenuItem


class Command(BaseCommand):
    help = 'Add complete Mang Inasal menu items'

    def handle(self, *args, **options):
        try:
            mang_inasal = Restaurant.objects.get(name='Mang Inasal')
        except Restaurant.DoesNotExist:
            self.stdout.write(self.style.ERROR('Mang Inasal restaurant not found'))
            return

        # Clear existing menu items
        mang_inasal.menu_items.all().delete()

        menu_items = [
            # Chicken Inasal
            {'name': 'Chicken Inasal Pecho', 'description': 'Grilled chicken breast marinated in special spices with unlimited rice', 'price': 129.00, 'category': 'Chicken Inasal', 'is_popular': True, 'calories': 450},
            {'name': 'Chicken Inasal Paa', 'description': 'Grilled chicken leg marinated in special spices with unlimited rice', 'price': 99.00, 'category': 'Chicken Inasal', 'is_popular': True, 'calories': 380},
            {'name': 'Chicken Inasal Whole', 'description': 'Whole grilled chicken marinated in special spices', 'price': 299.00, 'category': 'Chicken Inasal', 'calories': 850},
            {'name': 'Chicken Inasal Half', 'description': 'Half grilled chicken marinated in special spices', 'price': 159.00, 'category': 'Chicken Inasal', 'calories': 425},

            # Pork BBQ
            {'name': 'Pork BBQ 2pcs', 'description': 'Two pieces of grilled pork skewers with sweet sauce', 'price': 79.00, 'category': 'Pork BBQ', 'is_popular': True, 'calories': 320},
            {'name': 'Pork BBQ 3pcs', 'description': 'Three pieces of grilled pork skewers with sweet sauce', 'price': 109.00, 'category': 'Pork BBQ', 'calories': 480},
            {'name': 'Pork BBQ Solo', 'description': 'Single pork BBQ stick with rice', 'price': 59.00, 'category': 'Pork BBQ', 'calories': 280},

            # Sisig
            {'name': 'Bangus Sisig', 'description': 'Sizzling milkfish sisig with egg and onions', 'price': 129.00, 'category': 'Sisig', 'is_popular': True, 'calories': 350},
            {'name': 'Pork Sisig', 'description': 'Sizzling pork sisig with egg and chili', 'price': 119.00, 'category': 'Sisig', 'calories': 420},
            {'name': 'Chicken Sisig', 'description': 'Sizzling chicken sisig with egg and onions', 'price': 109.00, 'category': 'Sisig', 'calories': 380},

            # Rice Meals
            {'name': 'Unlimited Rice', 'description': 'Unlimited steamed rice - perfect with any grilled item', 'price': 25.00, 'category': 'Rice', 'is_vegetarian': True, 'calories': 200},
            {'name': 'Garlic Rice', 'description': 'Fragrant garlic fried rice', 'price': 35.00, 'category': 'Rice', 'is_vegetarian': True, 'calories': 250},
            {'name': 'Java Rice', 'description': 'Yellow turmeric rice', 'price': 40.00, 'category': 'Rice', 'is_vegetarian': True, 'calories': 220},

            # Soup
            {'name': 'Batchoy', 'description': 'Traditional noodle soup with pork and liver', 'price': 89.00, 'category': 'Soup', 'calories': 380},
            {'name': 'Pancit Molo', 'description': 'Dumpling soup with ground pork', 'price': 79.00, 'category': 'Soup', 'calories': 320},

            # Desserts
            {'name': 'Halo-Halo', 'description': 'Traditional Filipino shaved ice dessert with mixed ingredients', 'price': 69.00, 'category': 'Desserts', 'is_popular': True, 'calories': 280},
            {'name': 'Leche Flan', 'description': 'Creamy caramel custard dessert', 'price': 59.00, 'category': 'Desserts', 'calories': 220},
            {'name': 'Buko Pie Slice', 'description': 'Traditional coconut pie slice', 'price': 49.00, 'category': 'Desserts', 'calories': 180},

            # Beverages
            {'name': 'Fresh Buko Juice', 'description': 'Fresh coconut water', 'price': 45.00, 'category': 'Beverages', 'calories': 60},
            {'name': 'Sago\'t Gulaman', 'description': 'Traditional Filipino drink with sago pearls and gulaman', 'price': 35.00, 'category': 'Beverages', 'calories': 120},
            {'name': 'Iced Tea', 'description': 'Refreshing iced tea', 'price': 29.00, 'category': 'Beverages', 'calories': 80},
            {'name': 'Softdrinks', 'description': 'Coke, Sprite, or Royal', 'price': 39.00, 'category': 'Beverages', 'calories': 140},

            # Appetizers
            {'name': 'Chicken Skin', 'description': 'Crispy fried chicken skin with spicy vinegar', 'price': 69.00, 'category': 'Appetizers', 'calories': 180},
            {'name': 'Tokwa\'t Baboy', 'description': 'Tofu and pork with soy-vinegar sauce', 'price': 89.00, 'category': 'Appetizers', 'calories': 220},
            {'name': 'Lumpiang Shanghai', 'description': 'Fried spring rolls with ground pork (6pcs)', 'price': 79.00, 'category': 'Appetizers', 'calories': 240},

            # Combo Meals
            {'name': 'Inasal + BBQ Combo', 'description': 'Chicken Inasal Paa + 2pcs Pork BBQ with unlimited rice', 'price': 159.00, 'category': 'Combo Meals', 'is_popular': True, 'calories': 700},
            {'name': 'Family Feast', 'description': 'Whole Chicken Inasal + 4pcs Pork BBQ + 4 cups rice', 'price': 399.00, 'category': 'Combo Meals', 'calories': 1200},
            {'name': 'Barkada Meal', 'description': '2 Chicken Inasal + 6pcs Pork BBQ + unlimited rice for 4', 'price': 599.00, 'category': 'Combo Meals', 'calories': 1800},
        ]

        for item_data in menu_items:
            MenuItem.objects.create(
                restaurant=mang_inasal,
                image_url=f'https://images.unsplash.com/photo-{self.get_image_id(item_data["category"])}?w=300',
                **item_data
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(menu_items)} menu items to Mang Inasal!'))

    def get_image_id(self, category):
        image_map = {
            'Chicken Inasal': '1598515214211-89d3c73ae83b',
            'Pork BBQ': '1544025162-d76694265947',
            'Sisig': '1565299624946-b28f40a0ca4b',
            'Rice': '1586201375761-83865001e31c',
            'Soup': '1547592166-23ac45744acd',
            'Desserts': '1563379091339-03246963d96c',
            'Beverages': '1571115764595-644a1f56a55c',
            'Appetizers': '1565299624946-b28f40a0ca4b',
            'Combo Meals': '1598515214211-89d3c73ae83b'
        }
        return image_map.get(category, '1565299624946-b28f40a0ca4b')