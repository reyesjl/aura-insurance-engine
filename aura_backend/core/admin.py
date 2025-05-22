from django.contrib import admin
from core.models import Carrier, CoverageLine, Question, ApplicationSession, Submission

class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class CoverageLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ('text',)
    filter_horizontal = ('carriers', 'coverages')

class ApplicationSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'created_at', 'status')
    search_fields = ('token', 'status')
    list_filter = ('status', 'created_at')
    filter_horizontal = ('carriers', 'coverages')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'submitted_at')
    search_fields = ('session__token',)

admin.site.register(Carrier, CarrierAdmin)
admin.site.register(CoverageLine, CoverageLineAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ApplicationSession, ApplicationSessionAdmin)
admin.site.register(Submission, SubmissionAdmin)