from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = ['Ocean View', 'Mountain Retreat',
                  'Urban Flat', 'Countryside Cottage']
        locations = ['Addis Ababa', 'Bahir Dar', 'Hawassa', 'Gondar']

        for _ in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description='Great place to stay.',
                location=random.choice(locations),
                price_per_night=random.randint(50, 300),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database.'))