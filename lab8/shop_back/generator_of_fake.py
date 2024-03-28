from faker import Faker
from api.models import Product, Category
import random

fake = Faker()

# Create categories
categories = ['Electronics', 'Clothing', 'Books', 'Home Appliances']

for category_name in categories:
    Category.objects.create(name=category_name)

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

# Print confirmation message
print("Fake data generation complete.")
