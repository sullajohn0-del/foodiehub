from django.core.management.base import BaseCommand
from myapp.models import Restaurant, MenuItem
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Add more Filipino cuisine restaurants and dishes'

    def handle(self, *args, **options):
        # Additional Filipino restaurants
        restaurants_data = [
            {
                'name': 'Max\'s Restaurant',
                'description': 'The House that Fried Chicken Built - serving Filipino comfort food since 1945',
                'cuisine_type': 'Filipino Comfort Food',
                'rating': 4.4,
                'review_count': 1567,
                'delivery_time': '25-35 min',
                'delivery_fee': 55.00,
                'min_order': 200.00,
                'address': 'Multiple Locations',
                'is_promoted': True,
                'discount_text': '10% OFF',
                'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=500'
            },
            {
                'name': 'Barrio Fiesta',
                'description': 'Authentic Filipino dishes in a traditional bahay kubo setting',
                'cuisine_type': 'Traditional Filipino',
                'rating': 4.2,
                'review_count': 892,
                'delivery_time': '30-40 min',
                'delivery_fee': 65.00,
                'min_order': 250.00,
                'address': 'Quezon City',
                'is_promoted': False,
                'image_url': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=500'
            },
            {
                'name': 'Aristocrat Restaurant',
                'description': 'Home of the original chicken barbecue and Filipino specialties',
                'cuisine_type': 'Filipino BBQ',
                'rating': 4.3,
                'review_count': 1234,
                'delivery_time': '20-30 min',
                'delivery_fee': 50.00,
                'min_order': 180.00,
                'address': 'Manila',
                'is_promoted': True,
                'discount_text': 'Free Delivery',
                'image_url': 'https://images.unsplash.com/photo-1544025162-d76694265947?w=500'
            },
            {
                'name': 'Pancake House',
                'description': 'Filipino-American fusion with pancakes, pasta, and local favorites',
                'cuisine_type': 'Filipino-American',
                'rating': 4.1,
                'review_count': 987,
                'delivery_time': '25-35 min',
                'delivery_fee': 60.00,
                'min_order': 220.00,
                'address': 'Metro Manila',
                'is_promoted': False,
                'image_url': 'https://images.unsplash.com/photo-1571115764595-644a1f56a55c?w=500'
            },
            {
                'name': 'Tapa King',
                'description': 'The king of Filipino breakfast - tapa, longsilog, and more',
                'cuisine_type': 'Filipino Breakfast',
                'rating': 4.0,
                'review_count': 756,
                'delivery_time': '15-25 min',
                'delivery_fee': 40.00,
                'min_order': 150.00,
                'address': 'Nationwide',
                'is_promoted': False,
                'image_url': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=500'
            }
        ]

        # Menu items for each restaurant
        menu_items_data = {
            'Max\'s Restaurant': [
                {'name': 'Max\'s Fried Chicken', 'description': 'The famous sarap-to-the-bones fried chicken', 'price': 149.00, 'category': 'Chicken', 'is_popular': True, 'calories': 420},
                {'name': 'Kare-Kare', 'description': 'Oxtail stew in rich peanut sauce with vegetables', 'price': 299.00, 'category': 'Filipino Dishes', 'is_popular': True, 'calories': 580},
                {'name': 'Pancit Canton', 'description': 'Stir-fried noodles with vegetables and meat', 'price': 189.00, 'category': 'Noodles', 'calories': 450},
                {'name': 'Lumpiang Shanghai', 'description': 'Crispy spring rolls with ground pork (8pcs)', 'price': 129.00, 'category': 'Appetizers', 'calories': 320},
                {'name': 'Caramel Bar', 'description': 'Max\'s signature caramel cake slice', 'price': 89.00, 'category': 'Desserts', 'calories': 280}
            ],
            'Barrio Fiesta': [
                {'name': 'Lechon Kawali', 'description': 'Crispy deep-fried pork belly with liver sauce', 'price': 259.00, 'category': 'Pork', 'is_popular': True, 'calories': 650},
                {'name': 'Pinakbet', 'description': 'Mixed vegetables with shrimp paste and pork', 'price': 169.00, 'category': 'Vegetables', 'is_vegetarian': True, 'calories': 220},
                {'name': 'Bulalo', 'description': 'Beef bone marrow soup with vegetables', 'price': 329.00, 'category': 'Soup', 'is_popular': True, 'calories': 480},
                {'name': 'Bicol Express', 'description': 'Spicy pork in coconut milk with chilies', 'price': 199.00, 'category': 'Spicy', 'is_spicy': True, 'calories': 420},
                {'name': 'Bibingka', 'description': 'Traditional rice cake with cheese and salted egg', 'price': 79.00, 'category': 'Desserts', 'calories': 180}
            ],
            'Aristocrat Restaurant': [
                {'name': 'Chicken Barbecue', 'description': 'The original Filipino-style grilled chicken', 'price': 179.00, 'category': 'BBQ', 'is_popular': True, 'calories': 380},
                {'name': 'Pork Barbecue', 'description': 'Grilled pork skewers with sweet marinade', 'price': 149.00, 'category': 'BBQ', 'is_popular': True, 'calories': 350},
                {'name': 'Beef Caldereta', 'description': 'Beef stew in tomato sauce with vegetables', 'price': 279.00, 'category': 'Beef', 'calories': 520},
                {'name': 'Crispy Pata', 'description': 'Deep-fried pork knuckle with soy-vinegar dip', 'price': 399.00, 'category': 'Pork', 'calories': 780},
                {'name': 'Mais Con Yelo', 'description': 'Corn with shaved ice, milk, and sugar', 'price': 69.00, 'category': 'Desserts', 'calories': 150}
            ],
            'Pancake House': [
                {'name': 'Blueberry Pancakes', 'description': 'Fluffy pancakes with fresh blueberries', 'price': 159.00, 'category': 'Pancakes', 'is_popular': True, 'calories': 420},
                {'name': 'Taco Rice', 'description': 'Filipino-style taco meat over rice', 'price': 189.00, 'category': 'Rice Meals', 'calories': 480},
                {'name': 'Spaghetti Bolognese', 'description': 'Filipino-style sweet spaghetti with meat sauce', 'price': 169.00, 'category': 'Pasta', 'calories': 520},
                {'name': 'Chicken Teriyaki', 'description': 'Grilled chicken with teriyaki glaze', 'price': 199.00, 'category': 'Chicken', 'calories': 380},
                {'name': 'Chocolate Cake', 'description': 'Rich chocolate layer cake', 'price': 99.00, 'category': 'Desserts', 'calories': 320}
            ],
            'Tapa King': [
                {'name': 'Tapsilog', 'description': 'Beef tapa with garlic rice and fried egg', 'price': 129.00, 'category': 'Silog Meals', 'is_popular': True, 'calories': 580},
                {'name': 'Longsilog', 'description': 'Longganisa with garlic rice and fried egg', 'price': 119.00, 'category': 'Silog Meals', 'is_popular': True, 'calories': 620},
                {'name': 'Bangsilog', 'description': 'Bangus with garlic rice and fried egg', 'price': 139.00, 'category': 'Silog Meals', 'calories': 520},
                {'name': 'Cornsilog', 'description': 'Corned beef with garlic rice and fried egg', 'price': 109.00, 'category': 'Silog Meals', 'calories': 540},
                {'name': 'Tsokolate', 'description': 'Traditional Filipino hot chocolate', 'price': 59.00, 'category': 'Beverages', 'calories': 180}
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
                            image_url=f'https://images.unsplash.com/photo-{self.get_image_id(item_data["category"])}?w=300',
                            **item_data
                        )
                    self.stdout.write(f'Added {len(menu_items_data[restaurant.name])} menu items for {restaurant.name}')
            else:
                self.stdout.write(f'Restaurant {restaurant.name} already exists')

        self.stdout.write(self.style.SUCCESS('Successfully added more Filipino cuisine restaurants!'))

    def get_image_id(self, category):
        image_map = {
            'Chicken': '1598515214211-89d3c73ae83b',
            'Filipino Dishes': '1565299624946-b28f40a0ca4b',
            'Noodles': '1621996346565-e3dbc353d2e5',
            'Appetizers': '1565299624946-b28f40a0ca4b',
            'Desserts': '1563379091339-03246963d96c',
            'Pork': '1544025162-d76694265947',
            'Vegetables': '1586201375761-83865001e31c',
            'Soup': '1547592166-23ac45744acd',
            'Spicy': '1565299624946-b28f40a0ca4b',
            'BBQ': '1544025162-d76694265947',
            'Beef': '1603133872878-684f208fb84b',
            'Pancakes': '1571115764595-644a1f56a55c',
            'Rice Meals': '1586201375761-83865001e31c',
            'Pasta': '1621996346565-e3dbc353d2e5',
            'Silog Meals': '1565299624946-b28f40a0ca4b',
            'Beverages': '1571115764595-644a1f56a55c'
        }
        return image_map.get(category, '1565299624946-b28f40a0ca4b')