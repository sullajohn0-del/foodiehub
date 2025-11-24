from django.core.management.base import BaseCommand
from myapp.models import Restaurant, MenuItem
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Add Filipino restaurants and menu items'

    def handle(self, *args, **options):
        # Create Filipino restaurants
        restaurants_data = [
            {
                'name': 'Jollibee',
                'description': 'The home of the world-famous Chickenjoy and other Filipino favorites',
                'cuisine_type': 'Filipino Fast Food',
                'rating': 4.5,
                'review_count': 2847,
                'delivery_time': '15-25 min',
                'delivery_fee': 49.00,
                'min_order': 199.00,
                'address': 'Multiple Locations',
                'is_promoted': True,
                'discount_text': '20% OFF',
                'image_url': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=500'
            },
            {
                'name': 'Mang Inasal',
                'description': 'Authentic Filipino grilled chicken and unlimited rice',
                'cuisine_type': 'Filipino Grill',
                'rating': 4.3,
                'review_count': 1923,
                'delivery_time': '20-30 min',
                'delivery_fee': 39.00,
                'min_order': 150.00,
                'address': 'Nationwide',
                'is_promoted': True,
                'discount_text': 'Free Delivery',
                'image_url': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=500'
            },
            {
                'name': 'Goldilocks',
                'description': 'Filipino bakery and restaurant serving traditional dishes and desserts',
                'cuisine_type': 'Filipino Bakery',
                'rating': 4.2,
                'review_count': 1456,
                'delivery_time': '25-35 min',
                'delivery_fee': 59.00,
                'min_order': 250.00,
                'address': 'Metro Manila',
                'is_promoted': False,
                'image_url': 'https://images.unsplash.com/photo-1571115764595-644a1f56a55c?w=500'
            },
            {
                'name': 'Chowking',
                'description': 'Chinese-Filipino fusion cuisine with noodles, rice meals, and dim sum',
                'cuisine_type': 'Chinese-Filipino',
                'rating': 4.1,
                'review_count': 1789,
                'delivery_time': '20-30 min',
                'delivery_fee': 45.00,
                'min_order': 180.00,
                'address': 'Multiple Locations',
                'is_promoted': False,
                'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=500'
            },
            {
                'name': 'Kamayan sa Palaisdaan',
                'description': 'Traditional Filipino seafood and kamayan dining experience',
                'cuisine_type': 'Filipino Seafood',
                'rating': 4.6,
                'review_count': 892,
                'delivery_time': '30-45 min',
                'delivery_fee': 79.00,
                'min_order': 350.00,
                'address': 'Quezon City',
                'is_promoted': True,
                'discount_text': '15% OFF',
                'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=500'
            }
        ]

        # Menu items for each restaurant
        menu_items_data = {
            'Jollibee': [
                {'name': 'Chickenjoy', 'description': 'Crispy fried chicken with signature gravy', 'price': 89.00, 'category': 'Chicken', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=300'},
                {'name': 'Jolly Spaghetti', 'description': 'Sweet-style spaghetti with hotdog and cheese', 'price': 65.00, 'category': 'Pasta', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=300'},
                {'name': 'Yumburger', 'description': 'Juicy beef burger with special sauce', 'price': 45.00, 'category': 'Burgers', 'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=300'},
                {'name': 'Peach Mango Pie', 'description': 'Crispy pie filled with peach and mango', 'price': 35.00, 'category': 'Desserts', 'image_url': 'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=300'},
                {'name': 'Chicken Sandwich', 'description': 'Crispy chicken fillet sandwich', 'price': 75.00, 'category': 'Sandwiches', 'image_url': 'https://images.unsplash.com/photo-1606755962773-d324e9a13086?w=300'}
            ],
            'Mang Inasal': [
                {'name': 'Chicken Inasal', 'description': 'Grilled chicken marinated in special spices', 'price': 99.00, 'category': 'Grilled', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=300'},
                {'name': 'Pork BBQ', 'description': 'Grilled pork skewers with sweet sauce', 'price': 79.00, 'category': 'Grilled', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300'},
                {'name': 'Bangus Sisig', 'description': 'Sizzling milkfish sisig with egg', 'price': 129.00, 'category': 'Sisig', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300'},
                {'name': 'Unlimited Rice', 'description': 'Unlimited steamed rice', 'price': 25.00, 'category': 'Rice', 'image_url': 'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300'},
                {'name': 'Halo-Halo', 'description': 'Traditional Filipino shaved ice dessert', 'price': 69.00, 'category': 'Desserts', 'image_url': 'https://images.unsplash.com/photo-1563379091339-03246963d96c?w=300'}
            ],
            'Goldilocks': [
                {'name': 'Adobo Rice Bowl', 'description': 'Classic Filipino adobo with steamed rice', 'price': 119.00, 'category': 'Rice Bowls', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300'},
                {'name': 'Leche Flan', 'description': 'Creamy caramel custard dessert', 'price': 89.00, 'category': 'Desserts', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=300'},
                {'name': 'Palabok', 'description': 'Rice noodles with shrimp sauce and toppings', 'price': 95.00, 'category': 'Noodles', 'image_url': 'https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=300'},
                {'name': 'Ube Cake', 'description': 'Purple yam cake with ube frosting', 'price': 159.00, 'category': 'Cakes', 'image_url': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=300'},
                {'name': 'Ensaymada', 'description': 'Sweet bread with cheese and butter', 'price': 45.00, 'category': 'Pastries', 'image_url': 'https://images.unsplash.com/photo-1571115764595-644a1f56a55c?w=300'}
            ],
            'Chowking': [
                {'name': 'Beef Wanton Noodles', 'description': 'Egg noodles with beef and wanton dumplings', 'price': 109.00, 'category': 'Noodles', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=300'},
                {'name': 'Sweet & Sour Pork', 'description': 'Crispy pork with sweet and sour sauce', 'price': 139.00, 'category': 'Pork', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=300'},
                {'name': 'Siomai', 'description': 'Steamed pork dumplings (6 pieces)', 'price': 69.00, 'category': 'Dim Sum', 'image_url': 'https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=300'},
                {'name': 'Yang Chow Fried Rice', 'description': 'Special fried rice with mixed ingredients', 'price': 89.00, 'category': 'Rice', 'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=300'},
                {'name': 'Halo-Halo Supreme', 'description': 'Premium halo-halo with ice cream', 'price': 89.00, 'category': 'Desserts', 'image_url': 'https://images.unsplash.com/photo-1563379091339-03246963d96c?w=300'}
            ],
            'Kamayan sa Palaisdaan': [
                {'name': 'Grilled Tilapia', 'description': 'Fresh tilapia grilled with herbs and spices', 'price': 189.00, 'category': 'Seafood', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300'},
                {'name': 'Crispy Pata', 'description': 'Deep-fried pork knuckle, crispy outside tender inside', 'price': 299.00, 'category': 'Pork', 'is_popular': True, 'image_url': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300'},
                {'name': 'Kare-Kare', 'description': 'Oxtail stew in peanut sauce with vegetables', 'price': 249.00, 'category': 'Stews', 'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=300'},
                {'name': 'Sinigang na Baboy', 'description': 'Sour pork soup with vegetables', 'price': 199.00, 'category': 'Soups', 'image_url': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=300'},
                {'name': 'Buko Pie', 'description': 'Traditional coconut pie dessert', 'price': 129.00, 'category': 'Desserts', 'image_url': 'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=300'}
            ]
        }

        # Create restaurants and menu items
        for restaurant_data in restaurants_data:
            restaurant_data['slug'] = slugify(restaurant_data['name'])
            restaurant, created = Restaurant.objects.get_or_create(
                name=restaurant_data['name'],
                defaults=restaurant_data
            )
            
            if created:
                self.stdout.write(f'Created restaurant: {restaurant.name}')
                
                # Add menu items for this restaurant
                if restaurant.name in menu_items_data:
                    for item_data in menu_items_data[restaurant.name]:
                        MenuItem.objects.create(
                            restaurant=restaurant,
                            **item_data
                        )
                    self.stdout.write(f'Added {len(menu_items_data[restaurant.name])} menu items for {restaurant.name}')
            else:
                self.stdout.write(f'Restaurant {restaurant.name} already exists')

        self.stdout.write(self.style.SUCCESS('Successfully added Filipino restaurant data!'))