from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Product, Category
import random

class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **options):
        fake = Faker()

        # Create categories
        categories = ['Electronics', 'Clothing', 'Books', 'Home Appliances']

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)

        # Create products
        for _ in range(20):  # Create 20 products
            random_category = random.choice(Category.objects.all())
            Product.objects.create(
                name=fake.company(),
                price=random.uniform(10, 1000),  # Random price between 10 and 1000
                description=fake.text(),
                count=random.randint(1, 100),  # Random count between 1 and 100
                is_active=random.choice([True, False]),
                category=random_category
            )

        self.stdout.write(self.style.SUCCESS('Fake data generation complete.'))
