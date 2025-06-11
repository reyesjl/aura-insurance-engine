from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'insurance-types', views.InsuranceTypeViewSet)
router.register(r'carriers', views.CarrierViewSet)
router.register(r'coverage-lines', views.CoverageLineViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'application-templates', views.ApplicationTemplateViewSet)
router.register(r'template-question-snapshots', views.TemplateQuestionSnapshotViewSet)
router.register(r'application-sessions', views.ApplicationSessionViewSet)
router.register(r'application-answers', views.ApplicationAnswerViewSet)
router.register(r'submissions', views.SubmissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
