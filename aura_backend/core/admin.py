from django.contrib import admin
from core.models import Carrier, CoverageLine, Question, ApplicationSession, Submission

admin.site.register(Carrier)
admin.site.register(CoverageLine)
admin.site.register(Question)
admin.site.register(ApplicationSession)
admin.site.register(Submission)