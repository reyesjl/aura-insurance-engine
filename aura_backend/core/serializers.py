from rest_framework import serializers
from .models import (
    InsuranceType, Carrier, CoverageLine, Question,
    ApplicationTemplate, TemplateQuestionSnapshot,
    ApplicationSession, ApplicationAnswer, Submission
)

class InsuranceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceType
        fields = ['id', 'key', 'label']

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'insurance_types']

class CoverageLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverageLine
        fields = ['id', 'name', 'abbreviation', 'insurance_types']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'carriers', 'coverages', 'insurance_types']

class ApplicationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationTemplate
        fields = [
            'id', 'name', 'insurance_type', 'carriers',
            'coverages', 'created_at'
        ]

class TemplateQuestionSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateQuestionSnapshot
        fields = [
            'id', 'template', 'original_question', 'question_text'
        ]

class ApplicationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSession
        fields = [
            'id', 'template', 'token', 'name', 'created_at', 'status'
        ]

class ApplicationAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationAnswer
        fields = [
            'id', 'session', 'question_snapshot', 'answer'
        ]

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'id', 'session', 'submitted_at'
        ]