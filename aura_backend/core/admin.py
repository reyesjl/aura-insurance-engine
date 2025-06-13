from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

# Register your custom User model with the built-in UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add custom fields to the admin if you want them editable/searchable
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Agent Info', {
            'fields': ('is_agent', 'agent_name', 'agency', 'phone_number', 'level', 'xp')
        }),
    ]
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Agent Info', {
            'fields': ('is_agent', 'agent_name', 'agency', 'phone_number', 'level', 'xp')
        }),
    )
    list_display = tuple(UserAdmin.list_display) + ('is_agent', 'agent_name', 'agency', 'phone_number', 'level', 'xp')
    search_fields = list(UserAdmin.search_fields) + ['agent_name', 'agency', 'phone_number']

@admin.register(InsuranceType)
class InsuranceTypeAdmin(admin.ModelAdmin):
    search_fields = ['key', 'label']
    list_display = ['key', 'label']
    list_filter = ['key']

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    filter_horizontal = ['insurance_types']
    list_filter = ['insurance_types']

@admin.register(CoverageLine)
class CoverageLineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'abbreviation']
    list_display = ['name', 'abbreviation']
    filter_horizontal = ['insurance_types']
    list_filter = ['insurance_types']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['text']
    list_display = ['text']
    filter_horizontal = ['carriers', 'coverages', 'insurance_types']
    list_filter = ['insurance_types', 'carriers', 'coverages']

@admin.register(ApplicationTemplate)
class ApplicationTemplateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'insurance_type', 'created_at']
    filter_horizontal = ['carriers', 'coverages']
    list_filter = ['insurance_type', 'carriers', 'coverages']

@admin.register(TemplateQuestionSnapshot)
class TemplateQuestionSnapshotAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_display = ['template', 'original_question', 'question_text']
    list_filter = ['template', 'original_question']

@admin.register(ApplicationSession)
class ApplicationSessionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'token']
    list_display = ['name', 'template', 'token', 'created_at', 'status']
    list_filter = ['template', 'status']

@admin.register(ApplicationAnswer)
class ApplicationAnswerAdmin(admin.ModelAdmin):
    search_fields = ['answer', 'question_snapshot__question_text']
    list_display = ['session', 'question_snapshot', 'answer']
    list_filter = ['session', 'question_snapshot']

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    search_fields = ['session__name', 'session__token']
    list_display = ['session', 'submitted_at']
    list_filter = ['submitted_at']