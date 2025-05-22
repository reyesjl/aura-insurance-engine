import uuid
from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=100)

class CoverageLine(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    text = models.TextField()
    carriers = models.ManyToManyField(Carrier, blank=True)
    coverages = models.ManyToManyField(CoverageLine, blank=True)

class ApplicationSession(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    carriers = models.ManyToManyField(Carrier)
    coverages = models.ManyToManyField(CoverageLine)
    status = models.CharField(default='pending', max_length=20)

class Submission(models.Model):
    session = models.OneToOneField(ApplicationSession, on_delete=models.CASCADE)
    answers = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)