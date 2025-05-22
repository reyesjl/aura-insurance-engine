from django.core.management.base import BaseCommand
from core.models import CoverageLine

COVERAGE_LINES = [
    "General Liability",
    "Workers' Compensation",
    "Cyber Liability",
    "Professional Liability (E&O)",
    "Directors & Officers (D&O)",
    "Employment Practices Liability (EPLI)",
    "Fiduciary Liability",
    "Commercial Property",
    "Business Owner’s Policy (BOP)",
    "Crime Insurance"
]

class Command(BaseCommand):
    help = 'Seed the database with standard insurance lines of coverage.'

    def handle(self, *args, **kwargs):
        created_count = 0
        for name in COVERAGE_LINES:
            coverage, created = CoverageLine.objects.get_or_create(name=name)
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} coverage lines.'))