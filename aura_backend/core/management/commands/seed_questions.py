from django.core.management.base import BaseCommand
from core.models import Question

class Command(BaseCommand):
    help = 'Seed the database with common insurance questions.'

    def handle(self, *args, **kwargs):
        questions = [
            "What is the legal name of the organization?",
            "What is the principal business address?",
            "In what year was the organization established?",
            "Is the organization tax-exempt under IRS rules?",
            "What is the organization's total annual revenue?",
            "How many full-time employees does the organization have?",
            "Has the organization experienced any layoffs or reorganizations in the last 18 months?",
            "Does the organization have written anti-discrimination policies?",
            "Has the organization had any claims or lawsuits in the past 5 years?",
            "What was the largest claim value in the past 5 years?",
            "Does the organization have any subsidiaries?",
            "Does the organization verify invoices against purchase orders?",
            "Does the organization conduct background checks for new employees?",
            "How many physical locations does the organization operate?"
        ]

        created_count = 0
        for text in questions:
            q, created = Question.objects.get_or_create(text=text)
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} questions.'))