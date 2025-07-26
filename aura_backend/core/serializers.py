#
# Aura Insurance Engine – Proprietary Software
#
# Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
#
# This software was developed solely by Jose Reyes – full-stack engineer and designer.
# Jacob Powers contributed as the licensed insurance agent for the project.
# It is a modern insurance submission platform built to streamline the intake
# and processing of insurance applications.
#
# This code is proprietary and confidential. Unauthorized use, reproduction,
# distribution, or modification is strictly prohibited.
#
# Project repository: https://github.com/reyesjl/aura-insurance-engine
# DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
#

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    ApplicationAnswer,
    ApplicationSession,
    ApplicationTemplate,
    Carrier,
    CoverageLine,
    InsuranceType,
    Question,
    Submission,
    TemplateQuestionSnapshot,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_agent",
            "agent_name",
            "agency",
            "phone_number",
            "level",
            "xp",
            # add other fields as needed
        ]


class InsuranceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceType
        fields = ["id", "key", "label"]


class CarrierSerializer(serializers.ModelSerializer):
    insurance_types = InsuranceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Carrier
        fields = ["id", "name", "insurance_types"]


class CoverageLineSerializer(serializers.ModelSerializer):
    insurance_types = InsuranceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = CoverageLine
        fields = ["id", "name", "abbreviation", "insurance_types"]


class QuestionSerializer(serializers.ModelSerializer):
    coverages = CoverageLineSerializer(many=True, read_only=True)
    carriers = CarrierSerializer(many=True, read_only=True)
    insurance_types = InsuranceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "carriers", "coverages", "insurance_types"]


class ApplicationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationTemplate
        fields = [
            "id",
            "agent",
            "name",
            "insurance_type",
            "carriers",
            "coverages",
            "created_at",
        ]


class TemplateQuestionSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateQuestionSnapshot
        fields = ["id", "template", "original_question", "question_text"]


class ApplicationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSession
        fields = [
            "id",
            "template",
            "agent",
            "token",
            "name",
            "insured_email",
            "created_at",
            "status",
        ]


class ApplicationAnswerSerializer(serializers.ModelSerializer):
    question_snapshot = TemplateQuestionSnapshotSerializer(read_only=True)

    class Meta:
        model = ApplicationAnswer
        fields = ["id", "session", "question_snapshot", "answer"]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "session", "submitted_at"]
