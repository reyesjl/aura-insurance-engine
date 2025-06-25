import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# --- User Model ---

class User(AbstractUser):
    """
    Custom user model for agents and platform users.

    Inherits all fields from AbstractUser, including:
        - id
        - password
        - last_login
        - is_superuser
        - username
        - first_name
        - last_name
        - email                                                 # Expected for drfpassworless login
        - is_staff
        - is_active
        - date_joined
        - groups
        - user_permissions

    Custom fields below:
        - is_agent: Boolean, True if user is an agent
        - agent_name: Optional, agent's display name
        - agency: Optional, agency name
        - phone_number: Optional, agent's phone number          # Expected for drfpassworless login
        - level: Integer, agent's level for gamification
        - xp: Integer, experience points for achievements
        - (future) achievements: ManyToMany to Achievement model
    """
    is_agent = models.BooleanField(default=False)
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=0)
    # achievements = models.ManyToManyField('Achievement', blank=True)  # Uncomment when Achievement model is added

    def __str__(self):
        return self.agent_name or self.username

# --- Core Classifications ---

class InsuranceType(models.Model):
    """
    Represents the type of insurance: Personal, Commercial, or both.
    Used to scope carriers, coverage lines, and questions.
    """
    key = models.CharField(max_length=50, unique=True)  # e.g. "personal", "commercial"
    label = models.CharField(max_length=100)            # e.g. "Personal", "Commercial"

    def __str__(self):
        return self.label


# --- Business Entities ---

class Carrier(models.Model):
    """
    Represents an insurance carrier (e.g., Chubb, Travelers).
    Can be associated with one or more insurance types.
    """
    name = models.CharField(max_length=100)
    insurance_types = models.ManyToManyField(InsuranceType)

    def __str__(self):
        return self.name


class CoverageLine(models.Model):
    """
    Represents a line of insurance coverage (e.g., General Liability, Cyber).
    Also scoped by insurance types.
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20, blank=True, null=True)  # e.g., "GL", "Cyber"
    insurance_types = models.ManyToManyField(InsuranceType)

    def __str__(self):
        return self.name


# --- Questions and Snapshots ---

class Question(models.Model):
    """
    A master question that may apply to certain carriers, coverages, and insurance types.
    Questions can be reused, and only relevant ones are snapshotted into templates.
    """
    text = models.TextField()
    carriers = models.ManyToManyField(Carrier, blank=True)
    coverages = models.ManyToManyField(CoverageLine, blank=True)
    insurance_types = models.ManyToManyField(InsuranceType)

    def __str__(self):
        return self.text[:50]


class ApplicationTemplate(models.Model):
    """
    A named group of carrier + coverage + insurance type selections.
    It stores a static question snapshot so changes to the base questions do not affect existing templates.
    """
    name = models.CharField(max_length=255)
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='application_templates',
        null=True, blank=True
    )
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.PROTECT)
    carriers = models.ManyToManyField(Carrier)
    coverages = models.ManyToManyField(CoverageLine)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TemplateQuestionSnapshot(models.Model):
    """
    Snapshotted question at the moment a template is created.
    This preserves the text and question identity even if the original question changes.
    """
    template = models.ForeignKey(ApplicationTemplate, related_name='question_snapshots', on_delete=models.CASCADE)
    original_question = models.ForeignKey(Question, on_delete=models.PROTECT)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text[:50]


# --- Application Sessions & Answers ---

class ApplicationSession(models.Model):
    """
    An instance of a form session generated from a template.
    It holds a secure UUID token and is tied to the original template and question snapshots.
    """
    template = models.ForeignKey(ApplicationTemplate, on_delete=models.PROTECT)
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='application_sessions',
        null=True, blank=True
    )
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='pending', max_length=20)

    def __str__(self):
        return f"{self.name or self.token}"


class ApplicationAnswer(models.Model):
    """
    An answer to a specific question snapshot, tied to a session.
    This model ensures immutability of the original question and supports tracking progress.
    """
    session = models.ForeignKey(ApplicationSession, related_name='answers', on_delete=models.CASCADE)
    question_snapshot = models.ForeignKey(TemplateQuestionSnapshot, on_delete=models.PROTECT)
    answer = models.TextField(blank=True)

    def __str__(self):
        return f"Answer to {self.question_snapshot.question_text[:30]}..."


# --- Submission ---

class Submission(models.Model):
    """
    A finalized submission for a session.
    Only one submission per session is allowed.
    """
    session = models.OneToOneField(ApplicationSession, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission for {self.session}"
