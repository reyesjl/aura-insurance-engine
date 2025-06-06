import random
from django.core.management.base import BaseCommand
from core.models import InsuranceType, Carrier, CoverageLine, Question

class Command(BaseCommand):
    help = "Seeds initial insurance data with 100 unique questions for development."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding insurance types...")
        personal = InsuranceType.objects.get_or_create(key="personal", label="Personal")[0]
        commercial = InsuranceType.objects.get_or_create(key="commercial", label="Commercial")[0]

        self.stdout.write("Seeding carriers...")
        carrier_names = [
            "Acme Insurance", "GloboCoverage", "Universal Trust", "Titan Assurance",
            "Zenith Mutual", "Ironclad Risk", "MapleShield", "Redline Insurance"
        ]
        carriers = []
        for name in carrier_names:
            carrier = Carrier.objects.get_or_create(name=name)[0]
            # Randomly associate with personal, commercial, or both
            assigned_types = random.sample([personal, commercial], k=random.choice([1, 2]))
            carrier.insurance_types.set(assigned_types)
            carriers.append(carrier)

        self.stdout.write("Seeding coverage lines...")
        cov_auto = CoverageLine.objects.get_or_create(name="Auto")[0]
        cov_gl = CoverageLine.objects.get_or_create(name="General Liability")[0]
        cov_cyber = CoverageLine.objects.get_or_create(name="Cyber")[0]
        coverages = [cov_auto, cov_gl, cov_cyber]

        cov_auto.insurance_types.set([personal])
        cov_gl.insurance_types.set([commercial])
        cov_cyber.insurance_types.set([personal, commercial])

        self.stdout.write("Generating 100 unique questions...")
        questions = [
            # Personal - Auto
            "What is the vehicle's make?",
            "What is the vehicle's model?",
            "What year was the vehicle manufactured?",
            "Is this your primary vehicle?",
            "Do you use the vehicle for commuting?",
            "Is the vehicle financed or leased?",
            "How many miles does the vehicle drive annually?",
            "Is the vehicle parked in a garage overnight?",
            "Has the vehicle been modified from factory specifications?",
            "Do you have anti-theft devices installed?",
            "What is the vehicle’s VIN?",
            "Do you use the vehicle for ride-sharing services?",
            "Are there any other drivers on the policy?",
            "Have you had any at-fault accidents in the past 5 years?",
            "Have you received any traffic violations in the past 3 years?",
            "What is your current deductible amount?",
            "Do you carry comprehensive coverage?",
            "Do you carry collision coverage?",
            "Do you want roadside assistance included?",
            "Is the title of the vehicle in your name?",

            # Personal – Cyber
            "Do you store passwords digitally?",
            "Do you use a password manager?",
            "Is your home Wi-Fi password-protected?",
            "Do you back up your data regularly?",
            "Have you experienced identity theft before?",
            "Do you use antivirus software?",
            "Are your devices encrypted?",
            "Do you use multi-factor authentication for email?",
            "Have you shopped online in the past 6 months?",
            "Do you use public Wi-Fi regularly?",
            "Is your personal information shared with third-party apps?",
            "Do you use biometric authentication (fingerprint/face ID)?",
            "Do you want identity theft protection included?",
            "Have you clicked on suspicious email links in the past?",
            "Have you lost a personal device in the last year?",

            # Commercial – GL
            "What is your business type?",
            "How many employees do you have?",
            "What is your annual revenue?",
            "Do customers visit your business premises?",
            "Have you had any liability claims in the past 5 years?",
            "Do you host events for clients?",
            "Do you subcontract any services?",
            "Do you operate out of multiple locations?",
            "Do you sell physical products?",
            "Are safety training programs in place?",
            "Is your business insured elsewhere?",
            "Do you require coverage for third-party property damage?",
            "Do you use temporary workers?",
            "Have you changed business names in the past 5 years?",
            "Do you provide professional services or advice?",
            "Do you store hazardous materials?",
            "Are your employees covered by workers’ compensation?",
            "Do you have existing lawsuits or pending legal action?",
            "Do you advertise using customer testimonials?",
            "Are drones used for any business operations?",

            # Commercial – Cyber
            "Do you collect customer SSNs or sensitive information?",
            "Do you use a third-party payment processor?",
            "Do you maintain a cybersecurity policy?",
            "Is sensitive customer data encrypted in storage?",
            "Do employees receive cybersecurity training?",
            "Have you ever experienced a data breach?",
            "Do you monitor network traffic?",
            "Is endpoint protection deployed across all devices?",
            "Are software patches applied monthly?",
            "Is there a data recovery plan in place?",
            "Are employees required to change passwords regularly?",
            "Do you carry cyber liability coverage with another provider?",
            "Do you allow remote access to company systems?",
            "Is cloud storage used for confidential files?",
            "Do vendors have access to your data systems?",

            # Commercial – Auto
            "How many commercial vehicles do you operate?",
            "Are vehicles used across state lines?",
            "Do employees use personal vehicles for business?",
            "Are vehicles equipped with GPS tracking?",
            "Are drivers subject to background checks?",
            "What are the operating hours for your fleet?",
            "Are your commercial vehicles marked with company branding?",
            "Is cargo transported as part of business operations?",
            "Do you hire independent contractors as drivers?",
            "Are driving records monitored for all employees?",

            # Shared / Misc
            "What is your preferred policy start date?",
            "Do you require bundled coverage?",
            "Are you switching from a current provider?",
            "Have you had coverage denied in the past?",
            "Do you work with an insurance broker?",
            "How soon do you need coverage to start?",
            "Are you interested in multi-policy discounts?",
            "Do you require monthly billing?",
            "Do you need coverage for multiple addresses?",
            "Do you want coverage to include mobile devices?",
            "Is umbrella coverage needed?",
            "Will this policy replace an existing one?",
            "Do you have existing claims not yet settled?",
            "Have you filed for bankruptcy in the last 7 years?",
            "Is your contact information up to date?",
            "Do you want a PDF summary after submitting?",
            "Will someone else complete this form on your behalf?",
            "Do you need document signing capabilities?",
            "Would you like to schedule a follow-up call?",
            "Do you consent to digital communication?"
        ]

        for i, q_text in enumerate(questions, 1):
            coverage = random.choice(coverages)
            insurance_type = random.choice([personal, commercial])
            valid_carriers = [c for c in carriers if insurance_type in c.insurance_types.all()]
            selected_carriers = random.sample(valid_carriers, k=random.randint(1, len(valid_carriers)))

            question = Question.objects.create(text=q_text)
            question.coverages.set([coverage])
            question.carriers.set(selected_carriers)
            question.insurance_types.set([insurance_type])

        self.stdout.write(self.style.SUCCESS("✅ 100 questions seeded successfully."))
