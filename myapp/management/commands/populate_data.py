from django.core.management.base import BaseCommand
from myapp.models import Restaurant, MenuItem, MenuItemVariant


class Command(BaseCommand):
    help = 'Populate database with sample Filipino restaurants and dishes'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample Filipino food data...')

        # Clear existing data
        Restaurant.objects.all().delete()
        MenuItem.objects.all().delete()

        # Restaurant 1: Lutong Bahay
        lutong_bahay = Restaurant.objects.create(
            name='Lutong Bahay',
            slug='lutong-bahay',
            description='Authentic home-style Filipino cooking with traditional recipes passed down through generations',
            image_url='https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=1200&auto=format&fit=crop',
            cuisine_type='Filipino • Home-style',
            rating=4.9,
            review_count=1850,
            delivery_time='25-35 min',
            delivery_fee=50.00,
            min_order=150.00,
            address='123 Rizal Street, Makati',
            is_promoted=True,
            discount_text='20% OFF',
            is_active=True
        )

        item1 = MenuItem.objects.create(
            restaurant=lutong_bahay,
            name='Adobo',
            description='Classic Filipino adobo with tender pork or chicken marinated in soy sauce, vinegar, and garlic. Served with steamed rice.',
            price=120.00,
            image_url='https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=1200&auto=format&fit=crop',
            category='Main Course',
            is_popular=True,
            calories=450,
            prep_time='20 min',
            is_available=True
        )
        MenuItemVariant.objects.create(menu_item=item1, name='Pork', price=120.00)
        MenuItemVariant.objects.create(menu_item=item1, name='Chicken', price=120.00)
        MenuItemVariant.objects.create(menu_item=item1, name='Combo (Both)', price=150.00)

        MenuItem.objects.create(
            restaurant=lutong_bahay,
            name='Sinigang',
            description='Sour tamarind soup with pork ribs, vegetables, and rice. A Filipino comfort food favorite.',
            price=130.00,
            image_url='https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1200&auto=format&fit=crop',
            category='Soup',
            is_popular=True,
            calories=380,
            prep_time='25 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=lutong_bahay,
            name='Lechon Kawali',
            description='Crispy deep-fried pork belly served with rice and special sauce. Perfectly golden and crunchy.',
            price=140.00,
            image_url='https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop',
            category='Main Course',
            is_popular=True,
            calories=620,
            prep_time='30 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=lutong_bahay,
            name='Lumpia',
            description='Crispy spring rolls filled with vegetables and meat, served with sweet and sour sauce.',
            price=80.00,
            image_url='https://images.unsplash.com/photo-1565299585323-38174c26b4e1?q=80&w=1200&auto=format&fit=crop',
            category='Appetizer',
            is_vegetarian=False,
            calories=180,
            prep_time='10 min',
            is_available=True
        )

        # Restaurant 2: Sisig Express
        sisig_express = Restaurant.objects.create(
            name='Sisig Express',
            slug='sisig-express',
            description='Specializing in authentic Kapampangan cuisine, especially our famous sizzling sisig',
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            cuisine_type='Filipino • Kapampangan',
            rating=4.8,
            review_count=1240,
            delivery_time='20-30 min',
            delivery_fee=40.00,
            min_order=120.00,
            address='456 EDSA, Quezon City',
            is_promoted=True,
            discount_text='Free Delivery',
            is_active=True
        )

        item2 = MenuItem.objects.create(
            restaurant=sisig_express,
            name='Sisig',
            description='Sizzling pork sisig served on a hot plate with egg, onions, and chili. A Kapampangan specialty.',
            price=130.00,
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            category='Main Course',
            is_popular=True,
            is_spicy=True,
            calories=520,
            prep_time='15 min',
            is_available=True
        )
        MenuItemVariant.objects.create(menu_item=item2, name='Regular', price=130.00)
        MenuItemVariant.objects.create(menu_item=item2, name='Large', price=150.00)
        MenuItemVariant.objects.create(menu_item=item2, name='With Egg', price=140.00)

        MenuItem.objects.create(
            restaurant=sisig_express,
            name='Crispy Pata',
            description='Deep-fried pork leg served with soy-vinegar dipping sauce. Crispy on the outside, tender inside.',
            price=150.00,
            image_url='https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop',
            category='Main Course',
            is_popular=True,
            calories=750,
            prep_time='35 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=sisig_express,
            name='Kare-Kare',
            description='Rich peanut-based stew with oxtail, vegetables, and bagoong (shrimp paste). Served with rice.',
            price=140.00,
            image_url='https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1200&auto=format&fit=crop',
            category='Main Course',
            is_popular=True,
            calories=580,
            prep_time='40 min',
            is_available=True
        )

        # Restaurant 3: Tapsilog Station
        tapsilog_station = Restaurant.objects.create(
            name='Tapsilog Station',
            slug='tapsilog-station',
            description='Your go-to place for authentic Filipino breakfast and silog meals, open 24/7',
            image_url='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?q=80&w=1200&auto=format&fit=crop',
            cuisine_type='Filipino • Silog Meals',
            rating=4.7,
            review_count=2100,
            delivery_time='15-25 min',
            delivery_fee=30.00,
            min_order=100.00,
            address='789 Taft Avenue, Manila',
            is_active=True
        )

        item3 = MenuItem.objects.create(
            restaurant=tapsilog_station,
            name='Tapsilog',
            description='Marinated beef tapa, garlic fried rice, and sunny-side-up egg. The classic Filipino breakfast combo.',
            price=95.00,
            image_url='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?q=80&w=1200&auto=format&fit=crop',
            category='Silog Meals',
            is_popular=True,
            calories=550,
            prep_time='12 min',
            is_available=True
        )
        MenuItemVariant.objects.create(menu_item=item3, name='Regular', price=95.00)
        MenuItemVariant.objects.create(menu_item=item3, name='Extra Rice', price=110.00)
        MenuItemVariant.objects.create(menu_item=item3, name='Double Egg', price=110.00)

        MenuItem.objects.create(
            restaurant=tapsilog_station,
            name='Longsilog',
            description='Sweet Filipino longganisa, garlic rice, and egg. A breakfast favorite.',
            price=90.00,
            image_url='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?q=80&w=1200&auto=format&fit=crop',
            category='Silog Meals',
            is_popular=True,
            calories=480,
            prep_time='10 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=tapsilog_station,
            name='Tocino',
            description='Sweet cured pork served with garlic rice and egg. Perfectly caramelized and tender.',
            price=95.00,
            image_url='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?q=80&w=1200&auto=format&fit=crop',
            category='Silog Meals',
            is_popular=True,
            calories=520,
            prep_time='12 min',
            is_available=True
        )

        # Restaurant 4: Halo-Halo Paradise
        halo_halo_paradise = Restaurant.objects.create(
            name='Halo-Halo Paradise',
            slug='halo-halo-paradise',
            description='Cool down with authentic Filipino desserts and refreshing drinks',
            image_url='https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1200&auto=format&fit=crop',
            cuisine_type='Filipino • Desserts',
            rating=4.9,
            review_count=890,
            delivery_time='15-20 min',
            delivery_fee=30.00,
            min_order=80.00,
            address='321 BGC, Taguig',
            is_active=True
        )

        item4 = MenuItem.objects.create(
            restaurant=halo_halo_paradise,
            name='Halo-Halo',
            description='Traditional Filipino shaved ice dessert with sweet beans, fruits, leche flan, ube, and evaporated milk.',
            price=85.00,
            image_url='https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1200&auto=format&fit=crop',
            category='Desserts',
            is_popular=True,
            is_vegetarian=True,
            calories=320,
            prep_time='5 min',
            is_available=True
        )
        MenuItemVariant.objects.create(menu_item=item4, name='Regular', price=85.00)
        MenuItemVariant.objects.create(menu_item=item4, name='Special (Extra Toppings)', price=110.00)
        MenuItemVariant.objects.create(menu_item=item4, name='Premium (With Ice Cream)', price=130.00)

        MenuItem.objects.create(
            restaurant=halo_halo_paradise,
            name='Leche Flan',
            description='Creamy caramel custard dessert. Rich, smooth, and perfectly sweet.',
            price=80.00,
            image_url='https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1200&auto=format&fit=crop',
            category='Desserts',
            is_popular=True,
            is_vegetarian=True,
            calories=280,
            prep_time='3 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=halo_halo_paradise,
            name='Ube Halaya',
            description='Sweet purple yam jam served with coconut. A Filipino dessert classic.',
            price=90.00,
            image_url='https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1200&auto=format&fit=crop',
            category='Desserts',
            is_vegetarian=True,
            calories=350,
            prep_time='3 min',
            is_available=True
        )

        # Restaurant 5: Pancit House
        pancit_house = Restaurant.objects.create(
            name='Pancit House',
            slug='pancit-house',
            description='Authentic Filipino noodles and pancit dishes from different regions',
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            cuisine_type='Filipino • Noodles',
            rating=4.6,
            review_count=1560,
            delivery_time='20-30 min',
            delivery_fee=50.00,
            min_order=120.00,
            address='654 Ortigas Avenue, Pasig',
            is_active=True
        )

        MenuItem.objects.create(
            restaurant=pancit_house,
            name='Pancit Canton',
            description='Stir-fried noodles with vegetables, meat, and soy sauce. A Filipino party favorite.',
            price=110.00,
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            category='Noodles',
            is_popular=True,
            calories=420,
            prep_time='15 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=pancit_house,
            name='Pancit Bihon',
            description='Thin rice noodles stir-fried with vegetables, meat, and shrimp. Light and flavorful.',
            price=100.00,
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            category='Noodles',
            is_popular=True,
            calories=380,
            prep_time='15 min',
            is_available=True
        )

        MenuItem.objects.create(
            restaurant=pancit_house,
            name='Pancit Palabok',
            description='Rice noodles with rich orange sauce, shrimp, pork, and crispy toppings.',
            price=120.00,
            image_url='https://images.unsplash.com/photo-1559314809-0d155014e29e?q=80&w=1200&auto=format&fit=crop',
            category='Noodles',
            is_popular=True,
            calories=450,
            prep_time='18 min',
            is_available=True
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {Restaurant.objects.count()} Filipino restaurants'))
        self.stdout.write(self.style.SUCCESS(f'Successfully created {MenuItem.objects.count()} Filipino dishes'))
