from django.core.management.base import BaseCommand
from jobs.models import Job, Tag
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populates the job table with sample data using Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Number of jobs to create'
        )

    def handle(self, *args, **kwargs):
        # Initialize Faker
        fake = Faker()
        count = kwargs['count']

        # Delete all existing jobs and tags
        Job.objects.all().delete()
        Tag.objects.all().delete()

        # Common tech job titles and skills for more realistic data
        tech_roles = [
            'Python Developer', 'Django Developer', 'FastAPI Developer',
            'Data Engineer', 'Machine Learning Engineer', 'Backend Engineer',
            'Full Stack Developer', 'DevOps Engineer', 'Site Reliability Engineer',
            'Software Architect'
        ]

        companies = [fake.company() for _ in range(10)]  # Generate a pool of companies

        # Philippine cities
        ph_cities = [
            'Manila', 'Makati', 'BGC', 'Ortigas', 'Quezon City', 'Cebu City',
            'Davao City', 'Pasig', 'Mandaluyong', 'Pasay'
        ]

        # Create tags
        tags = [
            Tag(name='Django'),
            Tag(name='FastAPI'),
            Tag(name='Pandas'),
            Tag(name='Automation')
        ]
        Tag.objects.bulk_create(tags)

        # Create jobs
        for _ in range(count):
            # Generate salary range (in thousands)
            min_salary = random.randint(40, 200)
            max_salary = min_salary + random.randint(20, 100)

            # Randomly decide seniority
            seniority = random.choice(['Junior', 'Mid-Level', 'Senior', 'Lead'])

            # Combine seniority with random tech role
            title = f"{seniority} {random.choice(tech_roles)}"

            job = Job.objects.create(
                title=title,
                company_name=random.choice(companies),
                location=random.choice(ph_cities),
                salary_range=f'₱{min_salary:,},000 - ₱{max_salary:,},000',
                short_description=fake.sentence(nb_words=15)[:100],
                description='\n'.join([
                    fake.paragraph(),
                    '\nKey Responsibilities:\n',
                    *[f'• {fake.sentence()}' for _ in range(4)],
                    '\nRequirements:\n',
                    *[f'• {fake.sentence()}' for _ in range(4)]
                ]),
                is_remote=random.choice([True, False, True])  # 66% chance of remote work
            )

            job.assigned_tags.add(*random.sample(tags, random.choice(range(1, 3))))  # add 1 or 2 tags

            self.stdout.write(
                self.style.SUCCESS(f'Created job: {job.title} at {job.company_name}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} jobs')
        ) 
