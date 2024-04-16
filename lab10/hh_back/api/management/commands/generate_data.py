import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from api.models import Company, Vacancy

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake companies and vacancies data'

    def add_arguments(self, parser):
        parser.add_argument('num_companies', type=int, default=10, help='Number of companies to generate')
        parser.add_argument('num_vacancies', type=int, default=50, help='Number of vacancies to generate')

    def handle(self, *args, **options):
        num_companies = options['num_companies']
        num_vacancies = options['num_vacancies']

        self.generate_companies(num_companies)
        self.generate_vacancies(num_vacancies, num_companies)

        self.stdout.write(self.style.SUCCESS("Data generation completed."))

    def generate_companies(self, num_companies):
        for _ in range(num_companies):
            company = Company.objects.create(
                name=fake.company(),
                description=fake.text(),
                city=fake.city(),
                address=fake.address(),
            )
            self.stdout.write(self.style.SUCCESS(f"Created Company: {company}"))

    def generate_vacancies(self, num_vacancies, num_companies):
        companies = list(Company.objects.all())
        for _ in range(num_vacancies):
            vacancy = Vacancy.objects.create(
                name=fake.job(),
                description=fake.text(),
                salary=random.uniform(30000, 100000),  # Adjust salary range as needed
                company=random.choice(companies),
            )
            self.stdout.write(self.style.SUCCESS(f"Created Vacancy: {vacancy}"))
