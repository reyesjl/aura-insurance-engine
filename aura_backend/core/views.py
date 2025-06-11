from rest_framework import viewsets
from .models import (
    InsuranceType, Carrier, CoverageLine, Question,
    ApplicationTemplate, TemplateQuestionSnapshot,
    ApplicationSession, ApplicationAnswer, Submission
)
from .serializers import (
    InsuranceTypeSerializer, CarrierSerializer, CoverageLineSerializer, QuestionSerializer,
    ApplicationTemplateSerializer, TemplateQuestionSnapshotSerializer,
    ApplicationSessionSerializer, ApplicationAnswerSerializer, SubmissionSerializer
)

class InsuranceTypeViewSet(viewsets.ModelViewSet):
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer

class CarrierViewSet(viewsets.ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

class CoverageLineViewSet(viewsets.ModelViewSet):
    queryset = CoverageLine.objects.all()
    serializer_class = CoverageLineSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ApplicationTemplateViewSet(viewsets.ModelViewSet):
    queryset = ApplicationTemplate.objects.all()
    serializer_class = ApplicationTemplateSerializer

class TemplateQuestionSnapshotViewSet(viewsets.ModelViewSet):
    queryset = TemplateQuestionSnapshot.objects.all()
    serializer_class = TemplateQuestionSnapshotSerializer

class ApplicationSessionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationSession.objects.all()
    serializer_class = ApplicationSessionSerializer

class ApplicationAnswerViewSet(viewsets.ModelViewSet):
    queryset = ApplicationAnswer.objects.all()
    serializer_class = ApplicationAnswerSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer