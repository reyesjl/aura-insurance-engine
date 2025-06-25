from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from core import views
from core.views import ApiInfo, ApiHealth
from core.auth_views import login_view, register_view, logout_view, user_profile_view
from core.application_views import get_carriers_by_coverage, create_application_session, preview_questions

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
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
    path('api/info/', ApiInfo.as_view(), name='api-info'),
    path('api/health/', ApiHealth.as_view(), name='api-health'),
    
    # JWT Auth endpoints
    path('api/auth/login/', login_view, name='login'),
    path('api/auth/register/', register_view, name='register'),
    path('api/auth/logout/', logout_view, name='logout'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/profile/', user_profile_view, name='user_profile'),
    
    # New application workflow endpoints
    path('api/carriers-by-coverage/', get_carriers_by_coverage, name='carriers-by-coverage'),
    path('api/create-application-session/', create_application_session, name='create-application-session'),
    path('api/preview-questions/', preview_questions, name='preview-questions'),
]
