from django.core.management.base import BaseCommand
from core.models import Carrier

CARRIERS = [
    "Chubb",
    "Travelers",
    "Hartford",
    "Cincinnati Insurance",
    "Philadelphia Insurance"
]

class Command(BaseCommand):
    help = 'Seed the database with common insurance carriers.'

    def handle(self, *args, **kwargs):
        created_count = 0
        for name in CARRIERS:
            carrier, created = Carrier.objects.get_or_create(name=name)
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} carriers.'))