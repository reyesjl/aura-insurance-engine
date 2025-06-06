import uuid
from django.db import models

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
