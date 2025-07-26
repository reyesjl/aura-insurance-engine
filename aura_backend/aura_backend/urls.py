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

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from core import views
from core.application_views import (
    application_session_details,
    authenticate_application_session,
    create_application_session,
    get_carriers_by_coverage,
    preview_questions,
    roll_application_session_token,
    verify_application_token,
)
from core.auth_views import login_view, logout_view, register_view, user_profile_view
from core.views import ApiHealth, ApiInfo

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"insurance-types", views.InsuranceTypeViewSet)
router.register(r"carriers", views.CarrierViewSet)
router.register(r"coverage-lines", views.CoverageLineViewSet)
router.register(r"questions", views.QuestionViewSet)
router.register(r"application-templates", views.ApplicationTemplateViewSet)
router.register(r"template-question-snapshots", views.TemplateQuestionSnapshotViewSet)
router.register(r"application-sessions", views.ApplicationSessionViewSet)
router.register(r"application-answers", views.ApplicationAnswerViewSet)
router.register(r"submissions", views.SubmissionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/info/", ApiInfo.as_view(), name="api-info"),
    path("api/health/", ApiHealth.as_view(), name="api-health"),
    # JWT Auth endpoints
    path("api/auth/login/", login_view, name="login"),
    path("api/auth/register/", register_view, name="register"),
    path("api/auth/logout/", logout_view, name="logout"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/profile/", user_profile_view, name="user_profile"),
    # New application workflow endpoints
    path(
        "api/carriers-by-coverage/",
        get_carriers_by_coverage,
        name="carriers-by-coverage",
    ),
    path(
        "api/create-application-session/",
        create_application_session,
        name="create-application-session",
    ),
    path("api/preview-questions/", preview_questions, name="preview-questions"),
    path(
        "api/application-session-details/<int:session_id>/",
        application_session_details,
        name="application-session-details",
    ),
    path(
        "api/application-session/<int:session_id>/roll-token/",
        roll_application_session_token,
        name="roll-application-session-token",
    ),
    path(
        "api/application-session/verify-token/<uuid:token>/",
        verify_application_token,
        name="verify-application-token",
    ),
    path(
        "api/application-session/authenticate/<uuid:token>/",
        authenticate_application_session,
        name="authenticate-application-session",
    ),
]
