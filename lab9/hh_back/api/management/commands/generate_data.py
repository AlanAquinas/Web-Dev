import random

from django.core.management import BaseCommand
from faker import Faker
from django.utils import timezone

from hh_back.api.models import Company, Vacancy

fake = Faker()

class Command(BaseCommand):
    def generate_companies(num_companies):
        for _ in range(num_companies):
            company = Company.objects.create(
                name=fake.company(),
                description=fake.text(),
                city=fake.city(),
                address=fake.address(),
            )
            yield company

    def generate_vacancies(num_vacancies, num_companies):
        companies = list(Company.objects.all())
        for _ in range(num_vacancies):
            vacancy = Vacancy.objects.create(
                name=fake.job(),
                description=fake.text(),
                salary=random.uniform(30000, 100000),  # Adjust salary range as needed
                company=random.choice(companies),
            )
            yield vacancy

    # Usage example:
    # Generate 10 companies and 50 vacancies
    num_companies = 10
    num_vacancies = 50

    companies_generator = generate_companies(num_companies)
    vacancies_generator = generate_vacancies(num_vacancies, num_companies)

    # You can iterate over the generators to create and save objects
    for company in companies_generator:
        print(f"Created Company: {company}")

    for vacancy in vacancies_generator:
        print(f"Created Vacancy: {vacancy}")
