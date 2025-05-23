from django.core.management.base import BaseCommand
from core.models import Question, Carrier, CoverageLine

class Command(BaseCommand):
    help = 'Seed the database with common insurance questions.'

    def handle(self, *args, **kwargs):
        # General questions
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

        # Carrier and coverage-specific questions
        # Example: Chubb + Cyber Liability
        chubb = Carrier.objects.filter(name="Chubb").first()
        cyber = CoverageLine.objects.filter(name="Cyber Liability").first()
        if chubb and cyber:
            specific_questions = [
                "Does your organization use multi-factor authentication for all remote access?",
                "Has your organization had a cybersecurity audit in the past 12 months?"
            ]
            for text in specific_questions:
                q, created = Question.objects.get_or_create(text=text)
                if created:
                    created_count += 1
                q.carriers.add(chubb)
                q.coverages.add(cyber)

        # Example: Travelers + General Liability
        travelers = Carrier.objects.filter(name="Travelers").first()
        general_liability = CoverageLine.objects.filter(name="General Liability").first()
        if travelers and general_liability:
            specific_questions = [
                "Does your organization host public events on its premises?",
                "Are there any ongoing renovations at your primary location?"
            ]
            for text in specific_questions:
                q, created = Question.objects.get_or_create(text=text)
                if created:
                    created_count += 1
                q.carriers.add(travelers)
                q.coverages.add(general_liability)

        # Example: Hartford + Workers' Compensation
        hartford = Carrier.objects.filter(name="Hartford").first()
        workers_comp = CoverageLine.objects.filter(name="Workers' Compensation").first()
        if hartford and workers_comp:
            specific_questions = [
                "Does your organization provide safety training for all employees?",
                "Has your organization had any workplace injuries in the past year?"
            ]
            for text in specific_questions:
                q, created = Question.objects.get_or_create(text=text)
                if created:
                    created_count += 1
                q.carriers.add(hartford)
                q.coverages.add(workers_comp)

        # Example: Cincinnati Insurance + Commercial Property
        cincy = Carrier.objects.filter(name="Cincinnati Insurance").first()
        prop = CoverageLine.objects.filter(name="Commercial Property").first()
        if cincy and prop:
            specific_questions = [
                "Does your organization have a central alarm system?",
                "Are all properties insured up to replacement cost?"
            ]
            for text in specific_questions:
                q, created = Question.objects.get_or_create(text=text)
                if created:
                    created_count += 1
                q.carriers.add(cincy)
                q.coverages.add(prop)

        # Example: Philadelphia Insurance + EPLI
        philly = Carrier.objects.filter(name="Philadelphia Insurance").first()
        epli = CoverageLine.objects.filter(name="Employment Practices Liability (EPLI)").first()
        if philly and epli:
            specific_questions = [
                "Does your organization provide annual anti-harassment training?",
                "Has your organization updated its employee handbook in the last 2 years?"
            ]
            for text in specific_questions:
                q, created = Question.objects.get_or_create(text=text)
                if created:
                    created_count += 1
                q.carriers.add(philly)
                q.coverages.add(epli)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} questions.'))