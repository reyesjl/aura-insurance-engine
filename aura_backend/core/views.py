import time
import django
import platform
from rest_framework import viewsets
from datetime import timedelta, datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAgentUser

# Starttime for uptime tracking
APP_START_TIME = time.time()

from .models import (
    User,
    InsuranceType,
    Carrier,
    CoverageLine,
    Question,
    ApplicationTemplate,
    TemplateQuestionSnapshot,
    ApplicationSession,
    ApplicationAnswer,
    Submission,
)
from .serializers import (
    UserSerializer,
    InsuranceTypeSerializer,
    CarrierSerializer,
    CoverageLineSerializer,
    QuestionSerializer,
    ApplicationTemplateSerializer,
    TemplateQuestionSnapshotSerializer,
    ApplicationSessionSerializer,
    ApplicationAnswerSerializer,
    SubmissionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAgentUser]


class InsuranceTypeViewSet(viewsets.ModelViewSet):
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer
    permission_classes = [IsAgentUser]


class CarrierViewSet(viewsets.ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    permission_classes = [IsAgentUser]


class CoverageLineViewSet(viewsets.ModelViewSet):
    queryset = CoverageLine.objects.all()
    serializer_class = CoverageLineSerializer
    permission_classes = [IsAgentUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAgentUser]


class ApplicationTemplateViewSet(viewsets.ModelViewSet):
    queryset = ApplicationTemplate.objects.all()
    serializer_class = ApplicationTemplateSerializer
    permission_classes = [IsAgentUser]


class TemplateQuestionSnapshotViewSet(viewsets.ModelViewSet):
    queryset = TemplateQuestionSnapshot.objects.all()
    serializer_class = TemplateQuestionSnapshotSerializer
    permission_classes = [IsAgentUser]


class ApplicationSessionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationSession.objects.all()
    serializer_class = ApplicationSessionSerializer
    permission_classes = [IsAgentUser]


class ApplicationAnswerViewSet(viewsets.ModelViewSet):
    queryset = ApplicationAnswer.objects.all()
    serializer_class = ApplicationAnswerSerializer
    permission_classes = [IsAgentUser]


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAgentUser]


class ApiInfo(APIView):
    """
    Public endpoint providing API and platform information.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "platform": "Aura",
                "description": "Aura Insurance Engine Backend API",
                "django_version": django.get_version(),
                "python_version": platform.python_version(),
                "app_version": "1.0.0",
            }
        )


class ApiHealth(APIView):
    """
    Public endpoint for health checks (minimal, for uptime/ping).
    """

    permission_classes = [AllowAny]

    def get(self, request):
        uptime_seconds = int(time.time() - APP_START_TIME)
        uptime_str = str(timedelta(seconds=uptime_seconds))
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            greeting = "Good morning, Agent."
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon, Agent."
        elif 18 <= current_hour < 22:
            greeting = "Good evening, Agent."
        else:
            greeting = "It's late, Agent. All systems remain vigilant."

        return Response(
            {
                "status": "ok",
                "message": f"{greeting} Aura API systems are operational and standing by for your next command.",
                "uptime": uptime_str,
            }
        )
