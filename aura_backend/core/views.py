from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session = ApplicationSession.objects.create()
        session.carriers.set(Carrier.objects.filter(id__in=data['carriers']))
        session.coverages.set(CoverageLine.objects.filter(id__in=data['coverages']))
        session.save()
        return JsonResponse({'token': str(session.token)}, status=201)

def fill_session(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        carrier_ids = session.carriers.values_list('id', flat=True)
        coverage_ids = session.coverages.values_list('id', flat=True)
        questions = Question.objects.filter(
            carriers__id__in=carrier_ids,
            coverages__id__in=coverage_ids
        ).distinct()

        return JsonResponse({
            'questions': [{'id': q.id, 'text': q.text} for q in questions]
        })

    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)

@csrf_exempt
def submit_form(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        if session.status == 'complete':
            return JsonResponse({'error': 'Already submitted'}, status=400)
        data = json.loads(request.body)
        Submission.objects.create(session=session, answers=data['answers'])
        session.status = 'complete'
        session.save()
        return JsonResponse({'status': 'submitted'})
    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)

def get_status(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        if session.status == 'complete':
            submission = Submission.objects.get(session=session)
            return JsonResponse({
                'status': 'complete',
                'answers': submission.answers
            })
        else:
            return JsonResponse({'status': session.status})
    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)